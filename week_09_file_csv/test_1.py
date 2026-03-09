#data1 ="Name,Age,Score"
#data2= "Ngoc Cong,18,90"
#data3= "Tai,8,10"

#with open("output.csv",mode="w",newline='',encoding='utf-8') as file:
#    writer=file.write(data1)
#    file.write("\n")
#    file.write(data2)
#    file.write("\n")
#   file.write(data3)
    
import csv
data=[["Name","Age","Score"],
      ["Ngoc Cong",19,16],
      ["Tai",9,10]]

with open("output.csv",mode="w",newline="",encoding="utf-8") as file:
    writer=csv.writer(file)
    writer.writerows(data)
#data_1=["Cong",9,100]

#with open("output.csv",mode="a",newline="",encoding="utf-8") as file: # newline: xoa bo dong trong
#    writer=csv.writer(file)
#    writer.writerows(data_1)

#with open("output.csv",mode="r",encoding="utf-8") as file:
    #reader=file.read()
    #print(reader)

with open("output.csv",mode="r",encoding="utf-8") as file:
    reader=csv.reader(file)
    for a in reader:
        print(a)