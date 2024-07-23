print("nevada3921")

def readfile():
    with open("names.txt", "r") as file:
        names = file.readlines()
        names.sort()
        
    return names

def writefile(names):
    with open("sorted_names.txt", "w") as file:
        file.writelines(names)
        file.close()
    return file

def appendfile(studentID):
    with open("sorted_names.txt", "a") as file:
        file.writelines(studentID + "\n")
        file.close()
    return file

names = readfile()
writefile(names)
appendfile("nevada3921")

with open("sorted_names.txt", "r") as file:
    names = file.readlines()
    print(names)
 
