


# data=openfile.read()
# openfile.close()
# openfile=open("text.txt","r")
# data2=openfile.readlines()
ls=["Steve", "Vonetta","Susan","Precious","John","Brian","Albright"]


with open("text.txt","a") as wrt:
  for i in ls:
    wrt.write(i)
    wrt.write("\n")
opn=open("text.txt","r")

print(opn.read())
