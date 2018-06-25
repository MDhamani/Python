#####################################
# MDhamani
#####################################

x = int(input("enter max no."))
showprime = input("show composite no.????")

p = 1 # 1 is composite so start from 2
prime = 0
composite = 1

while p <= x:
    i = 1
    flag = 0
    while i < p:
        if p % i == 0:
            flag += 1
        i += 1
    if flag == 1:
        print(p, "prime")
        prime += 1
    elif flag >= 1:
        composite += 1
        if showprime == "Y" or showprime == "y":
            print(p, "composite")
    p += 1
    
print("prime no.s B/W 0 -", x ,":-" , prime)
print("composite no.s B/W 0 -", x, ":-", composite)
