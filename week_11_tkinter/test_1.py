# # # import tkinter as tk #1

# # # #root=tk.Tk() #2
# # # #root.title("Thu_Huyen")
# # # #root.geometry("400x600")

# # # #label=tk.Label(root,text="Hello") #3
# # # #label.pack()

# # # #root.mainloop()#4

# # # # mo rong ra 

# # # root=tk.Tk()
# # # root.title("Thu_Huyen")
# # # root.geometry("300x400")
# # # root.config(background="Blue")
# # # root.resizable(False,False)

# # # label=tk.Label(root,text="Hello",fg="red",font=("Arial",22))
# # # label.pack()

# # # #nut nhan
# # # #button=tk.Button(root,text="Press here",bg="yellow",fg="blue",font=("Arial",18))
# # # #button.pack()

# # # # trong nut nhan hien thi tren terminal
# # # #def click():
# # # #    print("HCMC technology and education")
# # # #button=tk.Button(root,text="Press here",bg="yellow",fg="blue",font=("Arial",18),command=click)
# # # #button.pack()

# # # # nhan nut hen tren python
# # # #def click():
# # # #    label=tk.Label(root,text="hcmc technology and education",font=("Arial",18))
# # # #    label.pack()
# # # #button=tk.Button(root,text="Press here",bg="yellow",fg="blue",font=("Arial",16),command=click)
# # # #button.pack()

# # # # o nhap du lieu 
# # # #entry=tk.Entry(root,bg="white",fg="black",font=("Arial",16))
# # # #entry.pack()


# # # #entry=tk.Entry(root)
# # # #entry.pack()
# # # ##def in_text():
# # # #    print("Please text: ",entry.get())
# # # #btn=tk.Button(root,text="Show in terminal",command=in_text)
# # # #btn.pack()

# # # # hien dau*
# # # #entry=tk.Entry(root,bg="white",fg="black",font=("Aria",16),show="#")
# # # #entry.pack()#

# # # #def in_gui():
# # # #    label1.config(text=entry)
# # # #btn=tk.Button(root,text="Show in Gui",command=in_gui)
# # # #btn.pack()
# # # #label1=tk.Label(root,text="",font=("Arial",10))
# # # #label1.pack()



# # # #entry = tk.Entry(root, bg="white", fg="black", font=("Arial", 16), show="*")
# # # #entry.pack()

# # # #def in_text():
# # # #    user_input = entry.get()
# # # ##    print("Please text:", user_input)
# # # #    label1 = tk.Label(root, text=user_input, font=("Arial", 10))
# # # #    label1.pack()

# # # #btn = tk.Button(root, text="Show in terminal and GUI", command=in_text)
# # # #btn.pack()

# # # #text=tk.Text(root,height=5,width=30)
# # # #text.pack()

# # # def in_ra_terminal():
# # #     noi_dung = text.get("1.0", tk.END)
# # #     print("Text:")
# # #     print(noi_dung.strip())

# # # def reset_gui():
# # #     text.delete("1.0", tk.END)
# # #     label.config(text="")  # Sửa lỗi ở đây

# # # root = tk.Tk()
# # # root.title("Show text in terminal")

# # # text = tk.Text(root, height=5, width=30)
# # # text.pack()

# # # button = tk.Button(root, text="In ra terminal", command=in_ra_terminal)
# # # button.pack()

# # # btn_reset = tk.Button(root, text="Reset text in GUI", command=reset_gui)
# # # btn_reset.pack()  # Sửa lỗi tên biến: bth_reset -> btn_reset

# # # # Nếu bạn muốn có label, thêm đoạn này:
# # # label = tk.Label(root, text="Nội dung đầu ra sẽ ở đây")
# # # label.pack()

# # # #


# # # def in_ra_terminal():
# # #     noi_dung = text.get("1.0", tk.END)
# # #     print("Text:")
# # #     print(noi_dung.strip())

# # # def reset_gui():
# # #     text.delete("1.0", tk.END)

# # # root = tk.Tk()
# # # root.title("Show text in terminal")

# # # text = tk.Text(root, height=5, width=30)
# # # text.pack()

# # # button = tk.Button(root, text="In ra terminal", command=in_ra_terminal)
# # # button.pack()

# # # btn_reset = tk.Button(root, text="Reset text in GUI", command=reset_gui)
# # # btn_reset.pack()

# # # # Nếu bạn thực sự muốn dùng label để hiển thị nội dung khác, có thể để lại:
# # # # label = tk.Label(root, text="Nội dung đầu ra sẽ ở đây")
# # # # label.pack()

# # # root.mainloop()

# # # root.mainloop()

# #               # Đặt tiêu đề cho cửa sổ
# #               # Kích thước cửa sổ 300px x 400px
# # # root.config(background="Skyblue")         # Đặt màu nền là màu xanh dương
# # # root.resizable(False, False)     


# # # label = tk.Label(root, text="Hello", fg="red", font=("Arial", 22))
# # # label.pack()

# # # button = tk.Button(root, text="Press here", bg="yellow", fg="blue", font=("Arial", 18))
# # # button.pack()

# # # def click():
# # #      label=tk.Label(root,text="dfkhđshàdshh")
# # #      label.pack()

# # # button = tk.Button(root, text="Press here", bg="yellow", fg="blue", font=("Arial", 18), command=click)
# # # button.pack()
# # import tkinter as tk 

# # root=tk.Tk()
# # root.title("Thu_Huyen")
# # root.geometry("300x400") 
# # def doi_label():
# #     label.configure(text=entry.get())

# # button=tk.Button(root,text="Click",command=doi_label)
# # button.pack()

# # entry=tk.Entry(root)
# # entry.pack()

# # label=tk.Label(root,text=" ", fg="red", bg="blue", font=("Arial",18))
# # label.pack()



# # root.mainloop()





# # # root.mainloop()

# import tkinter as tk

# def in_ra():
#     noi=text.get("1.0",tk.END)
#     print("Cac")
#     print(noi.strip())

# root=tk.Tk()
# root.title("Show")

# text=tk.Text(root,height=5,width=10)
# text.pack()

# button=tk.Button(root,text="Click",command=in_ra)
# button.pack( )

# root.mainloop()

import tkinter as tk

root = tk.Tk()

# Label nằm ở hàng 0, cột 0
label1 = tk.Label(root, text="A", bg="lightblue")
label1.grid(row=0, column=0)

# Label nằm ở hàng 0, cột 1 nhưng chiếm 2 hàng (rowspan=2)
label2 = tk.Label(root, text="B", bg="lightgreen")
label2.grid(row=0, column=1, rowspan=10)

# Label nằm ở hàng 1, cột 0
label3 = tk.Label(root, text="C", bg="lightpink")
label3.grid(row=1, column=0)

root.mainloop()