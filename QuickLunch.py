'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
#####
Ismail A Ahmed
Midterm program
Version 1.0
'''
#help section/progress bar
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo #popup

root = Tk() #creates GUI
root.title("Quick Lunch") #title

def about():
    showinfo("Version", "Quick Lunch\nVersion 1.0")

def hello():
    showinfo("Help", "When you want to calculate your your lunch, enter your food and drink.When you want to check out, make sure you have submitted all of your info.")


def calculate():
    if len(drinky.get()) and len(box1.curselection()):
        drinkyprice = drinkprice[0]
        foodyprice = foodprice[0]
        pricex = drinkyprice + foodyprice
        tax_tax = (float(pricex) * 0.0825) #how much tax there is on the gift
        tax_tax = round(tax_tax, 2) #rounds tax to the second digit
        total_pricez = (float(pricex) + tax_tax) #adds how much tax there is on the gift with the price
        total_price = total_pricez + 0 #adds in shipping fee-tax w/ shipping
        total_pricefd = round(total_price, 2) #rounds the total price to the second digit
        price.set("Price: $"+ str(total_pricefd)) #str because cant add a string and a integer together
    else:
        showinfo("Error", "Please select both a drink and a food!")


def checkout():
    if len(drinky.get()) and len(box1.curselection()) and len(employeeID.get()) and len(payment.get()):
        drinkyprice = drinkprice[0]
        foodyprice = foodprice[0]
        pricex = drinkyprice + foodyprice
        tax_tax = (float(pricex) * 0.0825) #how much tax there is on the gift
        tax_tax = round(tax_tax, 2) #rounds tax to the second digit
        total_pricez = (float(pricex) + tax_tax) #adds how much tax there is on the gift with the price
        total_price = total_pricez + 0 #adds in shipping fee-tax w/ shipping
        total_pricefd = round(total_price, 2) #rounds the total price to the second digit
        outfile = open('lunchbuy.txt', 'a')
        file = ('Name:'+ ' '+employeeID.get()+' '+ 'Total price: $'+str(total_pricefd)+'\n')
        outfile.write(file)
        outfile.close()
        drinky.set('')  # makes password empty
        box1.select_clear(0, END)  # clears the selection
        employeeID.set('')  # clears the selection
        payment.set('')  # makes username empty
        days.config(state=NORMAL)
        days.delete(0, END)  # deletes the year
        days.insert(0, "Monday")  # inserts the default '2017'
        days.config(state='readonly')  # if not places here then wont change cause cant edit when 'readonly'
        price.set("Price: ")
        pb["value"] = 0
    else:
        showinfo("Error", "Please in all of the information!")
global count
count = 0
drinkprice = []
def buy_drink():
    global count
    if drinky.get() == "Soda":
        drinkprice.clear()  # clearing previous minute changes to the time(minute = 1 minute, 2 minutes, etc...)
        drinkprice.append(1)  # adding the current time to the list
        if count <1:
            pb["value"] +=34
            count+=1
    elif drinky.get() == "Tea":
        drinkprice.clear()  # clearing previous minute changes to the time(minute = 1 minute, 2 minutes, etc...)
        drinkprice.append(1)  # adding the current time to the list
        if count <1:
            pb["value"] +=34
            count+=1
    elif drinky.get() == "Milk":
        drinkprice.clear()  # clearing previous minute changes to the time(minute = 1 minute, 2 minutes, etc...)
        drinkprice.append(.75)  # adding the current time to the list
        if count <1:
            pb["value"] +=34
            count+=1
    elif drinky.get() == "Juice":
        drinkprice.clear()  # clearing previous minute changes to the time(minute = 1 minute, 2 minutes, etc...)
        drinkprice.append(1.25)  # adding the current time to the list
        if count <1:
            pb["value"] +=34
            count+=1
    elif drinky.get() == "Bottled Water":
        drinkprice.clear()  # clearing previous minute changes to the time(minute = 1 minute, 2 minutes, etc...)
        drinkprice.append(1)  # adding the current time to the list
        if count <1:
            pb["value"] +=34
            count+=1
global countz
countz = 0
foodprice = []
def buy_food(*args):
    try:
        global countz
        if box1.curselection()[0] == 0:
            foodprice.clear() #clearing previous minute changes to the time(minute = 1 minute, 2 minutes, etc...)
            foodprice.append(3) #adding the current time to the list
            if countz < 1:
                pb["value"] += 34
                countz += 1
        elif box1.curselection()[0] == 1:
            foodprice.clear()  # clearing previous minute changes to the time(minute = 1 minute, 2 minutes, etc...)
            foodprice.append(4)  # adding the current time to the list
            if countz < 1:
                pb["value"] += 34
                countz += 1
        elif box1.curselection()[0] == 2:
            foodprice.clear()  # clearing previous minute changes to the time(minute = 1 minute, 2 minutes, etc...)
            foodprice.append(3.75)  # adding the current time to the list
            if countz < 1:
                pb["value"] += 34
                countz += 1
        elif box1.curselection()[0] == 3:
            foodprice.clear()  # clearing previous minute changes to the time(minute = 1 minute, 2 minutes, etc...)
            foodprice.append(4)  # adding the current time to the list
            if countz < 1:
                pb["value"] += 34
                countz += 1
        elif box1.curselection()[0] == 4:
            foodprice.clear()  # clearing previous minute changes to the time(minute = 1 minute, 2 minutes, etc...)
            foodprice.append(15)  # adding the current time to the list
            if countz < 1:
                pb["value"] += 34
                countz += 1
        elif box1.curselection()[0] == 5:
            foodprice.clear()  # clearing previous minute changes to the time(minute = 1 minute, 2 minutes, etc...)
            foodprice.append(20)  # adding the current time to the list
            if countz < 1:
                pb["value"] += 34
                countz += 1
    except:
        pass

global countzb
countzb = 0
def prog(*args):
    global countzb
    if countzb < 1:
        pb["value"] += 34
        countzb += 1


root.option_add('*tearOff', FALSE) #gets rid of dashed line
menu = Menu(root) #creates menu
root.config(menu=menu) #adds ability to create options

subMenu = Menu(menu) #creats submenu
menu.add_cascade(label="File", menu=subMenu) # creates a memu option
subMenu.add_command(label="Exit", command=root.destroy) #file option

helpMenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpMenu) #creates another menu option
helpMenu.add_command(label="Help", command=hello) #file option
helpMenu.add_command(label="About", command=about) #file option

mainframe = ttk.Frame(root, padding="5 10")
mainframe.grid(column=0, row=0, columnspan=3, rowspan=3, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

planet_l= ['Sandwich', 'Pizza', 'Chicken Nuggets', 'Chicken', 'Tofu', 'Gluten/Soy/Shellfish Free Clam Chowder']#list of planets
dayy = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

drinky = StringVar()
planet = StringVar(value=planet_l)
payment = StringVar()
spin_day = StringVar()
employeeID = StringVar()
price = StringVar()

soda = ttk.Radiobutton(mainframe, text='Soda', variable=drinky, value='Soda', command=buy_drink)
soda.grid(column=1, row=2, sticky=(W,E))
tea = ttk.Radiobutton(mainframe, text='Tea', variable=drinky, value='Tea', command=buy_drink)
tea.grid(column=1, row=3, sticky=(W,E))
milk = ttk.Radiobutton(mainframe, text='Milk', variable=drinky, value='Milk', command=buy_drink)
milk.grid(column=1, row=4, sticky=(W,E))
juice = ttk.Radiobutton(mainframe, text='Juice', variable=drinky, value='Juice', command=buy_drink)
juice.grid(column=1, row=5, sticky=(W,E))
water = ttk.Radiobutton(mainframe, text='Bottled Water', variable=drinky, value='Bottled Water', command=buy_drink)
water.grid(column=1, row=6, sticky=(W,E))

box1 = Listbox(mainframe, height=6, width=25,listvariable=planet, exportselection=0) #planets
box1.grid(column = 1, row = 8, columnspan=2,sticky = (N,W,E,S))
#creates listbox which has all the planets. listvariable acceses the planets and adds to listbox
box1.bind('<<ListboxSelect>>',buy_food)

ttk.Entry(mainframe, textvariable=employeeID,width = 20).grid(column = 2, row = 2, sticky = W)

days = Spinbox(mainframe, values=dayy, textvariable=spin_day, width = 18, state = 'readonly')#spinbox that has year numbers
days.grid(column=2, row = 4, sticky = W)

pay = ttk.Combobox(mainframe, textvariable=payment, width=17, state = 'readonly')
pay.grid(column=2, row=6, sticky=(W))
pay['values'] = ('Credit', 'Check', 'Cash')
pay.bind('<<ComboboxSelected>>', prog)
#states of the US

ttk.Label(mainframe, text="Drink").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Entree").grid(column=1, row=7, sticky=W)
ttk.Label(mainframe, text="Employee ID").grid(column=2, row=1, sticky=W)
ttk.Label(mainframe, text="Day of the week").grid(column=2, row=3, sticky=W)
ttk.Label(mainframe, text="Payment type").grid(column=2, row=5, sticky=W)
ttk.Label(mainframe, text = "Price: ", textvariable=price).grid(column = 3, row = 1, sticky =(N,W))
price.set("Price: ")

ttk.Button(mainframe, text="Calculate", width = 10, command=calculate).grid(column=3, row=2, sticky = (N))
ttk.Button(mainframe, text="Checkout", width = 10, command=checkout).grid(column=3, row=3, sticky = (N))

pb = ttk.Progressbar(root, orient=VERTICAL, length=250, mode='determinate')
pb.grid(column=4, row =0, rowspan=4,sticky=W)

root.resizable(False, False)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()