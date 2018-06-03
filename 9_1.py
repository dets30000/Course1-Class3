name=input("Enter file: ")
if len(name)<1: name="mbox-short.txt"
handle=open(name)
email=dict()


for line in handle:
    if not line.startswith("From ") : continue
    words=line.split()
    for word in words:
        if word!=words[1]: continue
        email[word]= email.get(word,0)+1


largest=0
topword=None


for k,v in email.items():
    if v>largest:
        largest=v
        topword=k
print(topword,largest)
