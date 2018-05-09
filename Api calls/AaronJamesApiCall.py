import sys
import urllib.request
import json
import time

myList = []
printableList = []

def main():
    #Read in Symbols from config file to myList[]
    readSymbols()
    #Creates a loop that runs every thirty seconds
    looper()
    
def looper():
    infinity = 1
    while infinity != 0:
        Iteration()
        #sleep for 30 seconds
        time.sleep(30)
    
def readSymbols():
    with open('config.txt', 'r') as f:
        file = f.read()
        for value in file.split(","):
            myList.append(value)

def Iteration():
    for value in myList:
        createdString = "https://api.iextrading.com/1.0/stock/" + value + "/news/"
        try:
            fob = urllib.request.urlopen(createdString)
            data = fob.read()
            companydata = json.loads(data)
            for temp in companydata:
                mdt = monthdatetime(temp['datetime'])
                print(mdt)
                print(temp['source'] + " : " + temp['headline'])
                print(temp['url'])
                print("Tags : " + temp['related'])
                print("")
                print("")
                
        except:
            print("Sorry the data symbol was not found, try again later")
            
    return 0

def monthdatetime(temp):
    temp = temp.replace('-', ',')
    temp = temp.replace('T', ',')
    temparr = temp.split(',')

    if str(temparr[1]) == "01":
        temparr[1] = "January"
    elif str(temparr[1]) == "02":
        temparr[1] = "Febuary"
    elif str(temparr[1]) == "03":
        temparr[1] = "March"
    elif str(temparr[1]) == "04":
        temparr[1] = "April"
    elif str(temparr[1]) == "05":
        temparr[1] = "May"
    elif str(temparr[1]) == "06":
        temparr[1] = "June"
    elif str(temparr[1]) == "07":
        temparr[1] = "July"
    elif str(temparr[1]) == "08":
        temparr[1] = "Augest"
    elif str(temparr[1]) == "09":
        temparr[1] = "Septemeber"
    elif str(temparr[1]) == "10":
        temparr[1] = "October"
    elif str(temparr[1]) == "11":
        temparr[1] = "November"
    else:
        temparr[1] = "December"
            

    compiledString = ("======== ["+ temparr[1], temparr[2], temparr[0] + " , " + temparr[3]+ "] ========")
    return compiledString
    
    
main()
