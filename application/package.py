class DependencyLink:
    def __init__(self,name,hrefName=""):
        self.name = [name,"asd"]
        self.href = ["/packages/{}".format(hrefName),None]
        self.content = zip(self.name,self.href)

class Package:
    def __init__(self, name, descriptionBeginning, descriptionAll, dependencies):
        self.name = name
        self.descriptionBeginning= descriptionBeginning
        self.descriptionAll= descriptionAll
        self.dependencies= dependencies
        self.dependencyLinks = []
        self.dependants = []
        self.dependantLinks = []
        self.href = "/packages/{}".format(name)

    def getAll(self):
        return (self.name, self.descriptionBeginning, self.dependencies)

    def getName(self):
        return self.name

    def getDescription(self):
        return ("{}{}").format(self.descriptionBeginning, self.descriptionRest)

    def getDependencies(self):
        return self.dependencies
    
    def addDependency(self,dependencyName):
        self.dependencyLinks.append(DependencyLink(dependencyName))

    def addDependant(self, other):
        self.dependantLinks.append(DependencyLink(other,other))
        self.dependants.append(other)

