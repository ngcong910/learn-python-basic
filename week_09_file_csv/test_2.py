import csv
fields=["Name","Age","Score"]
rows=[{"Name":"Ngoc Cong","Age":18,"Score":9},
      {"Name":"Tai","Age":8,"Score":11}]

with open("output.csv",mode="w",newline="",encoding="utf-8")as file:
    writer=csv.DictWriter(file,fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

##with open("output.csv",mode="r",encoding="utf-8")as file:
##    reader=csv.DictReader(file)
#    for a in reader:
#        print(a["Name"],a["Age"],a["Score"])

# duyet qua tung gia tri 
#with open("output.csv",mode="r",encoding="utf-8")as file:
#    reader=csv.reader(file)
#    for row in reader:
#       for value in row: 
#            print(value)
#with open("output.csv",mode="r",encoding="utf-8") as file:
  ##  reader=csv.DictReader(file)
   # count=0
   # for row in reader:
   #     count+=1
   #     if count==1:
   #         for key,value in row.items():
   #             if key=="Age":
   #                 print(f"{key}:{value}")

# truy cap hang
#with open("output.csv",mode="r",encoding="utf-8")as file:
#    reader=csv.reader(file)
#    header=next(reader)
#    rows=list(reader)
#    print("Line2:",rows[1])

# truy cap cot
#with open("output.csv",mode="r",encoding="utf-8") as file:
#    reader=csv.reader(file)
#    header=next(reader)
#    for row in reader:
#        print("Colums:",row[1])

#with open("output.csv",mode="r",encoding="utf-8")as file:
#    reader=csv.DictReader(file)
#    for row in reader:
#        if row["Name"]=="Ngoc Cong":
#            print("Age of Ngoc Cong is:",row["Age"])

#chuyen gia tri cua hang trong file thanh list
with open("output.csv",mode="r",encoding="utf-8")as file:
    reader=csv.DictReader(file)
    data=[row for row in reader]
    print(data)

#copy file csv nay sang fie csv khac
with open("output.csv",mode="r",encoding="utf-8")as infile:
    reader=csv.reader(infile)
    with open("data_copy.csv",mode="w",newline="",encoding="utf-8")as outfile:
        writer=csv.writer(outfile)
        for row in reader:
            writer.writerow(row)
print("Done")

# đếm số dòng
with open("output.csv","r",encoding="utf-8")as file:

