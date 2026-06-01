import csv
#create csv file and write data into it
with open("employees.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["id", "name", "salary"])
    writer.writerow([1, "prinsi", 50000])
    writer.writerow([2,"jensi",60000])


#read csv file

with open("employees.csv", "r") as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)

#csv.dictreader()
#use for the read row as a dictionary

with open("employees.csv","r") as file:
    reader=csv.DictReader(file)
    for row in reader:
        print(row)


#csv.write()
#write row into csv

with open("employees.csv","w",newline="") as file:
    writer=csv.writer(file)
    writer.writerow([3,"mitali",70000])
    print("data written successfully")


#csv.DictWriter()
#write row into csv as a dictionary

with open("employees.csv","w",newline="") as file:
    fieldnames=["id","name","salary"]
    writer=csv.DictWriter(file,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"id":4,"name":"januuuu","salary":80000})
    print("data written successfully")

#read all data
with open("employees.csv","r",newline="") as file:
    reader=csv.DictReader(file)
    for row in reader:
        print(row)

