import tkinter
from pytube import YouTube

root = tkinter.Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("manish's youtube video downloader")


tkinter.Label(root, text ='Youtube Video Downloader',bg='red', font ='arial 20 bold').pack()




##enter link
link = tkinter.StringVar()

tkinter.Label(root, text ='Paste Link Here:',bg='orange', font ='Georgia 18 bold').place(x= 140, y = 60)
link_enter = tkinter.Entry(root, width = 70, textvariable = link).place(x = 32, y = 100)



#function to download video


def Downloader():
     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    tkinter.Label(root, text =' video DOWNLOADED', bg='blue',font ='arial 15').place(x= 160, y = 210)


tkinter.Button(root, text ='DOWNLOAD', font ='arial 15 bold', bg ='green', padx = 2, command = Downloader).place(x=180, y = 150)



root.mainloop()
