import tkinter as tk
root = tk.Tk()
root.geometry('400x400')
root.title('Allowence tracker')
# Entrys
deposit_entry = tk.Entry()
deposit_entry.grid(column=2, row=1)

withdraw_entry = tk.Entry()
withdraw_entry.grid(column=2, row=2)

# labels
deposit_label = tk.Label(text='deposit')
deposit_label.grid(column=1, row=1)

withdraw_label = tk.Label(text='withdraw')
withdraw_label.grid(column=1, row=2)

class allowence:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def deposit(self, deposit):
        self.amount += deposit

    def withdraw(self, amount):
        self.amount -= amount
# make object
Bilal = allowence('Bilal', 0)

def response():
    
    Bilal.deposit(int(deposit_entry.get()))
    Bilal.withdraw(int(withdraw_entry.get()))
    # make response
    answer_text = '{name} has ${amount}'.format(name=Bilal.name, amount=Bilal.amount)
    # make text window
    text=tk.Text(master=root, height=25, width=25)
    text.grid(column=1, row=6)
    text.insert(tk.END, answer_text)
#make button
button = tk.Button(text = 'print allowence', command = response)
button.grid(column=1, row=4)

root.mainloop()
    
        
