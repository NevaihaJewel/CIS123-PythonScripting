def HelloWorld():
    print("Hello World, my name is Nevaiha.")
    print("I am a student at ECPI University.")
    print("I have never programmed a computer before.")
    print("This is great!")

def CheckEven():
    num = input("Enter a number: ")
    num = int(num)

    if num % 2:
        print("Number is Odd.")
    else:
        print("Number is Even.")

def Birthday():
    import datetime

    birthdate = input ("What is your birthday (MM/DD/YYYY): ")

    month, day, year = birthdate.split("/")
    bdate = datetime.datetime(int(year), int(month), int(day))
    todaysDate = datetime.datetime.now()
    age = todaysDate - bdate

    print("You are "+str(age.days/365.25)+" years old!")
