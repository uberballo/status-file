import re
from time import time
from application.package import Package
from application.regexPatterns import *

def parsePackages(fileLocation):
    listOfPackages = []
    with open(fileLocation, "r") as f:
        name = ""
        descriptionBeginning = ""
        description = ""
        dependencies = []
        descriptionFound = False

        for line in f:
            if not descriptionFound:

                if re.match(packagePattern, line):
                   name = re.search(searchPackagePattern, line).group()

                if re.match(dependencyPattern, line):
                   foundDependencies = re.search(searchDependencyPattern, line).group()
                   foundDependencies = re.sub(replaceMiscDependcyPattern, '', foundDependencies)
                   dependencies = re.split(',', foundDependencies)
                   dependencies = list(set(dependencies))

                if re.match(descriptionPattern, line):
                   descriptionBeginning= re.search(searchDescriptionPattern, line).group()
                   description =  line
                   descriptionFound = True
            else:
                description = description + line

                if line == "\n" :
                    description = re.search(searchWholeDescriptionPattern, description)
                    if description:
                        description =description.group()
                        description = re.sub('Homepage: .*','',description)

                    package = Package(name, descriptionBeginning,description, dependencies)
                    listOfPackages.append(package)
                    descriptionFound = False
                    name, descriptionBeginning, descriptionFound, description  = "","","",""
                    dependencies = []


        listOfPackages.sort(key=lambda package: package.name)
        findDependants(listOfPackages)
        handlePackageDependencies(listOfPackages)
        return listOfPackages


def findDependants(listOfPackages):
    for package in listOfPackages:
        packageDepencies = package.dependencies
        if (packageDepencies):
            for dependency in packageDepencies:
                dependant = next((x for x in listOfPackages if dependency ==
                             x.name), None)
                if dependant:
                    dependant.addDependant(package.name)

def handlePackageDependencies(listOfPackages):
    for package in listOfPackages:
        for dependency in package.dependencies:
            splittedDepencyList = filter(None,re.split("(\|.+)",dependency))
            names = []
            hrefNames = []

            for splittedDependency in splittedDepencyList:
                trimmedSplittedDependency = splittedDependency.replace("|","").strip()
                foundDependency = next((x for x in listOfPackages if trimmedSplittedDependency==
                             x.name), None)

                if foundDependency:
                    names.append(splittedDependency)
                    hrefNames.append(trimmedSplittedDependency)

                else:
                    names.append(splittedDependency)
                    hrefNames.append(None)
            package.addDependency(names,hrefNames)

