class Package:
    def __init__(self, name, descriptionBeginning, descriptionAll, dependencies):
        self.name = name
        self.descriptionBeginning= descriptionBeginning
        self.descriptionAll= descriptionAll
        self.dependencies= dependencies
        self.dependants = []

    def getAll(self):
        return (self.name, self.descriptionBeginning, self.dependencies)

    def getName(self):
        return self.name

    def getDescription(self):
        return ("{}{}").format(self.descriptionBeginning, self.descriptionRest)

    def getDependencies(self):
        return self.dependencies

    def addDependant(self, other):
        self.dependants.append(other)

