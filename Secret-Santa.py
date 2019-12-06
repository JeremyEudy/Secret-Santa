# Author: Jeremy Eudy
import sys, getopt, os
import json, csv
import random, datetime

def printHeader():
    print("###################################################")
    print("#                                                 #")
    print("#             Welcome to Secret Santa             #")
    print("#                                                 #")
    print("###################################################")
    return

def sendInfo(pairs):
    print(pairs)
    sys.exit()

def buildPairs(participants):
    pairs = {}
    options = list(participants.keys())
    now = datetime.datetime.now()
    while(True):
        if len(pairs) == len(options):
            break

        currentPerson = random.choice(options)
        tempPartner = random.choice(options)
        if currentPerson != tempPartner and currentPerson not in pairs.keys() and tempPartner not in pairs.values():
            pairs[currentPerson] = tempPartner

        if (datetime.datetime.now()-now).seconds > 3:
            return 0

    return pairs

def silent(argv):
    if len(argv) == 0:
        return
    inputFile = ''
    fileType = ''
    try:
        opts, args = getopt.getopt(argv,"ht:i:",["ifile=","ftype="])
    except getopt.GetoptError:
        print('usage: Secret-Santa.py -t <file type> -i <input file>')
        print('\tSupported file types: .json, .txt, .csv')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('usage: Secret-Santa.py -t <file type> -i <input file>')
            print('\tSupported file types: json, csv')
            sys.exit()
        elif opt in ("-t", "--ftype"):
            fileType = arg
        elif opt in ("-i", "--ifile"):
            inputFile = arg

    if inputFile:
        participants = {}
        with open(inputFile, "r") as f:
            if fileType == "json":
                participants = json.loads(f.read())
            elif fileType == "csv":
                csvReader = csv.reader(f)
                for row in csvReader:
                    participants[row[0]] = row[1]

        while(True):
            pairs = buildPairs(participants)
            if type(pairs) is dict:
                sendInfo(pairs)
            elif pairs == 0:
                pairs = buildPairs(participants)

def manual():
    printHeader()
    participants = {}
    print("Input the name of each participant (enter 'q' when done)")
    while(True):
        person = input(">")
        if person == "q":
            break
        else:
            participants[person] = "None"

    if len(participants) == 0:
        sys.exit()

    print("Input the email of each participant")
    for person in participants.keys():
        email = input("{}\n>".format(person))
        participants[person]= email

    while(True):
       pairs = buildPairs(participants)
       if type(pairs) is dict:
           sendInfo(pairs)
       elif pairs == 0:
           pairs = buildPairs(participants)

if __name__ == "__main__":
    os.system("clear")
    silent(sys.argv[1:])
    manual()
