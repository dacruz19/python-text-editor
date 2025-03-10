import customtkinter as ctk
from tkinter import filedialog,messagebox
import subprocess

app = ctk.CTk()
current_file=None

def callback():
    global current_file
    x = filedialog.askopenfile(mode='r')
    
    if x:
        current_file = x.name
        scrbl.delete("0.0","end")
        scrbl.insert(ctk.END,str(x.read()))
        x.close()
    
def callback2():
    global current_file
    if current_file:
        with open(current_file,"w") as file:
            file.write(str(scrbl.get("0.0","end")))
    else:
        x = filedialog.asksaveasfile()
        x.write(str(scrbl.get("0.0","end")))
        x.close()
        messagebox.Message("Saved")
    
def callback4():
    if current_file:
        output = subprocess.run(["python",current_file],text=True,capture_output=True)
        term.insert(ctk.END,f"python {current_file}"+output.stdout+"\n")
    
ctk.set_default_color_theme("dark-blue")
app.title("Super Halal Code Editor (SHCE)")
app.geometry("500x700")

title = ctk.CTkLabel(app,text="Random Text Editor",font=("Arial",35,"bold"))
title.pack(pady=2.5)

topbar = ctk.CTkFrame(app,height=35,fg_color="#363636")
topbar.pack(pady=10,fill="x")

filebutton = ctk.CTkButton(topbar,text="Open File",width=100,font=("Arial",17),command=callback)
filebutton.pack(side="left",padx=5,pady=5)

filebutton2 = ctk.CTkButton(topbar,text="Save",width=100,font=("Arial",17),command=callback2)
filebutton2.pack(side="left",padx=5,pady=5)

filebutton4 = ctk.CTkButton(topbar,text="Run",width=100,font=("Arial",17),command=callback4)
filebutton4.pack(side="left",padx=5,pady=5)

scrbl = ctk.CTkTextbox(app,height = 450,font=("Arial",17,"bold"))
scrbl.pack(pady=5,fill="x")

term = ctk.CTkTextbox(app,height=150,font=("Arial",17,"bold"))
term.pack(pady=5,fill="x")

app.mainloop()
