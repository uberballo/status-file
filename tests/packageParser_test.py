import pytest
from application.packageParser import parsePackages,findDependants

correctPackages = [
    "java-common",
    "libaspectj-java",
    "libbsf-java",
    "libplexus-sec-dispatcher-java",
    "libslf4j-java",
    "libtext-charwidth-perl",
    "libtext-wrapi18n-perl",
    "libws-commons-util-java",
    "python-pkg-resources",
    "tcpd"
]

@pytest.fixture
def parsedPackages():
    return parsePackages("testStatus")

def findCorrectPackage(parsedPackages,name):
    return  next(package for package in parsedPackages if
                                      package.name ==
                                      name)

def test_packagesAreSortedCorrectly(parsedPackages):
    temporaryCorrectPackages = correctPackages
    temporaryCorrectPackages.sort()
    assert(all([a == b.name for a, b in zip(temporaryCorrectPackages,
                                            parsedPackages)]))

def test_packagesHaveCorrectLength(parsedPackages):
    assert(len(correctPackages) == len(parsedPackages))

def test_packagewithnodepenciescontainsnodependencies(parsedPackages):
    testPackage = findCorrectPackage(parsedPackages, "libws-commons-util-java")
    testPackageDepencies = testPackage.dependencies
    assert(len(testPackageDepencies) == 0)

def test_packageContainsCorrectDependencies(parsedPackages):
    testPackage = findCorrectPackage(parsedPackages, "tcpd")
    testPackageDependencies= testPackage.getDependencies()
    correctDependencies = [
        "libc6",
        "libwrap0"
    ]
    assert(len(testPackageDependencies) == len(correctDependencies))
    assert(all(a == b for a,b in
               zip(correctDependencies, testPackageDependencies)))

def test_packageDependantsAreCorrect(parsedPackages):
    findDependants(parsedPackages)
    testPackage = findCorrectPackage(parsedPackages, "libtext-charwidth-perl")
    assert(testPackage.dependants[0] == "libtext-wrapi18n-perl")

def test_packageDescriptionIsCorrect(parsedPackages):
    testPackage = findCorrectPackage(parsedPackages, "libws-commons-util-java")
    correctDescription = """
    Common utilities from the Apache Web Services Project
 This is a small collection of utility classes, that allow high
 performance XML processing based on SAX.
    """
    assert(testPackage.descriptionAll.strip() == correctDescription.strip())

