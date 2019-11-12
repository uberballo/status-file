import os
from flask import Flask, request, render_template, url_for, redirect
from packageParser import parsePackages, findDependants
#from testi import findDependants
app = Flask(__name__)

packages = parsePackages()
findDependants(packages)

@app.route("/")
def fileFrontPage():
    return render_template('layout.html', packages = packages)

@app.route("/<packageName>")
def singlePackage(packageName):
    shownPackage = next(package for package in packages if package.name ==
                        packageName)
    #print(shownPackage.name)
    print(shownPackage.descriptionBeginning)
    #print(shownPackage.dependencies)
    return render_template('package.html', package=shownPackage)

@app.route("/handleUpload", methods=['POST'])
def handleFileUpload():
    path2 = '/var/lib/dpkg/status'

    if 'photo' in request.files:
        photo = request.files['photo']
        if photo.filename != '':
            cwd = os.getcwd()
            photo.save(os.path.join(cwd, photo.filename))
    return redirect(url_for('fileFrontPage'))

if __name__ == "__main__":
    app.run()
