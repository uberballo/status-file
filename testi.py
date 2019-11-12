import re
from time import time

class Paketti:
    def __init__(self, name, description, dependencies):
        self.name = name
        self.description= description
        self.dependencies= dependencies
        self.dependants = []

    def getAll(self):
        return (self.name, self.description, self.dependencies)

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getDependencies(self):
        return self.dependencies

    def addDependant(self, other):
        self.dependants.append(other)

 #   def __eq__(self, other):
        #We only compare names for simplicity's sake
  #      return self.name == other.name

def paketit2():
    listOfPackages = []
    with open("status", "r") as f:
        name = ""
        description = ""
        dependencies = []

        for line in f:
            if re.match(r'^Package: (.*)$', line):
               name = re.search(r'(?<=Package: ).*', line).group()

            if re.match(r'^Depends: (.*)$', line):
               foundDependencies = re.search(r'(?<=Depends: ).*', line).group()
               foundDependencies = re.sub('\s|\((.*?)\)', '', foundDependencies)
               #For now both of the dependencies is included
               dependencies = re.split(',|\|', foundDependencies)
               print(dependencies)

            if re.match(r'^Description: (.*)', line):
               description = re.search(r'(?<=^Description: ).*', line).group()

            if line == "\n":
                paketti = Paketti(name, description, dependencies)
                listOfPackages.append(paketti)

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
t0 = time()
paketit = paketit2()
t1 = time()
print(t1-t0)
t0 = time()
findDependants(paketit)
t1 = time()
print(t1-t0)
