import customtkinter as tk

oot=tk.CTk(fg_color='#40665F')
oot.title("Student Panel")
oot.resizable(False,False)
oot.geometry("700x400")

frame = tk.CTkFrame(master=oot,width=200,corner_radius=20,fg_color='#5C867E')
frame.pack(side='left',pady=12, padx=10, fill="both",)

inframe= tk.CTkFrame(master=frame,width=200,corner_radius=20,fg_color='#40665F')
inframe.pack(side='top',pady=10, padx=10, fill="both",)
inframe1= tk.CTkFrame(master=frame,width=200,corner_radius=20,fg_color='#40665F')
inframe1.pack(side='bottom',pady=10, padx=10, fill="both",)
#----------------------------------------------------------------
frame1 = tk.CTkFrame(master=oot,corner_radius=20,fg_color='#5C867E')
frame1.pack(side='right',pady=12, padx=10, fill="both", expand=True)
def page1():
    try:
        fra2.destroy()
        fra3.destroy()
    except:
        pass
    fra1= tk.CTkFrame(master=frame1,width=200,corner_radius=20,fg_color='#40665F')
    fra1.pack(side='top',pady=10, padx=10, fill="both",)
def page2():
    try:
        fra1.destroy()
        fra3.destroy()
    except:
        pass
    fra2= tk.CTkFrame(master=frame1,width=200,corner_radius=20,fg_color='#40665F')
    fra2.pack(side='top',pady=10, padx=10, fill="both",)
def page3():
    try:
        fra2.destroy()
        fra1.destroy()
    except:
        pass
    fra3= tk.CTkFrame(master=frame1,width=200,corner_radius=20,fg_color='#40665F')
    fra3.pack(side='top',pady=10, padx=10, fill="both",)
#----------------------------------------------------------------
label1 = tk.CTkLabel(master=inframe,fg_color='#5C867E',text_color="white", corner_radius=20, font=("Hebrew", 20,"bold"),text="FOM",height=50, width=100)2
label1.pack(pady=12, padx=10)

button1=tk.CTkButton(master=inframe1,command=page1,fg_color='#5C867E',hover_color='#C24641', corner_radius=20, font=("Hebrew", 20,"bold"),text="Create",height=50, width=150)
button1.pack(pady=16, padx=10)

button2=tk.CTkButton(master=inframe1,command=page2,fg_color='#5C867E',hover_color='#C24641', corner_radius=20, font=("Hebrew", 20,"bold"),text="Delete",height=50, width=150)
button2.pack(pady=16, padx=10)

button4=tk.CTkButton(master=inframe1,command=page3,fg_color='#5C867E',hover_color='#C24641', corner_radius=20, font=("Hebrew", 20,"bold"),text="Access",height=50, width=150)
button4.pack(pady=16, padx=10)



oot.mainloop()