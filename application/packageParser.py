import re
from time import time
from application.package import Package

packagePattern = re.compile(r'(?<=(Package: )).*')
searchDependencyPattern = re.compile(r'(?<=Depends: ).*')
replaceMiscDependcyPattern = re.compile(r'\s|\((.*?)\)')
newSearchDescriptionPattern = re.compile(
    r'(?<=Description: )(.*\n)*?(?=^[A-Z](\d|\D)*:)', re.MULTILINE)


def parsePackages(fileLocation):
    tupleOfPackages = ()
    try:
        with open(fileLocation, "r") as f:
            listOfLines = filter(None, f.read().split("\n\n"))

            for line in listOfLines:
                tupleOfPackages = tupleOfPackages + (handleLine(line),)
        return tupleOfPackages
    except:
        return ()


def handleLine(line):
    name = getPackageName(line)
    description = getDescription(line)
    dependencies = getDependencies(line)
    package = Package(name,  description, dependencies)
    return package


def getPackageName(line):
    packageName = re.search(packagePattern, line)
    return packageName.group() if packageName else None


def getDescription(line):
    description = re.search(newSearchDescriptionPattern, line)
    return description.group() if description else None


def getDependencies(line):
    try:
        dependencies = re.search(searchDependencyPattern, line).group()
        dependencies = re.sub(
            replaceMiscDependcyPattern, '', dependencies)
        dependencies = dependencies.split(",")

        return dependencies
    except:
        return []
