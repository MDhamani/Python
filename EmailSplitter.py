#####################################
# MDhamani
#####################################
x = input("enter email\n")
user=""
org=""


try:
    user, org = x.split("@")

    if (org.strip() == "" or user.rstrip()== ""):
        exit(0)

except:
    print("enter a valid email " + x.strip())
    exit(0)

print("Registered to:-"+user)
print("organization:-"+org)
