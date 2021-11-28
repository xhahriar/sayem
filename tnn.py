import webbrowser

from tkinter import *


root = Tk()
root.title("WebBrowsers")
root.geometry("660x660")

pnd = PanedWindow (root,bg="yellow")
pnd.pack(fill=BOTH,expand=1)
TOP = Label(pnd,text="TOPP LAVEL",font="Attika 20 bold")
pnd.add(TOP)
pnd_2=PanedWindow(pnd,orient='vertical')
pnd.add(pnd_2)

def linkedin():
    webbrowser.open("www.linkedin.com")
def facebook():
    webbrowser.open("www.facebook.com")
def twitter():
    webbrowser.open("www.twitter.com")
def youtube():
    webbrowser.open("www.youtube.com")
def whatsappweb():
    webbrowser.open("www.whatsappweb.com")
def instagram():
    webbrowser.open("www.instagram.com")
def gmail():
    webbrowser.open("www.gmail.com")

top=Label(root, text="WELCOME TO MY FAVOURITE \nWEBSITES", font="Helvtica 25 bold").pack()
top_back=Label(root,text="Click on the buttons to open website",font="LUCIDA").pack()

mylinkedin = Button(root,text="LINKEDIN", command=linkedin,font="LUCIDA 15 bold")
mylinkedin.pack(padx=20,pady=20)

myfacebook = Button(root, text="FACEBOOK", command=facebook,font="LUCIDA 15 bold")
myfacebook.pack(padx=20,pady=20)

mytwitter = Button(root, text="TWITTER", command=twitter,font="LUCIDA 15 bold")
mytwitter.pack(padx=20,pady=20)

myyoutube = Button(root, text="YOUTUBE", command=youtube,font="LUCIDA 15 bold")
myyoutube.pack(padx=20,pady=20)

mywhatsapp = Button(root, text="WHATSAPP WEB", command=whatsappweb,font="LUCIDA 15 bold")
mywhatsapp.pack(padx=20,pady=20)

myinstagram = Button(root, text="INSTAGRAM", command=instagram,font="LUCIDA 15 bold")
myinstagram.pack(padx=20,pady=20)

mygmail= Button(root, text="GMAIL" , command=gmail,font="LUCIDA 15 bold")
mygmail.pack(padx=20,pady=20)

root.mainloop()