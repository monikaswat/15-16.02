import tkinter as tk

root = tk.Tk()
root.attributes('-topmost', 1)
root.geometry('600x400+1200+80')
root.title('moj program')

label = tk.Label(root, text='Siema', font=('Arial', 20),
                 background='#265ECE', fg='red')
label.pack(padx=2, pady=20)
textbox = tk.Text(root, height=3, font=('Arial', 14))
textbox.pack(padx=10, pady=20)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0)
buttonframe.columnconfigure(1)
buttonframe.columnconfigure(2)

btn1 = tk.Button(buttonframe, text='1', font=('Arial', 15))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E, pady=10, padx=10)
btn2 = tk.Button(buttonframe, text='2', font=('Arial', 15))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E, pady=10, padx=10)
btn3 = tk.Button(buttonframe, text='3', font=('Arial', 15))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E, pady=10, padx=10)
btn4 = tk.Button(buttonframe, text='4', font=('Arial', 15))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E, pady=10, padx=10)
btn5 = tk.Button(buttonframe, text='5', font=('Arial', 15))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E, pady=10, padx=10)
btn6 = tk.Button(buttonframe, text='6', font=('Arial', 15))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E, pady=10, padx=10)

buttonframe.pack(fill='x')

quit_btn = tk.Button(root, text='Wyjdz', command=root.quit, bg='red')
quit_btn.place(x=200, y=250, height=100, width=100)
root.mainloop()