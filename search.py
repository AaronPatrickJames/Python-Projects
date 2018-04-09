#Search Program Search.py by Aaron James
import os
import sys
import argparse
import glob

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("match", help="entry to search")
    parser.add_argument("--case", help="add any second argument to take away case sensetivity")
    args = parser.parse_args()

def main():
        fileSearch()

def fileSearch():
    filesInDir = []
    dirInDir = []
    currentdir = os.getcwd()
    os.chdir(currentdir)
    for file in glob.glob("*" + args.match + "*"):
        if os.path.isfile(file) == True:
            filesInDir.append(file)
        else:
            dirInDir.append(file)
    if args.case is None:
        place = len(filesInDir)
        while place != 0:
            place = place - 1
            originalString = filesInDir[place]
            testString = filesInDir[place]
            if testString.find(args.match):
                print("")
            else:
                filesInDir.remove(originalString)
                
        place = len(dirInDir)
        while place != 0:
            place = place - 1
            originalString = dirInDir[place]
            testString = dirInDir[place]
            testString = testString.replace(args.match, args.match)
            print(originalString + " " + testString)
            if originalString != testString:
                dirInDir.pop(place)
            
    print("")
    print("These are the files")
    for value in filesInDir:
        print(value)
    print("")
    print("These are the Dirs")
    for value in dirInDir:
        print(value)

main()
