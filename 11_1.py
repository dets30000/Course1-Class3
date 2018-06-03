import re

name=input("Enter file: ")

if len(name)<1: name="regex_sum_99190.txt"

handle=open(name)

 

numbers=list()

numint=list()

 

for line in handle:

    line=line.rstrip()

    numbers=re.findall('[0-9]+',line)

    if len(numbers) < 1: continue

    numbers = [int(x) for x in numbers]

    for i in numbers:

        numint.append(i)

 

print(sum(numint))

 
