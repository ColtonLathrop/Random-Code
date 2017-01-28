import os
#compare tool to find delta between two directories
#two diretories are required - working and test
#the working directory will be taking from a working store with similar settings
#a similar store can be found via bigfix exploration and filters

testList = 0
workingList = 0
resultsTxt = 0
cwd = os.getcwd()
cwdTest = os.getcwd() + '/test'
cwdWorking = os.getcwd() + '/working'
iniTest = 0
iniWorking = 0
yy = 0
temp = 0
outputList = 0

def resultTxt():
    global resultsTxt
    os.remove('results.txt')
    resultsTxt = open('results.txt', 'a')
    return
    #createresults() if results.txt doesnt exist
    #clears results.txt
    #openresults()


def dirList():
    global testList
    global workingList
    testList = [a for a in os.listdir(cwdTest) if a.endswith('.ini')]
    workingList = [a for a in os.listdir(cwdWorking) if a.endswith('.ini')]
    #open test directory and create list of files
    #open working directory and create list of files
    #print workingList
    #print testList
    

def gLists(testInput,workingInput):
    global resultsTxt
    global iniTest
    global iniWorking
    os.chdir(cwdTest)
    iniTest = open(testInput).readlines()
    os.chdir(cwdWorking)
    iniWorking = open(workingInput).readlines()
    resultsTxt.write(testInput + '\n')
    #resets prior lists
    #create lists of both files line by line
    #two inputs working files and test files
    #writes the test ini to the doc
    return

def compare(list1, list2):
    global outputList
    outputList = []
    list3 = list1 + list2
    for i in range(0, len(list3)):
        if ((list3[i] not in list1) or (list3[i] not in list2)) and (list3[i] not in outputList):
             outputList[len(outputList):] = [list3[i]]
    for h in outputList:
        print 'success1'
        resultsTxt.write("%s\n" % outputList)
    #yy = set(compWorking)
    #temp = [x for x in compTest if x not in yy]
    #compare lists line by lines
    #writing any differences to results.txt separated by ::::
    return

resultTxt()
dirList()
totalIni = len(testList)
startIni = 0
curIni = 0
for x in range(startIni, totalIni):
    gLists(testList[curIni], workingList[curIni])
    curIni += 1
    compare(iniTest, iniWorking)
    
    
    
    
    
    
