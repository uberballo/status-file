import re


def findDependants(package, tupleOfPackages):
    if package.dependencies:
        for dependency in package.dependencies:
            dependant = next(
                (x for x in tupleOfPackages if dependency == x.name), None)
            if dependant:
                dependant.addDependant(package.name)
    return package


def handlePackageDependencies(package, tupleOfPackages):
    for dependency in package.dependencies:
        names = []
        hrefNames = []
        splittedDepencyList = filter(None, re.split("(\|.+)", dependency))

        for splittedDependency in splittedDepencyList:
            foundDependency = next(
                (x for x in tupleOfPackages if splittedDependency == x.name), None)

            names.append(splittedDependency)
            hrefNames.append(
                splittedDependency if foundDependency else None)

            package.addDependency(names, hrefNames)

    return package


def createDependencies(tupleOfPackages):
    newTupleOfPackages = ()
    for package in tupleOfPackages:
        newPackage = handlePackageDependencies(package, tupleOfPackages)
        newPackage = findDependants(newPackage, tupleOfPackages)
        print(package.name)
        newTupleOfPackages = newTupleOfPackages + (newPackage,)

    return newTupleOfPackages
