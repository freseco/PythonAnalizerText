"""
    Author: Francisco Reseco
    Date: 01/09/2018
    Description: Script to count character in a file text and find what percentage of the text each character occupies
"""

#count the number of times the character is in the text
def count_char(text,char):
    count=0
    for c in text:
        if c==char:
            count+=1
    return count


Filename= input("Introduce the file name:")

with open(Filename)as f:
    text=f.read()

longtext=len(text)

for char in "abcdefghijklmnñopqrtuvwyz1234567890,.?¿":
    perc=100*count_char(text,char)/longtext
    print("Character:{0} -> {1}%".format(char,round(perc,2)))



