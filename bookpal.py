import tkinter as tk
from tkinter import font
import regex
import time

#function that prints messages on the screen
def send_message(event=None): 
    message = input_field.get()
    if message:
        input_field.delete(0, tk.END)
        display_message("You: ", message)                      #displays the message the user typed
        display_message("BookPal: ", regex.chatbot(message))  #displays the computer generated response based on pattern matching by the chatbot

#function that specifies the message format
def display_message(sender, message):
    messages_text.config(state=tk.NORMAL)
    messages_text.insert(tk.END, f"{sender}{message}\n\n")
    messages_text.config(state=tk.DISABLED)
    messages_text.see(tk.END)


#main window
root = tk.Tk()
root.title("BookPal")

#message frame creation (has a text widget and a scrollbar to scroll through the chat history)
chat_frame = tk.Frame(root)
chat_frame.pack(fill=tk.BOTH, expand=True)

messages_text = tk.Text(chat_frame, wrap=tk.WORD)
messages_text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
messages_text.config(state=tk.DISABLED)

scrollbar = tk.Scrollbar(chat_frame, command=messages_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
messages_text.config(yscrollcommand=scrollbar.set)

#input frame creation (has an input field and a send button)
input_frame = tk.Frame(root)
input_frame.pack(fill=tk.X)

input_field = tk.Entry(input_frame)
input_field.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
input_field.bind("<Return>", send_message)

send_button = tk.Button(input_frame, text="Send", command=send_message)
send_button.pack(side=tk.RIGHT)

input_field.focus()     #to enable user to write without having to click in the imput field

display_message("", "BookPal is a chatbot written in Python, created by Konstantinos Vrazalis (ics22115) for the course \"Computation Theory\" at the University of Macedonia.\n\nThis chatbot uses regular expressions to understand user input about various books and provide the corresponding details. It can provide info about a book's title and author, publish date and publisher, written language, online purchase link and also give a short description.\n\nBookPal uses Google's Book API to draw information about almost every book published online, based on the user's title prompt.\n")    #display introductory message

root.mainloop()         #start the window loop
