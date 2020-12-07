import re


def getInput():
    f = open("input.txt")
    stringList = f.read().split()
    fileInput = []
    for x in range(0, len(stringList), 3):
        fileInput.append(
            [stringList[x].split("-"), stringList[x + 1][0], stringList[x + 2]]
        )
    return fileInput


getInput()