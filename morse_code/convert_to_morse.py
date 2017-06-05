from ConfigParser import SafeConfigParser
import string
import os

target = 'target.txt'


def parse_ini():
    parser = SafeConfigParser()
    parser.read('conversion.ini')
    morselist = list(string.ascii_uppercase)
    number = 0
    for i in morselist:
        i = parser.get('CONVERSIONS', i)
        morselist[number] = i
        number += 1
    return morselist

def convert_target():
    with open(target, "r") as targetfile:
        targetstring = targetfile.read()
        templist = list()
    for i in xrange(0, len(targetstring)):
        #print targetstring[i]
        templist.append(targetstring[i])
    outputfile = open('output.txt', "a")
    for i in templist:
        try:
            a = combined_alphabet.index(i)
        except ValueError:
            outputfile.write(" ")
        outputfile.write(combined_morse[a])

    '''for x in templist:
        tempvar0 = 0
        tempvar1 = 0
        for z in capital_alphabet:
            if templist[x] == capital_alphabet[tempvar1]:
                tempvar0 += 1
                outputfile.write(morselist[tempvar0])
            else:
                tempvar1 += 1
                pass
        tempvar0 = 0
        tempvar1 = 0
        for y in lower_alphabet:
            if templist[x] == lower_alphabet[y]:
                outputfile.write(morselist[tempvar0])
            else:
                tempvar1 += 1
                pass
        if templist[x] == ' ':
            outputfile.write(' ')
        else:
            pass'''



morselist = parse_ini()
#print morselist
capital_alphabet = list(string.ascii_uppercase)
lower_alphabet = list(string.ascii_lowercase)
combined_alphabet = capital_alphabet + lower_alphabet
combined_morse = morselist + morselist


#print capital_alphabet
#print lower_alphabet
print combined_alphabet
print combined_morse
a = combined_alphabet.index('a')
print a
convert_target()