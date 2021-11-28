from tkinter import Tk

import webbrowser

from tkinter import*

root = Tk()
root.title("Webbrowsers")
root.geometry("660x660")
root.configure(bg="Salmon")

label = Label(root,text="THIS IS MY FEVOURITE WEBSITES",font="Attika 15 bold",bg="Purple")
label.pack()

def linkedin():
    webbrowser.open("www.linkedin.com")

def facebook():
    webbrowser.open("www.facebook.com")

def youtube():
    webbrowser.open("www.youtube.com")

def twitter():
    webbrowser.open("www.twitter.com")



mylinkedin = Button(root,text="LINKEDIN",command=linkedin,font="LUCIDA 15 bold",bg="lightblue")
mylinkedin.pack(padx=20,pady=20)

myfacebook = Button(root,text="FACEBOOK",command=facebook,font="LUCIDA 15 bold",bg="blue")
myfacebook.pack(padx=20,pady=20)
myyoutube = Button(root,text="YOUTUBE",command=youtube,font="LUCIDA 15 bold",bg="red")
myyoutube.pack(padx=20,pady=20)
mytwitter = Button(root,text="TWITTER",command=twitter,font="LUCIDA 15 bold",bg="Turquoise")
mytwitter.pack(padx=20,pady=20)

mainloop()