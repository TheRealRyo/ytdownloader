from pytube import YouTube
import tkinter
from tkinter import filedialog
import pdb
import os
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

dir = ""
app = customtkinter.CTk()
app.geometry("720x480")
app.title("sum")


def openfile():
    global dir
    
    dir = filedialog.askdirectory()
    path.configure(text=dir)
    

def on_progress(stream, chunk, bytes_remaining):
   total_size = stream.filesize
   bytes_downloaded = total_size - bytes_remaining
   percentage = bytes_downloaded / total_size * 100
   per= str(int(percentage))
   pp.configure(text=per + '%')
   pp.update()

   pb.set(float(percentage) / 100)
   
def startDownload():
    try:
       
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        global resolutions
        
        resolutions = [stream.resolution for stream in ytObject.streams.filter(progressive=True)]
        
        
        # Display the selected resolution
        selected_resolution = optionmenu_var.get()
        
        selected_stream = ytObject.streams.filter(progressive=True, resolution=selected_resolution).first()
        
        # Download the selected stream
        global dir
        if dir == "<built-in function dir>":
            dir=""
        
        selected_stream.download(dir)
        label.configure(text=ytObject.title)
        msg.configure(text="download compeleted!")
        
        
        



        
     
        
    except Exception as e:

        if link.get()== "":
            msgerr.configure(text="please enter a link" , text_color="red")
        elif resolutions== "" :
            msgerr.configure(text="link not valid" , text_color="red")
        else :
            msgerr.configure(text="Failed to download: " + str(e) + "             these are the supported resulotions"   + str(resolutions)  , text_color="red")
            


          
          
         

#frame 1        
frame1 = customtkinter.CTkFrame(app,bg_color="#242424",fg_color="#242424")
frame1.pack(ipady=20, ipadx=20 )
frame1.rowconfigure((0,1), weight=1)
frame1.columnconfigure((0,1), weight=1)
label = customtkinter.CTkLabel(frame1, text="put it here")
label.grid(row=0,column=0,columnspan=2)
input = tkinter.StringVar()
link = customtkinter.CTkEntry(frame1, width=540 , height=28, textvariable=input)
link.grid(row=1,column=0)
button2 = customtkinter.CTkButton(frame1, text="...", command=openfile, width= 10,height=28 )
button2.grid(row=1,column=1,padx=8)

#frame 2        
frame2 = customtkinter.CTkFrame(app,bg_color="#242424",fg_color="#242424")
frame2.place(x=0,y=160, relwidth=1)
msg = customtkinter.CTkLabel(app, text="")
msg.pack(padx=10, pady=10)
path = customtkinter.CTkLabel(frame2, text=os.getcwd())
path.pack(padx=10,pady=10)
msgerr = customtkinter.CTkLabel(frame2, text="")
msgerr.pack(padx=10,pady=10)


pp = customtkinter.CTkLabel(frame2, text="0%")
pp.pack(padx=10,pady=10)
pb = customtkinter.CTkProgressBar(frame2, width=240)
pb.set(0)
pb.pack(padx=10,pady=10)

optionmenu_var = customtkinter.StringVar(value="360p")  # set initial value
select = customtkinter.CTkOptionMenu(frame2,values=["360p", "480p","720p"], variable=optionmenu_var)
select.pack(padx=10,pady=10)

button = customtkinter.CTkButton(frame2, text="download", command=startDownload)
button.pack(padx=10,pady=10)
app.mainloop()