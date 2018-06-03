import re
name=input("Enter file: ")
if len(name)<1: name="regex_sum_42.txt"
handle=open(name)

numbers=list()
y=list()

for line in handle:
    line=line.rstrip()
    numbers=re.findall('[0-9+]',line)
    
