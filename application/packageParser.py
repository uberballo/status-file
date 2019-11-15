import re
from application.package import Package

def parsePackages(fileLocation):
    listOfPackages = []
    with open(fileLocation, "r") as f:
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
                package = Package(name, descriptionBeginning,descriptionRest, dependencies)
                listOfPackages.append(package)
                descriptionFound = False
                name,descriptionBeginning,descriptionFound = "","",""
                dependencies = []
        listOfPackages.sort(key=lambda package: package.name)
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
