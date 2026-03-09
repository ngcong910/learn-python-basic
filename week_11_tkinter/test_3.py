import tkinter as tk

root = tk.Tk()
root.title("GUI")
root.geometry("300x400")

tk.Label(root, text="Họ tên:").grid(row=0, column=0,rowspan=2, padx=5, pady=5)
tk.Entry(root).grid(row=0, column=0, padx=5, pady=5)

tk.Label(root, text="Tuổi:").grid(row=1, column=0, padx=5, pady=5)
tk.Entry(root).grid(row=1, column=0, padx=5, pady=5)

tk.Button(root, text="Gửi").grid(row=2, column=0, columnspan=100,rowspan=50, pady=5)

# sap xep tuyen doi 
entry=tk.Entry(root)
entry.place(width=150,height=20)

root.mainloop()
