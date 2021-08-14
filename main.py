# Python3 program for the above approach
from collections import Counter
import itertools

FILE = "INPUT.txt"
OUTPUT = "outPut.txt"

try:
    with open(FILE, 'r') as filehandle:
        S1 = filehandle.readline()
        S2 = filehandle.readline()
        NoS2 = len(S2)
        print(NoS2)
        print('File Found')
       
except FileNotFoundError:
    print("Failed to open file")
    S1 = []
    S2 = []
   
def check(S1, S2):
    fileOutput = open(OUTPUT, 'a') #fileOutput opens the output file
    print(S1)
    str1 = ""
    S1 = str1.join(S1)
    if(Counter(S1) == Counter(S2)):
        print("The strings are anagrams.")
        fileOutput.write("YES\n")
        fileOutput.close()
        print(S1)
        exit()
        
    else:
        fileOutput.write("NO\n")
        fileOutput.close()

def filter_char(letter):
    filterS2 = sorted(S2)
    return True if letter in filterS2 else False

filtered_char = filter(filter_char, S1)
S1 = tuple(filtered_char)
string1 = set(S1) 
string2 = set(S2)
S1 = string1 & string2
print(S1)
per = itertools.permutations(S1)

def main():
    for val in per:
        S1 = val
        S1 = S1[:NoS2]
        check(S1, S2)
        
if __name__ == "__main__":
    main()

