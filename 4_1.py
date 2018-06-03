
#Chapter 4
def computepay(h,r):
    if h <=40:
        wage=h*r

    else:
        wage=40*r+(h-40)*1.5*r

    return(wage)

hrs = input("Enter Hours:")
h = float(hrs)
hourlyrate=input("Enter rate per hour:")
r=float(hourlyrate)

p=computepay(h,r)
print(p)
