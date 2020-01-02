import re


def findDependants(tupleOfPackages):
    newTupleOfPackages = ()
    for package in tupleOfPackages:
        if package.dependencies:
            for dependency in package.dependencies:
                dependant = next(
                    (x for x in tupleOfPackages if dependency == x.name), None)
                if dependant:
                    dependant.addDependant(package.name)
        newTupleOfPackages = newTupleOfPackages + (package, )
    return newTupleOfPackages


def handlePackageDependencies(tupleOfPackages):
    newTupleOfPackages = ()
    for package in tupleOfPackages:
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

        newTupleOfPackages = newTupleOfPackages + (package,)
    return newTupleOfPackages


def createDependencies(tupleOfPackages):
    newTupleOfPackages = ()
    newTupleOfPackages = handlePackageDependencies(tupleOfPackages)
    newTupleOfPackages = findDependants(newTupleOfPackages)
    return newTupleOfPackages
