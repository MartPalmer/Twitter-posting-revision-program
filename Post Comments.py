##Program created by Martyn Palmer - 10/2/2018
##Program loads in a data file of revision comments and tweets them every day

import twitter
import os.path
import time
import datetime

revision_list = []
keys = []

def settings():
##    Loads the twitter settings from a text file and uses it to log into twitter
##    and use their api. 
    
    global keys

    setting_data = open("settings.txt", "r")
    keys = list(setting_data)
    
    for counter in range(0, len(keys)):
        keys[counter] = keys[counter].strip("\n")
        keys[counter] = keys[counter].split("\"")

    setting_data.close()

def openFile():
##    Opens the data file (revision phrases) and adds them to an array
    global revision_list

    revision_list = []

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


settings()

api = twitter.Api(consumer_key=keys[0][1],
                  consumer_secret=keys[1][1],
                  access_token_key=keys[2][1],
                  access_token_secret=keys[3][1])

print("Logged in to twitter")

##Gets the settings for the twitter and logs in

counter = 0
while counter != 999:
    openFile()
    try:
        status = api.PostUpdate(revision_list[counter])
        t = (60*60)*24
        time.sleep(t)
        counter += 1
##        Posts the comments on twitter then waits 1 day before posting again. 

        
        
    except:
        print("Error")
        counter = counter+1
##        If post exists in the twitter it skips and updates the counter

    if counter > len(revision_list):
        counter = 999

##        When the last post has been posted quits out of the loop and finishes the program


