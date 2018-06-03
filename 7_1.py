fname=input("Enter file name: ")
fh=open(fname)
count=0
tot=0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count=count+1
    avg=float(line[20:])
    tot=tot+avg


print("Average spam confidence: ", tot/count)
