import os
import sys
from flask import Flask, request, render_template, url_for, redirect
from werkzeug.utils import secure_filename
from application import app
#from application.packageParser import parsePackages, findDependants
from application.packageHandler import getPackageData

os.makedirs(os.path.join(app.instance_path, 'status'), exist_ok=True)
packages = ()
statusPath = ""


@app.route("/")
def fileFrontPage(errorMessage=""):
    global packages
    packages = ()
    return render_template('frontpage.html', errorMessage=errorMessage)


@app.route("/packages")
def allPackages(errorMessage=""):
    global packages
    if not packages:
        path = "status.real"
        packages = getPackageData(path)
    return render_template('index.html', packages=packages, errorMessage=errorMessage)


@app.route("/packages/<packageName>")
def singlePackage(packageName):
    try:
        shownPackage = next(package for package in packages if package.name ==
                            packageName)
        return render_template('package.html', package=shownPackage)
    except:
        errorMessage = "Error {} occured".format(sys.exc_info()[0])
        return render_template('index.html', packages=packages, errorMessage=errorMessage)


@app.route("/handleUpload", methods=['POST'])
def handleFileUpload():
    if 'statusFile' in request.files:
        statusFile = request.files['statusFile']
        try:
            if statusFile.filename == 'status' or statusFile.filename == 'status.real':
                if isinstance(statusFile, str):
                    fileName = secure_filename(statusFile.filename)
                    path = os.path.join(app.instance_path, 'status', fileName)
                    statusFile.save(path)

                    global packages
                    packages = getPackageData(path)
                    # findDependants(packages)

                    return render_template('index.html', packages=packages)
            else:
                return render_template('frontpage.html', errorMessage="Invalid file")
        except:
            errorMessage = "Error {} occured".format(sys.exc_info()[0])
            return render_template('frontpage.html', errorMessage=errorMessage)
