from tkinter import *
from tkinter.messagebox import *
from pytube import YouTube

root = Tk()
root.title('Youtube video downloader')
root.geometry('600x500')

def help_ask(event):
    help_btn.config(text='HELP')
    showinfo("Help","This app is only to download youtube videos")
# downloading video
def download_video():
    global hurray
    hurray = Label(
        main_body,
        fg='#002',
        bg='#21eb21',
        font=("sans-serif",15,'bold')
    )
    try:
        yt = YouTube(f"https://www.youtube.com/watch?v={video_id_entry.get()}")
        hurray.config(text='downloading...')
        yt.streams.get_highest_resolution().download()
        hurray.config("Hurray Downloaded!!!")
    except:
        hurray.config(text='Please give a valid video id --- YouTube only')
    
# useless components
useless_body = Label(
    root,
    bg='#21eb12',
    fg='#002',
)

# setting textvariable
idofvideo = StringVar()
#  components
main_h = Label(
    root,
    text='Video downloader'.upper(),
    bg='#002',
    fg='#21eb21',
    font=("sans-serif",25,'bold')
)
main_body = Label(
    root,
    bg='#21eb12',
    fg='#002',
)
semi_head = Label(
    main_body,
    text="ONE CLICK GET ALL",
    fg='#002',
    bg='#21eb21',
    font=("sans-serif",15,'bold')
) 
help_btn = Button(
    main_h,
    text='help',
    bg='#002',
    fg='#21eb21',
    bd=0,
    activebackground='#21eb21',
    activeforeground='#002',
    font=('sans-serif',10,'bold')
)
video_id_frame = Frame(main_body,bg='#21eb21')
video_id_title = Label(
    video_id_frame,
    text="Video id ->",
    bg='#21eb21',
    fg='#002',
    font=('consolas',15,'bold')
)
video_id_entry = Entry(video_id_frame,textvariable=idofvideo,bg='#002',fg='#21eb21',font=('consolas',15,'bold'))
 
download_btn = Button(
    useless_body,
    text='DOWNLOAD',
    bg='#002',
    fg='#21eb12',
    activebackground='#21eb21',
    activeforeground='#002',
    font=('consolas',20,'bold'),
    bd=0,
    command=download_video
)


# packing the components
main_h.pack(expand=True,fill=BOTH)
help_btn.pack(side=LEFT,anchor=NW)
main_body.pack(expand=True,fill=BOTH)
semi_head.pack()
video_id_frame.pack(expand=True,fill=X)
video_id_title.pack(side=LEFT)
video_id_entry.pack(side=LEFT,expand=True,fill=X)
download_btn.pack()


# handeling events
help_btn.bind('<Button-1>',help_ask)

# packing useless components
useless_body.pack(expand=True,fill=BOTH)

root.mainloop()