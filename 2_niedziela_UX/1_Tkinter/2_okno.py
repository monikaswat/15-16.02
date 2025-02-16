import tkinter as tk

root = tk.Tk()
root.title('Tkinter')

root.geometry('600x400+1912+920')


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print(screen_width, screen_height)

message1 = tk.Label(root, text='Witamy we Wroclawiu')
message1.pack()

message2 = tk.Label(root, text='')
message2.pack()

message3 = tk.Label(root, text='...')
message3.pack()

root.mainloop()