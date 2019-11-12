import re

class Paketti:
    def __init__(self, teksti):
        self.nimi = re.match(r'^Package: .*',teksti)
        self.riippuvuudet = []
        self.kuvaus = ""
        self.depentants = []
    
    def addDependant(self, dependant):
        self.depentants.append(depentant)

    def getNimi(self):
        print(self.nimi)


def paketit2():
    packages = []
    with open("status", "r") as f:
        counter = 0
        teksti = ""
        name = ""
        description = ""
        dependencies = ""
        descriptionFound = False

        for line in f:
             if re.match(r'^Package: (.*)$',line):
                name = re.search(r'(?<=Package: ).*',line).group()

             if re.match(r'^Depends: (.*)$',line):
                dependencies = re.search(r'(?<=Depends: ).*',line).group()
                dependencies = re.sub('\((.*?)\)','',dependencies)
                print(dependencies)
             if re.match(r'^Description: (.*)',line):
               # print(line)
                description = re.search(r'(?<=^Description: ).*',line).group()
             #  print("des",description)
                descriptionFound = True

             if line == "\n":
                temp = Paketti(teksti):
                    if temp:
                        packages.append(temp)
                descriptionFound = False
        return packages

def findDependants(listOfPackages):
    for package in listOfPackages:
        packageDepencies = package.dependencies
        for packageDependant in packageDepencies:
            dependant = (x for x in listOfPackages if packageDependant.name ==
                         package.name)
            package.addDependant(dependant)
    return listOfPackages

paketit = paketit2()
print(paketit)
#findDependants(paketit)
