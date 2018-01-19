#####################################
# MDhamani
#####################################
x = input("enter email\n")
f=""
f2=""

try:
    f, f2 = x.split("@")
    if (f2 == ""):
        exit(0)

except:
    print("enter a valid email " + x)
    exit(0)

print("Registered to:-"+f)
print("organization:-"+f2)
