#write file
with open("data.txt","w") as file:
    file.write("hello,my name is prinsi")
#append file
with open ("data.txt","a") as file:
    file.write("\n i am from surat")
#read file
with open ("data.txt","r") as file:
    content=file.read()
    print(content)