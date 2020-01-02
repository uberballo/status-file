from application.packageParser import parsePackages
from application.dependencyHandler import createDependencies


def getPackageData(path):
    packageData = ()
    packageData = parsePackages(path)
    packageData = createDependencies(packageData)
    packageData = sorted(packageData, key=lambda package: package.name)
    return packageData
