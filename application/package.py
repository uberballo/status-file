class DependencyLink:
    def __init__(self, name, hrefNames=[]):
        self.name = name
        self.href = []
        for hrefName in hrefNames:
            if hrefName:
                self.href.append("/packages/{}".format(hrefName))
            else:
                self.href.append(None)
        self.content = []
        self.content = list(zip(self.name, self.href))


class Package:
    def __init__(self, name,  description, dependencies):
        self.name = name
        if description:
            self.descriptionBeginning = description.split("\n")[0]
            self.descriptionAll = description
        self.dependencies = dependencies
        self.dependencyLinks = []
        self.dependantLinks = []
        self.href = "/packages/{}".format(name)

    def getAll(self):
        return (self.name, self.descriptionBeginning, self.dependencies)

    def getName(self):
        return self.name

    def getDependencies(self):
        return self.dependencies

    def addDependency(self, dependencyName, hrefName=None):
        self.dependencyLinks.append(DependencyLink(dependencyName, hrefName))

    def addDependant(self, other):
        self.dependantLinks.append(DependencyLink([other], [other]))
