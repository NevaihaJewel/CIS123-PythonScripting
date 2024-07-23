print("nevada3921")

def readFile():
    path = "names.txt"
    names = []
    
    fopen = open(path, "r")
    for line in fopen:
        line = line.replace("\n","")
        names.append(line)
    fopen.close()
    return names

def writeFile(names):
    path = "sorted_names.txt"

    fopen = open(path, "w")
    for line in names:
        fopen.write(line + " \n")
    fopen.close()
    return names

def appendFile(line):
    path = "sorted_names.txt"

    fopen = open(path, "a")
    fopen.write(line + " \n")
    fopen.close()

listNames = readFile()
listNames.sort()
writeFile(listNames)
appendFile("End of file")

with open("sorted_names.txt", "r") as fopen:
    names = fopen.readlines()
    
    print(names)
