##A Program by Martyn Palmer - 10/2/2018
##Sets up a text file of revision phrases that can be used in the Post Comments program

import os.path

revision_list = []
hash_tag = " #ReviseCompSci"

def enterPoint():
##    Allows the user to enter a point and then checks to see if its under a 250 character limit.
##    Gets added to the revision list at the end. 
    global revision_list
    print("Enter a Revision Point (No more than 250 characters)")
    point = input("> ")
    point = point + hash_tag
    while len(point) > 250:
        print("Sorry too many characters entered, try again")
        point = input("> ")

    revision_list.append(point)

    return True

def openFile():
##    Opens the revision data text file, reads in the information, stips out formatting
##    characters and adds to the revision list array. 
    global revision_list

    if os.path.isfile("computing_revision_data.txt"):
        data = open("computing_revision_data.txt", "r")
        for line in data:
            line = line.strip("\n")
            if len(line) < 250:
                revision_list.append(line)
        data.close()
        return True
    else:
        print("Error - No file exists")
        return False
        
def writeFile():
##    Writes the contens of the computing_revision list back to the text file. 
    data = open("computing_revision_data.txt", "w")
    for item in revision_list:
        line = item + "\n"
        data.write(line)
    print("Data written to text file")
    data.close

def printList():
##    Outputs the revision list to the screen. 
    for item in revision_list:
        print(item + "\n")

def setHashtag():
##    Allows the user to change the default hash tag to be added onto the end of a tweet
    global hash_tag
    print("Current hash tag is " + hash_tag)
    change_hash = input("Do you want to change the hash tag? ")
    if len(change_hash) > 1:
        change_hash = change_hash[0]

    if change_hash.lower() == "y":
        print("Enter a new hash tag")
        hash_tag = input("> ")
        


#### Main Program ####

choice = 0
loaded = False

while choice != 9:
    if not loaded:
        if openFile():
            print("Data loaded")
            loaded = True
##If the data has not been loaded it will load the data from the text file. 
    
    print('''
        **** Setup Revision menu ****
        1. Update revision list
        2. Add point to revision list
        3. Update text file
        4. Print list of revision points
        5. Set Hash Tag
        9. quit
    ''')
    choice = int(input("> "))

##Allows the user to choose from a list of options

    if choice == 1:
        openFile()
    elif choice == 2:
        enterPoint()
    elif choice == 3:
        writeFile()
    elif choice == 4:
        printList()
    elif choice == 5:
        setHashtag()
    elif choice == 9:
        sure = input("Are you sure: ")
        if len(sure) > 1:
            sure = sure[0]
        else:
            sure = sure.lower()

        if sure != "y":
            choice = 0
    else:
        print("invalid option")

##Checks the options against the preset criteria and calls the relevant function
