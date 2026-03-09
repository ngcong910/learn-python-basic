import tkinter as tk

def calculator_sum():
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        label_result.config(text=f"Kết quả: {result}")

def return_label():
        entry1.delete(0,tk.END)
        entry2.delete(0,tk.END)
        label_result.configure(text="")

root = tk.Tk()
root.title("Calculator for Sum Operation")
root.geometry("300x200")

tk.Label(root, text="Number 1").grid(row=0, column=0, padx=5, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Number 2").grid(row=1, column=0, padx=5, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)

tk.Button(root, text="Tính", command=calculator_sum).grid(row=2, column=0, columnspan=2, pady=10)

label_result = tk.Label(root, text="Kết quả:")
label_result.grid(row=3, column=0, pady=10)

reset=tk.Button(root,text="Reset",command=return_label)
reset.grid(row=4,column=0,padx=1,pady=1)


root.mainloop()
