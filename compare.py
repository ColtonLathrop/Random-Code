#compare tool to find delta between two directories
#two diretories are required - working and test
#the working directory will be taking from a working store with similar settings
#a similar store can be found via bigfix exploration and filters

testdir = 'test'
workingdir = 'working'
testlist = []
workinglist = []


#open matching first file reading line by line creating list
#open matching second file line by line creating list
#write file to results that you are comparing
#results compare list writing lines from test on left side working on right side separated by ::::
#once loop is done closes results.txt saves it

def results():
    #createresults() if results.txt doesnt exist
    #clears results.txt
    #openresults()

def dirlist():
    #open test directory and create list of files
    #open working directory and create list of files

def getlists(a,b):
    #resets prior lists
    #create lists of both files line by line
    #two inputs a being test b being working with same name

def compare(c,d):
    #starts by writing the common file name on the doc
    #c being test d being working
    #compare lists line by lines
    #writing any differences to results.txt separated by ::::
