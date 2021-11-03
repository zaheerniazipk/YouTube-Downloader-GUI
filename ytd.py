"""        
            Project:  YouTube Downloader - GUI   
"""

# pip install pytube
from ssl import OP_NO_TICKET
from tkinter import *               # GUI Library
from tkinter import ttk             # Themed widget
from tkinter import filedialog      # open file dialog
from tkinter import font            # Text Font
from pytube import YouTube          # video downloading Library

# Python Code
folder_name = ""


# File Location
def openLocation():
    global folder_name
    folder_name = filedialog.askdirectory()

    if (len(folder_name) > 1):
        locationError.config(text=folder_name, fg='green')
    else:
        locationError.config(text="Please Choose a Folder!", fg='red')


# Downloading Video
def downloadVideo():
    choice = ytdChoices.get()
    url = ytdEntry.get()

    if (len(url) > 1):
        ytd_errorMsg.config(text="")
        yt = YouTube(url)

        if (choice == choices[0]):
            select = yt.streams.filter(progressive=True, res='720p').first()
        elif (choice == choices[1]):
            select = yt.streams.filter(
                progressive=True, file_extension='mp4').first()
        elif (choice == choices[2]):
            select = yt.streams.filter(
                only_audio=True,).first()
        elif (choice == choices[3]):
            select = yt.streams.filter(adaptive=TRUE).first()
        else:
            ytd_errorMsg.config(text="Please, Paste Link Again!", fg='red')

    # Download Function
    select.download(folder_name)
    ytd_errorMsg.config(text=" File Downloaded Successfully!")


""" Basic Tkinter Code Setup"""
# To Display the root window & manages the components of tkinter app
root = Tk()
# To provide a name of the window/App
root.title("YouTube Downloader")
# To decides the size, position of the screen layout
root.geometry('500x460')
root.resizable(0, 0)
# To set all the content in center (Grid Geometry Manager)
root.columnconfigure(0, weight=1)


# Add a Space between Widgets
whiteSpace = Label(root, pady=1)
whiteSpace.grid()

""" YouTube Video Link Label """
ytd_label = Label(root, text="Paste Video URL Here!", font=('Lato', 15))
# It puts the widgets in a 2-dimensional table/box.
ytd_label.grid()
''' EntryBox where pasting the URL'''
# Tkinter StringVar helps to manage the value of a Label or Entry
ytd_entryVar = StringVar()
# Entry widget used to provde single line text-box to accept a value from the user
ytdEntry = Entry(root, width=50, textvariable=ytd_entryVar)
ytdEntry.grid()


# Add a Space between Widgets
whiteSpace = Label(root, pady=1)
whiteSpace.grid()

""" Choosing the Download Path """
''' Save File Label '''
save_label = Label(root, text="Download Path", font=('Lato', 15, 'bold'))
save_label.grid()

whiteSpace = Label(root, pady=0.1)
whiteSpace.grid()

''' Button for Choosing Download Path '''
download_path = Button(root, width=15, bg='red',
                       fg='white', text="Choose Path", padx=1, pady=1, command=openLocation)
download_path.grid()

''' Show Error Message, if Wrong Path entered '''
locationError = Label(root, text="Please, Choose a Valid Path",
                      fg='red', font=('lato', 10))
locationError.grid()

# Add a Space between Widgets
whiteSpace = Label(root, pady=1)
whiteSpace.grid()


""" Choosing the Download Quality """
''' Download Quality'''
ytdQuality = Label(root, text="Select Quality", font=('Lato', 15))
ytdQuality.grid()
''' ComboBox '''
choices = ["Higher Quality", "Lower Quality",
           "Only Audio", "Only Video"]
ytdChoices = ttk.Combobox(root, values=choices)
ytdChoices.grid()

# Add a Space
whiteSpace = Label(root, pady=10)
whiteSpace.grid()


""" Download Button """
downloadBtn = Button(root, text='Download', bg='orange', fg='white',
                     font="Verdana 14 bold", command=downloadVideo, pady=2)
downloadBtn.grid()

# Add a Space between Widgets
whiteSpace = Label(root, pady=1, bg='#F0F0F0')
whiteSpace.grid()

''' Show Error Message, if Wrong input '''
ytd_errorMsg = Label(
    root, text="Click Download & Wait for sometime!", fg='green', font=('Lato', 10))
ytd_errorMsg.grid()


""" Developer Label """
developerLabel = Label(root, text="Developed & Designed by InfoZist Solutions",
                       font=('lato', 9), pady=40)
developerLabel.grid()

# mainloop() method tells Python to run the Tkinter event loop
root.mainloop()
