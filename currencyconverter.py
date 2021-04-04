from tkinter import *
from tkinter import LabelFrame
from ttkthemes import themed_tk as tk
from tkinter import ttk
import requests


def conversion():

    try:
        if var1.get()==var2.get():
            label7.config(text='Both currencies are same. No need of conversion')

        else:
            API_key ='FSGNCK6R2YXC1QI6'
            base_url = "https://www.alphavantage.co/query?function = CURRENCY_EXCHANGE_RATE"
            main_url =f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={var1.get()}&to_currency={var2.get()}&apikey={API_key}'

            info = requests.get(main_url)
            result = info.json()
            Exchange_Rate = float(result['Realtime Currency Exchange Rate']["5. Exchange Rate"])
            print(Exchange_Rate)
            print(result)
            amount = float(entry1.get())
            new_amount = round(amount * Exchange_Rate, 3)
            label4.config(text=f'{entry1.get()} {var1.get()} @ exch rate {Exchange_Rate} =',font=('courier',10,'bold'))
            label5.config(text=f'{new_amount} {var2.get()}',font=('courier',15,'bold'))

    except ValueError:
        label7.config(text='The Amount Field is empty. Please try again with valid amount.')


if __name__ == '__main__':
    
    window = tk.ThemedTk()
    window.geometry('650x400')
    window.get_themes()
    window.set_theme('kroc')
    window.title('Currency Converter Calculator')

    label1 = LabelFrame(window,text='FROM',pady=10,padx=10)
    label1.place(x=10,y=10)

    var1= StringVar()
    combo1=ttk.Combobox(label1,textvariable=var1,width=20)
    combo1['values'] = ('INR','USD','AUD','EUR','JPY','GBP','CAD','CHF')
    combo1.set('GBP')
    combo1.pack()

    label2 = LabelFrame(window,text='TO',pady=10,padx=10)
    label2.place(x=190,y=10)

    var2 = StringVar()
    combo2=ttk.Combobox(label2,textvariable=var2,width=20)
    combo2['values'] = ('INR','USD','AUD','EUR','JPY','GBP','CAD','CHF')
    combo2.set('EUR')
    combo2.pack()

    label3 = LabelFrame(window,text='AMOUNT',pady=10,padx=10)
    label3.place(x=370,y=10)
    entry1 = ttk.Entry(label3,width=20)
    entry1.pack()
    button1 = ttk.Button(text='CONVERT',command=conversion)
    button1.place(x=430,y=75)
    label4 = Label(text='')
    label4.place(x=16,y=90)
    label5 = Label(text='')
    label5.place(x=14,y=110)
    label6 = Label(text='')
    label6.place(x=14,y=180)
    label7 = Label(text='')
    label7.place(x=200,y=280)

    window.mainloop()
