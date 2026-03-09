import tkinter as tk 

root=tk.Tk()
root.title("Layout voi pack()")
label1=tk.Label(root,text="Label 1",bg="lightblue")
label1.pack(fill="both",padx=10,pady=5,expand=True)
label2=tk.Label(root,text="Label 2",bg="lightgreen")
label2.pack(fill="x",padx=10,pady=5,expand=False)

button=tk.Button(root,text="Bam vo dat")
button.pack(pady=10)

root.mainloop()