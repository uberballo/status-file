import os
from flask import Flask, request, render_template, url_for, redirect
from werkzeug.utils import secure_filename
from packageParser import parsePackages2,parsePackages, findDependants

app = Flask(__name__)
os.makedirs(os.path.join(app.instance_path, 'status'), exist_ok=True)
packages  = []
#findDependants(packages)

@app.route("/", methods=['GET', 'POST'])
def fileFrontPage():
    return render_template('frontpage.html')

@app.route("/packages")
def allPackages():
    return render_template('layout.html', packages = packages)

@app.route("/packages/<packageName>")
def singlePackage(packageName):
    shownPackage = next(package for package in packages if package.name ==
                        packageName)
    #print(shownPackage.name)
    #print(shownPackage.descriptionBeginning)
    #print(shownPackage.dependencies)
    return render_template('package.html', package=shownPackage)

@app.route("/handleUpload", methods=['POST'])
def handleFileUpload():
    if 'statusFile' in request.files:
        statusFile = request.files['statusFile']
        if statusFile.filename == 'status' or statusFile.filename =='status.real':
            fileName = secure_filename(statusFile.filename)
            path = os.path.join(app.instance_path, 'status', fileName)
            statusFile.save(path)

            global packages
            packages = parsePackages(path)
            findDependants(packages)

            return render_template('layout.html', packages = packages)
    return render_template('frontpage.html')

if __name__ == "__main__":
    app.run()
