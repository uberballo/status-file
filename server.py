import os
import sys
from flask import Flask, request, render_template, url_for, redirect
from werkzeug.utils import secure_filename
from packageParser import parsePackages, findDependants

app = Flask(__name__)
os.makedirs(os.path.join(app.instance_path, 'status'), exist_ok=True)
packages  = []
#unused
statusPath = ""
#findDependants(packages)

@app.route("/" )
def fileFrontPage(errorMessage = ""):
    global packages
    packages = []
    return render_template('frontpage.html',errorMessage= errorMessage)

@app.route("/packages")
def allPackages():
    global packages
    if not packages:
        packages = parsePackages("status")
        findDependants(packages)
    return render_template('index.html', packages = packages)

@app.route("/packages/<packageName>")
def singlePackage(packageName):
    shownPackage = next(package for package in packages if package.name ==
                        packageName)
    return render_template('package.html', package=shownPackage)

@app.route("/handleUpload", methods=['POST'])
def handleFileUpload():
    if 'statusFile' in request.files:
        statusFile = request.files['statusFile']
        try:
            if statusFile.filename == 'status' or statusFile.filename =='status.real':
                fileName = secure_filename(statusFile.filename)
                path = os.path.join(app.instance_path, 'status', fileName)
                statusFile.save(path)

                global packages
                packages = parsePackages(path)
                findDependants(packages)

                return render_template('index.html', packages = packages)
        except:
            #errorMessage = "Error "+sys.exc_info()[0]+" occured"
            errorMessage = "Error {} occured".format(sys.exc_info()[0])
            return render_template('frontpage.html', errorMessage = errorMessage)

if __name__ == "__main__":
    app.run()
