import tkinter as tk

root = tk.Tk()
root.title('Max i Min okna')
root.geometry('600x400+1200+80')
root.minsize(300, 300)
root.maxsize(800, 500)
root.attributes('-alpha', 0.8) # nieprzezroczystosc
root.attributes('-topmost', 1) # okno zawsze na wierzchu
root.iconbitmap(file='logo.ico')
root.mainloop()