with open("text.txt","w",encoding="utf-8") as file: # ghi vào file text
    text_1=input("Nhập nội dung vào file text: ")
    file.write(text_1) # ghi vào file 
    print("File của bạn đã được ghi vào")

with open("text.txt","r",encoding="utf-8") as file: # đọc file
    text_2=set((file.read().split())) # loại các từ trùng lập và tách từng từ ra 
    print(f"Các từ sau khi lọc trùng lập là: {text_2}")

with open("output.txt","w",encoding="utf-8") as file: # ghi vào file 
    file.write("\n".join(text_2)) # vì set nên dùng join
    print("File của bạn đã ghi vào file output.")
