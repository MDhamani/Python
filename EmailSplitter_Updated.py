#####################################
# MDhamani
#####################################

import string

x = input("enter email:\n -> ")
user = ""
org = ""

spc = 0
spc = x.find(" ")

dot = 0
dot = x.find(".")

illegalchars = string.punctuation.replace("@","")
illegalchars = illegalchars.replace('.',"")
illegalchars = illegalchars.replace("_","")

count = 0
for symbol in x:
    if symbol in illegalchars:
        count += 1
        print("Remove "+symbol+" from ur email and")

doterr = x.__len__()
count2 = 0
if x[doterr-1] == ".":
    count2 += 1

try:

  user,org = x.split("@")
  if org.strip() == "" or user.rstrip() == "" or spc >= 1 or dot <= 0 or count != 0 or count2 > 0:
        exit(0)

except:
    print("enter a valid email " + x.strip())
    exit(0)

print("Registered to:-"+user)
print("organization:-"+org)