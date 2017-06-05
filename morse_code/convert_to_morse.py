from ConfigParser import SafeConfigParser
import string

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
    for i in xrange(0, len(targetstring)):
        print targetstring[i]
        if any(character in targetstring)

    pass


morselist = parse_ini()
#print morselist
capital_alphabet = list(string.ascii_uppercase)
lower_alphabet = list(string.ascii_lowercase)
#print capital_alphabet
#print lower_alphabet
convert_target()
