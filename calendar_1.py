import csv
class calendar:
    def __init__ (self, name, description, date, completed):
        self.name = name
        self.description = description
        self.date = date
        self.completed = completed
event0 = calendar("Event 0", "This is a description of 0", "Feb 3", False)

def checkEvent(eventDict, userInput):
    if userInput in eventDict:
        return True
    else:
        return False

numEvent = 1
eventNameDict = {"Event 0": "event0"}
print("Welcome to the Calendar App")
while True:
    print("1. Add an Event")
    print("2. Print out a Description of an Event")
    print("3. Check if Event is Completed")
    print("4. Print the Date of an Event")
    print("5. Check off an Event")
    print("6. Show List of Events")
    userInput = input("Choose an option number: ")
    if userInput == "1":
        name = input("What is the name of the event? ")
        description = input("What is the description of the event? ")
        date = input("What is the date of the event? ")
        objectName = "event" + str(numEvent)
        globals()[objectName] = calendar(name, description, date, False)
        eventNameDict[name] = objectName
        numEvent += 1
    elif userInput == "2":
        eventName = input("What event would you like to see? ")
        if checkEvent(eventNameDict, eventName):
            print(globals()[eventNameDict[eventName]].description)
        else:
            print("Event Does Not exist. Please Try Again")
    elif userInput == "3":
        eventName = input("What event would you like to check if completed? ")
        if checkEvent(eventNameDict, eventName):
            if globals()[eventNameDict[eventName]].completed == False:
                print(eventName + " is not completed yet")
            else:
                print(eventName + " is completed")
        else:
            print("Event Does Not exist. Please Try Again")
    elif userInput == "4":
        eventName = input("What event would you like to know the date of? ")
        if checkEvent(eventNameDict, eventName):
            eventDate = globals()[eventNameDict[eventName]].date
            print(eventName + " is on " + eventDate)
        else: 
            print("Event Does Not exist. Please Try Again")
    elif userInput == "5":
        eventName = input("What event have you completed? ")
        if checkEvent(eventNameDict, eventName):
            globals()[eventNameDict[eventName]].completed = True
        else:
            print("Event Does Not exist. Please Try Again")