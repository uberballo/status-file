import os
from flask import Flask, request, render_template, url_for, redirect
from testi import paketit2
#from testi import findDependants
import testi
app = Flask(__name__)

packages = paketit2()
testi.findDependants(packages)

@app.route("/")
def fileFrontPage():
    return render_template('layout.html', packages = packages)

@app.route("/<packageName>")
def singlePackage(packageName):
    shownPackage = next(package for package in packages if package.name ==
                        packageName)
    #print(shownPackage.name)
    #print(shownPackage.description)
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
