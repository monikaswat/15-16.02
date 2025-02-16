import tkinter as tk
from tkinter.messagebox import showinfo
# import customtkinter as ctk
def clicked_entry():
    msg = f'Wpisales: {entry_text.get()}'
    showinfo(title='Info', message=msg)
    print('Kliknieto')
    print(f'Wpisano {entry_text.get()}')

def clicked_text():
    # Pobiera tekst od poczatku ("1.0") do konca (tk.END)
    content = text_field.get('1.0', tk.END)
    showinfo(title='Pole tekstowe TEXT', message=content)

root = tk.Tk()
entry_text = tk.StringVar()

frame = tk.Frame()
frame.pack(padx=50, pady=50)
label = tk.Label(frame, text='Wpisz cos')
label.pack()
entry = tk.Entry(frame, textvariable=entry_text, font=('Helvetica', 20))
entry.pack(ipadx=100, ipady=30)
text_field = tk.Text(frame, height=3, width=40)
text_field.pack()
button1 = tk.Button(frame, text='Entry', command=clicked_entry)
button1.pack(fill='x', ipady=5, pady=5)
button2 = tk.Button(frame, text='Text', command=clicked_text)
button2.pack()

root.mainloop()