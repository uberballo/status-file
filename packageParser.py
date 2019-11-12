import re
from time import time

class Paketti:
    def __init__(self, name, descriptionBeginning, descriptionRest, dependencies):
        self.name = name
        self.descriptionBeginning= descriptionBeginning
        self.descriptionRest= descriptionRest
        self.dependencies= dependencies
        self.dependants = []

    def getAll(self):
        return (self.name, self.descriptionBeginning, self.dependencies)

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getDependencies(self):
        return self.dependencies

    def addDependant(self, other):
        self.dependants.append(other)


def parsePackages():
    listOfPackages = []
    with open("status", "r") as f:
        name = ""
        descriptionBeginning = ""
        descriptionRest= ""
        dependencies = []
        descriptionFound = False

        for line in f:
            if not descriptionFound:
                if re.match(r'^Package: (.*)$', line):
                   name = re.search(r'(?<=Package: ).*', line).group()

                if re.match(r'^Depends: (.*)$', line):
                   foundDependencies = re.search(r'(?<=Depends: ).*', line).group()
                   foundDependencies = re.sub('\s|\((.*?)\)', '', foundDependencies)
                   #For now both of the dependencies is included
                   dependencies = re.split(',|\|', foundDependencies)

                if re.match(r'^Description: (.*)', line):
                   descriptionBeginning= re.search(r'(?<=^Description: ).*', line).group()
                   descriptionFound = True
            else:
                descriptionRest= descriptionRest+ line

            if line == "\n":
                paketti = Paketti(name, descriptionBeginning,descriptionRest, dependencies)
                listOfPackages.append(paketti)
                descriptionFound = False

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
