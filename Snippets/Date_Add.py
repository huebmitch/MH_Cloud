import os

workingDir = "\\\Tds\\ns\\Teams\\PD\Monthly Ops Review"
appendString = "_1-31-18"
appendExtension = ".xlsx"

os.chdir(workingDir)

for filename in os.listdir(workingDir):
    if filename.endswith(appendExtension):
        sliced = filename[:-5]
        os.rename(filename, sliced + appendString + appendExtension)
