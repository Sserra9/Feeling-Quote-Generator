from tkinter import * 
import tkinter as tk


root = Tk()
root.geometry("800x600")
root.resizable(height = 0, width = 0)

e = Entry(root, width = 75, fg = "black", bg = "white", font=("Arial",12))
e.grid(row=22, column=2, columnspan=4, padx=25, pady=10)
e.insert(0, "Type to get some inspiration: ")

text1 = tk.Label(text='Want a quote to match how you are feeling or how you want to feel?', font=("Arial",18))
text1.grid(row=10, column=2, padx=25, pady=10)


text2 = tk.Label(text='Type a feeling from the list in the text box below.', font=("Arial",15))
text2.grid(row=11, column=2, padx=25, pady=10)


text3= tk.Label(text= 'Happy 😀', font=("Arial",15))
text3.grid(row=13, column=2, padx=25, pady=10)
text4= tk.Label(text= 'Sad 😭')
text4.grid(row=14, column=2, padx=25, pady=10)
text5= tk.Label(text= 'Angry 🤬')
text5.grid(row=15, column=2, padx=25, pady=10)
text6= tk.Label(text= 'Loving 😘')
text6.grid(row=16, column=2, padx=25, pady=10)
text7= tk.Label(text= 'Crazy 🤪')
text7.grid(row=17, column=2, padx=25, pady=10)
text8= tk.Label(text= 'Confused 🤔')
text8.grid(row=18, column=2, padx=25, pady=10)
text9= tk.Label(text='Unloved 😞')
text9.grid(row=19, column=2, padx=25, pady=10)
text10= tk.Label(text='Mischeveous 😈')
text10.grid(row=20, column=2, padx=25, pady=10)
text11= tk.Label(text= 'Successful 🤩')
text11.grid(row=21, column=2, padx=25, pady=10)


#quote = 'you are the greatest'

#def my_click():
#    my_label = Label(root, text = quote)
#    my_label.grid(row=3, column=5, columnspan=3, padx=5, pady=10)
#
#my_button = Button(root, text='Click Me!', padx=50, pady=50, command=my_click, fg='yellow', bg='green', state=NORMAL)
#my_button.grid(row=3, column=5, columnspan=3, padx=5, pady=10)
#
root.mainloop()
