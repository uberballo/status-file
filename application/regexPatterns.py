import re

packagePattern = re.compile(r'(?<=(Package: )).*')
searchPackagePattern = re.compile(r'(?<=Package: ).*')
dependencyPattern = re.compile(r'^Depends: (.*)$')
searchDependencyPattern = re.compile(r'(?<=Depends: ).*')
replaceMiscDependcyPattern = re.compile(r'\s|\((.*?)\)')
descriptionPattern = re.compile(r'^Description: (.*)')
searchDescriptionPattern = re.compile(r'(?<=^Description: ).*')
searchWholeDescriptionPattern = re.compile(
    r'(?<=^Description: )(.*\n)*(?=([A-Z]+[a-z]*[-]*[A-Z][a-z]*: ))')

newSearchDescriptionPattern = re.compile(
    r'(?<=Description: )(.*\n)*?(?=^[A-Z](\d|\D)*:)', re.MULTILINE)
