import re
from time import time
from application.package import Package

def parsePackages(fileLocation):
    listOfPackages = []
    with open(fileLocation, "r") as f:
        name = ""
        descriptionBeginning = ""
        description = ""
        dependencies = []
        descriptionFound = False
        #Doesnt work with homepage line
        pattern = re.compile(r'(?<=^Description: )(.*\n)*(?=([A-Z]+[a-z]*[-]*[A-Z][a-z]*: ))')

        for line in f:
            if not descriptionFound:

                if re.match(r'^Package: (.*)$', line):
                   name = re.search(r'(?<=Package: ).*', line).group()

                if re.match(r'^Depends: (.*)$', line):
                   foundDependencies = re.search(r'(?<=Depends: ).*', line).group()
                   foundDependencies = re.sub('\s|\((.*?)\)', '', foundDependencies)
                   #For now both of the dependencies is included
                   dependencies = re.split(',', foundDependencies)
                   #removing duplicates
                   dependencies = list(set(dependencies))
                if re.match(r'^Description: (.*)', line):
                   descriptionBeginning= re.search(r'(?<=^Description: ).*', line).group()
                   description =  line
                   descriptionFound = True
            else:
                description = description + line

                if line == "\n" :
                    description = re.search(pattern ,description)
                    if description:
                        description =description.group()
                        description = re.sub('Homepage: .*','',description)

                    package = Package(name, descriptionBeginning,description, dependencies)
                    listOfPackages.append(package)
                    descriptionFound = False
                    name,descriptionBeginning,descriptionFound = "","",""
                    description = ""
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
                print(foundDependency)
                if foundDependency:
                    names.append(splittedDependency)
                    hrefNames.append(trimmedSplittedDependency)
                else:
                    names.append(splittedDependency)
                    hrefNames.append(None)
            package.addDependency(names,hrefNames)


