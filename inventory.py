#Aaron James
import os
import sys


stockDic = {1: 3,
            2: 3,
            3: 2,
            4: 2,
            5: 5,
            6: 5,
            7: 10,
            8: 5,
            9: 3,
            10: 4}

partDic ={1: "Wireless Mouse",
            2: "Wireless Keyboard",
            3: "19'' Monitor",
            4: "23'' Monitor",
            5: "HDMI Cable",
            6: "VGA Cable",
            7: "USB Cable",
            8: "Power Cable",
            9: "8GB Thumb Drive",
            10: "16GB Thumb Drive"}

archiveDic = {}

    
def main():
    userInterface()
    
def printInventory():
    for keyA, valueA in stockDic.items():  
        if keyA in partDic:
            print(str(keyA), str(valueA), partDic[keyA])

def newPart():
    CheckPlease = 1
    while CheckPlease != 0:
        skuInput = input("Please input a part number ")
        skuInput = int(skuInput)
        if skuInput in stockDic:
            print("already Exists")
        else: 
            inventoryInput = input("Please input how much of " + str(skuInput) + " do we have? ")
            partInput = input("Please input the name of the new part ")  
            inventoryInput = int(inventoryInput)
            stockDic[skuInput] = inventoryInput
            partDic[skuInput] = partInput
            CheckPlease = 0

def skuSearch():
    skuInput = input("Please enter the number of the part we are searching")
    skuInput = int(skuInput)
    if skuInput in stockDic.values():  
        print(skuInput, stockDic[skuInput], partDic[skuInput])
        inventoryChange = input("If you would like to change inventory for this product, please enter the total inventrory now... otherwise press enter: ")
        if not inventoryChange:
            print("Moving On")
            print("")
        else:
            inventoryChange = int(inventoryChange)
            stockDic[skuInput] = inventoryChange
            
def lowInventory():
    for keyA, valueA in stockDic.items():  
        if stockDic[keyA] <= 3:
            print(keyA, stockDic[keyA], partDic[keyA])

def exiting():
    sys.exit(0)

def commandList():
    print("Commands are as follows")
    print("P : Print all inventory")
    print("PA : Print archived parts")
    print("A : Add a new part")
    print("R : Print low inventory (3 units or lower)")
    print("L : Search for a specific part by SKU/ID Number")
    print("U : Archive Part")
    print("D : Delete From Archive")
    print("H : Help (this page)")
    print("Q : Quit")

def archivePart():
    print("Note, this part will be stored then deleted. Part will not be retriveable.")
    skuSearch = input("Please enter a SKU for us to archive for you? ")
    skuSearch = int(skuSearch)
    if skuSearch in partDic:
        print("Removing from List... Adding to archive...")
        archiveDic[skuSearch] = partDic[skuSearch]
        del stockDic[skuSearch]
        del partDic[skuSearch]
        print(stockDic)
        print(partDic)
        print(archiveDic)
    else:
        print("Part not found, try again later")

#delete part from archive. To Free Space up
def deleteFA():
    print("Note, deleting this part will make it unsearchable forever.")
    skuSearch = input("Please input the SKU that will be deleted")
    skuSearch = int(skuSearch)
    if skuSearch in archiveDic:
        print("Deleting forever...")
        del archiveDic[skuSearch]
    else:
        print("Part not found, please try again")

def printArchive():
    for key, value in archiveDic.items():
        print(key, value)
    
def userInterface():
    #Perma Loop Still Quit Statement is execuated
    command = "a"
    while command != "ProgramNull":
        userInput = input("Please enter a command or type H for help ")
        userInput = userInput.upper()
        commandDic = {"P": printInventory,
                      "PA": printArchive,
                      "A": newPart,
                      "L": skuSearch,
                      "R": lowInventory,
                      "Q": exiting,
                      "U": archivePart,
                      "D": deleteFA,
                      "H": commandList}
        #this with the upper block allows user to execute commands from a dictonary
        if userInput in commandDic:
            commandDic[userInput]()
        else:
            print("Sorry this is not a supported command try using the H command for more help ")
            
main()
