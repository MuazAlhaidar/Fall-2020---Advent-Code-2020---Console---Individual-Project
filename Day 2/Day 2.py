def getInput():
    f = open("input.txt")
    stringList = f.read().split()
    fileInput = []
    for x in range(0, len(stringList), 3):
        fileInput.append(
            [stringList[x].split("-"), stringList[x + 1][0], stringList[x + 2]]
        )
    return fileInput


def getPasswordsValidRange(fileInput):
    validPasswords = 0
    counter = 0
    for x in range(len(fileInput)):
        counter = fileInput[x][2].count(fileInput[x][1])
        if counter >= int(fileInput[x][0][0], base=10) and counter <= int(
            fileInput[x][0][1], base=10
        ):
            validPasswords += 1
    return validPasswords


def getPasswordsValidPositions(fileInput):
    validPasswords = 0
    for x in range(len(fileInput)):
        isAtFirstPos = (
            fileInput[x][2][int(fileInput[x][0][0], base=10) - 1] == fileInput[x][1]
        )
        isAtSecPos = (
            fileInput[x][2][int(fileInput[x][0][1], base=10) - 1] == fileInput[x][1]
        )
        if isAtFirstPos ^ isAtSecPos:
            validPasswords += 1
    return validPasswords


passwordInput = getInput()

validPasswords = getPasswordsValidRange(passwordInput)
print(validPasswords)

validPasswords = getPasswordsValidPositions(passwordInput)
print(validPasswords)
