from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from googletrans import Translator

def translate():
    lang_1 = text_entry1.get("1.0", "end-1c")
    cl = choose_language.get()
    if lang_1 == '':
        messagebox.showerror('Language Translator', 'Enter the words')
    else:
        text_entry2.delete(1.0, 'end')
        translator = Translator()
        try:
            output = translator.translate(lang_1, dest=cl)
            text_entry2.insert('end', output.text)
        except Exception as e:
            messagebox.showerror('Translation Error', f'An error occurred: {e}')

def clear():
    text_entry1.delete(1.0, 'end')
    text_entry2.delete(1.0, 'end')

root = Tk()
root.title('Language Translator')
root.geometry('590x370')

# Modern color scheme
bg_color = '#f0f0f0'
accent_color = '#007bff'
text_color = '#333333'

# Stylish background image
background_image = Image.open('b/Users/k/Documents/Pythonbasic/Online Dictionary/photo_2024-04-29 20.54.52.png')
background_image = ImageTk.PhotoImage(background_image)
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame1 = Frame(root, bg=bg_color, width=590, height=370)
frame1.place(x=0, y=0)

# Stylish title with custom font
title_font = ('Helvetica', 24, 'bold')
Label(frame1, text='Language Translator', font=title_font, fg=text_color, bg=bg_color).place(x=180, y=10)

# Language selection with custom font
l = StringVar()
choose_language = ttk.Combobox(frame1, width=27, textvariable=l, state='readonly', font=('verdana', 10, 'bold'))
choose_language['values'] = ('Uzbek', 'English')
choose_language.place(x=150, y=70)
choose_language.current(0)

# Text entry fields with custom font and border
text_entry1 = Text(frame1, width=20, height=7, borderwidth=0, bg='#E0E0E0', font=('verdana', 15))
text_entry1.place(x=20, y=110)

text_entry2 = Text(frame1, width=20, height=7, borderwidth=0, bg='#E0E0E0', font=('verdana', 15))
text_entry2.place(x=310, y=110)

# Stylish buttons with custom font and hover effect
button_font = ('verdana', 10)
btn_translate = Button(frame1, command=translate, text='Translate', relief='raised', borderwidth=2, font=button_font, bg=accent_color, fg='black')
btn_translate.place(x=180, y=290)

btn_clear = Button(frame1, command=clear, text='Clear', relief='raised', borderwidth=2, font=button_font, bg=accent_color, fg='black')
btn_clear.place(x=300, y=290)

# Hover effect for buttons
def on_enter(e):
    e.widget['background'] = '#0056b3'

def on_leave(e):
    e.widget['background'] = accent_color

btn_translate.bind('<Enter>', on_enter)
btn_translate.bind('<Leave>', on_leave)
btn_clear.bind('<Enter>', on_enter)
btn_clear.bind('<Leave>', on_leave)

root.mainloop()
