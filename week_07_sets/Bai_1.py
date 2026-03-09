with open("text.txt","w",encoding="utf-8") as file: # ghi vào file text
    text_1=input("Nhập nội dung vào file text: ")
    file.write(text_1) # ghi vào file 
    print("File của bạn đã được ghi vào")

with open("text.txt","r",encoding="utf-8") as file: # đọc file
    text_2=((file.read().split())) # loại các từ trùng lập và tách từng từ ra 
seen_one=set() # từ xuất hiện một lần
seen_multiple=set() # từ xuất hiện nhiều lần 
for word in text_2:
    if word in seen_one:
        seen_one.remove(word) # nếu từ này xuất hiện thì xóa
        seen_multiple.add(word) # và cho thêm vào multiplle
    else:
        seen_one.add(word)

print(word)

with open("output.txt","w",encoding="utf-8") as file: # ghi vào file 
    file.write("\n".join(seen_one)) # vì set nên dùng join
    print("File của bạn đã ghi vào file output.")