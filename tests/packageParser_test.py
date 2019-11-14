import pytest
from application.packageParser import parsePackages

correctPackages = [
    "java-common",
    "libaspectj-java",
    "libbsf-java",
    "libplexus-sec-dispatcher-java",
    "libslf4j-java",
    "libtext-wrapi18n-perl",
    "libws-commons-util-java",
    "python-pkg-resources",
    "tcpd"
]

@pytest.fixture
def parsedPackages():
    return parsePackages("testStatus")

def test_packagesAreSortedCorrectly(parsedPackages):
    temporaryCorrectPackages = correctPackages
    temporaryCorrectPackages.sort()
    packages= parsedPackages
    assert(all([a == b.name for a, b in zip(temporaryCorrectPackages, packages)]))

def test_packagesHaveCorrectLength(parsedPackages):
    assert(len(correctPackages) == len(parsedPackages))

def test_packagewithnodepenciescontainsnodependencies(parsedPackages):
    testpackage =  next(package for package in parsedPackages if
                                      package.name ==
                                      "libws-commons-util-java")
    testpackagedepencies = testpackage.dependencies
    assert(len(testpackagedepencies) == 0)

def test_packageContainsCorrectDependencies(parsedPackages):
    testPackage =  next(package for package in parsedPackages if
                                      package.name ==
                                      "tcpd")
    testPackageDepencies = testPackage.dependencies
    correctDependencies = [
        "libc6",
        "libwrap0"
    ]

    assert(len(testPackageDepencies) == len(correctDependencies))
    assert(all(a == b for a,b in
               zip(correctDependencies, testPackageDepencies)))

