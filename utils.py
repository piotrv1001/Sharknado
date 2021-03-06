def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def convertToNumber(species):
    species = species.replace(" ", "")
    species = species.lower()
    string = ""
    isFoot = False
    for i in range(1, len(species)):
        if species[i].isnumeric():
            if species[i - 1].isnumeric() or species[i - 1] == "." or string == "":
                string += species[i]
                if species[i - 1] == ".":
                    break
        elif species[i] == "." and species[i - 1].isnumeric():
            string += species[i]
            
    if species.find("'") != -1 or species.find("feet") != -1:
        isFoot = True
    if string != "" and isFloat(string):
        num = float(string)
    else:
        num = -1
    if isFoot:
        num *= 0.3048
    elif species.find("cm") != - 1:
        num /= 100

    return num

def determineSize(num):

    size = ""
    if num <= 2.5:
        size = "small"
    elif num <= 7:
        size = "medium"
    else:
        size = "big"

    return size if num != -1 else ""


if __name__ == '__main__':

    size = convertToNumber("Bull shark, 100cm")
    print(size)
    print(determineSize(size))