from tkinter import *
from tkinter import filedialog,messagebox
from numpy import *
import time

def nextpage():

    if firstname.get() == '' or lastname.get() == '' or pnumber.get() == '':
        messagebox.showerror('Error', 'Please Enter Your Information!')
        return window

    else:
        window.destroy()

    def totalcost():

        global costofa4_2DP, costofa4c_2DP, costofphoto_2DP, subtotal_2DP, service_2DP, subtotalcost_2DP, totalquantity

        if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 :

            item1 = int(e_a480.get())
            item2 = int(e_a4120.get())
            item3 = int(e_a4140.get())
            item4 = int(e_a4160.get())
            item5 = int(e_a4matt.get())

            item6 = int(e_a4c80.get())
            item7 = int(e_a4c120.get())
            item8 = int(e_a4c140.get())
            item9 = int(e_a4c160.get())
            item10 = int(e_a4cmatt.get())

            item11 = int(e_s4r.get())
            item12 = int(e_s5r.get())
            item13 = int(e_s8r.get())
            item14 = int(e_sa4.get())
            item15 = int(e_spass.get())

            priceofa4 = (item1*0.35)+(item2*0.55)+(item3*0.75)+(item4*0.95)+(item5*1.00)
            priceofa4c = (item6*1.45)+(item7*2.15)+(item8*3.15)+(item9*4.15)+(item10*5.05)
            priceofphoto = (item11*0.95)+(item12*5.50)+(item13*8.50)+(item14*17.50)+(item15*1.50)

            totalquantity = item1 + item2 + item3 + item4 + item5 + item6 + item7 + item8 + item9 + item10 + item11 + item12 + item13 + item14 + item15

            costofa4_2DP = "{:.2f}".format(priceofa4)
            costofa4.set('RM' + str(costofa4_2DP))
            costofa4c_2DP = "{:.2f}".format(priceofa4c)
            costofa4c.set('RM' + str(costofa4c_2DP))
            costofphoto_2DP = "{:.2f}".format(priceofphoto)
            costofphoto.set('RM' + str(costofphoto_2DP))

            subtotalbefore = priceofa4 + priceofa4c + priceofphoto
            subtotal_2DP = "{:.2f}".format(subtotalbefore)
            subtotal.set('RM' + str(subtotal_2DP))

            service = subtotalbefore * 0.06
            service_2DP = "{:.2f}".format(service)
            servicetax.set('RM' + str(service_2DP))

            subtotalafter = subtotalbefore + service
            subtotalcost_2DP = "{:.2f}".format(subtotalafter)
            subtotalcost.set('RM' + str(subtotalcost_2DP))

        else:
            messagebox.showerror('Error', 'No Item Is Selected')

    def reset():

        e_a480.set('0')
        e_a4120.set('0')
        e_a4140.set('0')
        e_a4160.set('0')
        e_a4matt.set('0')

        e_a4c80.set('0')
        e_a4c120.set('0')
        e_a4c140.set('0')
        e_a4c160.set('0')
        e_a4cmatt.set('0')

        e_s4r.set('0')
        e_s5r.set('0')
        e_s8r.set('0')
        e_sa4.set('0')
        e_spass.set('0')

        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)
        var5.set(0)
        var6.set(0)
        var7.set(0)
        var8.set(0)
        var9.set(0)
        var10.set(0)
        var11.set(0)
        var12.set(0)
        var13.set(0)
        var14.set(0)
        var15.set(0)

        costofa4.set('')
        costofa4c.set('')
        costofphoto.set('')
        subtotal.set('')
        servicetax.set('')
        subtotalcost.set('')

    def send():

        def send1():

            if phnumber.get() == '':
                messagebox.showerror('Error', 'Please Enter Phone Number to Send!')



            else:
                messagebox.showinfo('Information','Successfully Send the Receipt to Your Phone',command=window3.destroy())

        def receipt():

            textReceipt.delete(1.0, END)
            x = random.randint(100, 1000)

            if totalquantity < 50:
                datetaken = 1

            elif totalquantity >= 50 and totalquantity <100:
                datetaken = 2

            elif totalquantity >= 100 and totalquantity <200:
                datetaken = 3

            elif totalquantity >= 200 and totalquantity <300:
                datetaken = 4

            elif totalquantity >= 300 and totalquantity <400:
                datetaken = 4

            elif totalquantity >= 400 and totalquantity <500:
                datetaken = 5

            else:
                datetaken = 6

            billnumber = 'NO BILL : 00'+ str(x)
            date = time.strftime('%d.%m.%Y')
            textReceipt.insert(END,billnumber + '\t\t\t      DATE : ' + date)
            textReceipt.insert(END, f'Name : {str(firstname.get())} {str(lastname.get())}\n')
            textReceipt.insert(END, f'Phone Number : {str(pnumber.get())}\n')
            textReceipt.insert(END, f'Date To Taken : After {datetaken} days\n')
            textReceipt.insert(END, '***************************************************************\n')
            textReceipt.insert(END, 'Items:\t                     Quantity\t\t   Cost Of Items(RM)\n')
            textReceipt.insert(END, '***************************************************************\n')

            if e_a480.get() != '0':
                item1_2D = int(e_a480.get()) * 0.35
                ITEM1 = "{:.2f}".format(item1_2D)
                textReceipt.insert(END, f'A4(B&W) 80gsm\t\t          {(int(e_a480.get()))}\t\t         {ITEM1}\t\t\n\n')

            if e_a4120.get() != '0':
                item2_2D = int(e_a4120.get()) * 0.55
                ITEM2 = "{:.2f}".format(item2_2D)
                textReceipt.insert(END, f'A4(B&W) 120gsm\t\t          {(int(e_a4120.get()))}\t\t         {ITEM2}\t\t\n\n')

            if e_a4140.get() != '0':
                item3_2D = int(e_a4140.get()) * 0.75
                ITEM3 = "{:.2f}".format(item3_2D)
                textReceipt.insert(END, f'A4(B&W) 140gsm\t\t          {(int(e_a4140.get()))}\t\t         {ITEM3}\t\t\n\n')

            if e_a4160.get() != '0':
                item4_2D = int(e_a4160.get()) * 0.95
                ITEM4 = "{:.2f}".format(item4_2D)
                textReceipt.insert(END, f'A4(B&W) 160gsm\t\t          {(int(e_a4160.get()))}\t\t         {ITEM4}\t\t\n\n')

            if e_a4matt.get() != '0':
                item5_2D = int(e_a4matt.get()) * 1.00
                ITEM5 = "{:.2f}".format(item5_2D)
                textReceipt.insert(END, f'A4(B&W) Matt\t\t          {(int(e_a4matt.get()))}\t\t         {ITEM5}\t\t\n\n')

            if e_a4c80.get() != '0':
                item6_2D = int(e_a4c80.get()) * 1.45
                ITEM6 = "{:.2f}".format(item6_2D)
                textReceipt.insert(END, f'A4(C) 80gsm\t\t          {(int(e_a4c80.get()))}\t\t         {ITEM6}\t\t\n\n')

            if e_a4c120.get() != '0':
                item7_2D = int(e_a4c120.get()) * 2.15
                ITEM7 = "{:.2f}".format(item7_2D)
                textReceipt.insert(END, f'A4(C) 120gsm\t\t          {(int(e_a4c120.get()))}\t\t         {ITEM7}\t\t\n\n')

            if e_a4c140.get() != '0':
                item8_2D = int(e_a4c140.get()) * 3.15
                ITEM8 = "{:.2f}".format(item8_2D)
                textReceipt.insert(END, f'A4(C) 140gsm\t\t          {(int(e_a4c140.get()))}\t\t         {ITEM8}\t\t\n\n')

            if e_a4c160.get() != '0':
                item9_2D = int(e_a4c160.get()) * 4.15
                ITEM9 = "{:.2f}".format(item9_2D)
                textReceipt.insert(END, f'A4(C) 160gsm\t\t          {(int(e_a4c160.get()))}\t\t         {ITEM9}\t\t\n\n')

            if e_a4cmatt.get() != '0':
                item10_2D = int(e_a4cmatt.get()) * 5.05
                ITEM10 = "{:.2f}".format(item10_2D)
                textReceipt.insert(END, f'A4(C) Matt\t\t          {(int(e_a4cmatt.get()))}\t\t         {ITEM10}\t\t\n\n')

            if e_s4r.get() != '0':
                item11_2D = int(e_s4r.get()) * 0.95
                ITEM11 = "{:.2f}".format(item11_2D)
                textReceipt.insert(END, f'Photo S4R\t\t          {(int(e_s4r.get()))}\t\t         {ITEM11}\t\t\n\n')

            if e_s5r.get() != '0':
                item12_2D = int(e_s5r.get()) * 5.50
                ITEM12 = "{:.2f}".format(item12_2D)
                textReceipt.insert(END, f'Photo S5R\t\t          {(int(e_s5r.get()))}\t\t         {ITEM12}\t\t\n\n')

            if e_s8r.get() != '0':
                item13_2D = int(e_s8r.get()) * 8.50
                ITEM13 = "{:.2f}".format(item13_2D)
                textReceipt.insert(END, f'Photo S8R\t\t          {(int(e_s8r.get()))}\t\t         {ITEM13}\t\t\n\n')

            if e_sa4.get() != '0':
                item14_2D = int(e_sa4.get()) * 17.50
                ITEM14 = "{:.2f}".format(item14_2D)
                textReceipt.insert(END, f'Photo SA4\t\t          {(int(e_sa4.get()))}\t\t         {ITEM14}\t\t\n\n')

            if e_spass.get() != '0':
                item15_2D = int(e_spass.get()) * 1.50
                ITEM15 = "{:.2f}".format(item15_2D)
                textReceipt.insert(END, f'Photo Passport\t\t          {(int(e_spass.get()))}\t\t         {ITEM15}\t\t\n\n')

            textReceipt.insert(END, '***************************************************************\n')

            if costofa4.get() != '0 Rs':
                textReceipt.insert(END, f'Total Cost Of A4 (B&W)\t\t\t\t   RM{costofa4_2DP}\n\n')
            if costofa4c.get() != '0 Rs':
                textReceipt.insert(END, f'Total Cost Of A4 (C)\t\t\t\t   RM{costofa4c_2DP}\n\n')
            if costofphoto.get() != '0 Rs':
                textReceipt.insert(END, f'Total Cost Of Photo\t\t\t\t   RM{costofphoto_2DP}\n\n')

            textReceipt.insert(END, f'Sub Total\t\t\t\t   RM{subtotal_2DP}\n\n')
            textReceipt.insert(END, f'Service Tax\t\t\t\t   RM{service_2DP}\n\n')
            textReceipt.insert(END, f'Total Cost\t\t\t\t   RM{subtotalcost_2DP}\n\n')
            textReceipt.insert(END, '************************THANK YOU***********************\n')

        window3 = Toplevel()
        window3.geometry('900x650+350+90')
        window3.title('PRINTING SERVICE SYSTEM')
        window3.grab_set()
        window3.config(bg='dark orange')
        window3.resizable(0, 0)
        PayFrame = Frame(window3, bd=10, relief=RIDGE, bg='dark orange')
        PayFrame.pack(side=RIGHT)
        RecFrame = Frame(window3, bd=10, relief=RIDGE, bg='dark orange')
        RecFrame.pack(side=LEFT)
        labelTitle4 = LabelFrame(PayFrame, text='PLEASE SCAN THE QR CODE TO PAY', font=('arial', 12, 'bold'))
        labelTitle4.pack()
        image = PhotoImage(file="C:\\GUI\\QR.png")
        label = Label(labelTitle4, image=image, bg='dark orange')
        label.pack(side=LEFT)

        phnumber=StringVar()

        buttonSend = Button(PayFrame, text='Send', font=('arial', 14, 'bold'), fg='white', bg='red4', bd=3, padx=5, command=send1)
        buttonSend.pack(side=BOTTOM)
        textsend = Text(PayFrame, font=('arial', 12, 'bold'), bd=3, width=42, height=1)
        textsend.pack(side=BOTTOM)
        textss = Entry(textsend, font=('arial', 12, 'bold'), textvariable=phnumber)
        textss.pack()
        labelTitle2 = Label(PayFrame, text='PLEASE ENTER A PHONE NUMBER YOU WANT TO SEND', font=('arial', 12, 'bold'))
        labelTitle2.pack(side=BOTTOM)
        labelTitle3 = Label(PayFrame, text='IF YOU WANT TO SAVE THE RECEIPT', font=('arial', 12, 'bold'))
        labelTitle3.pack(side=BOTTOM)
        textReceipt = Text(RecFrame, font=('arial', 12, 'bold'), bd=3, width=41, height=27)
        textReceipt.pack()
        buttonReceipt = Button(RecFrame, text='Receipt', font=('arial', 14, 'bold'), fg='white', bg='red4', bd=3, padx=5, command=receipt)
        buttonReceipt.pack(side=BOTTOM)

        window3.mainloop()

    def openinsert():
        messagebox.showinfo('Information', 'Please Select Files To Print')
        filedialog.askopenfilename()
        messagebox.showinfo('Information','Successfully Insert Your File')

    def a480():
        if var1.get()==1:
            texta480.config(state=NORMAL)
            texta480.delete(0,END)
            texta480.focus()
        else:
            texta480.config(state=DISABLED)
            e_a480.set('0')

    def a4120():
        if var2.get()==1:
            texta4120.config(state=NORMAL)
            texta4120.delete(0,END)
            texta4120.focus()
        else:
            texta4120.config(state=DISABLED)
            e_a4120.set('0')

    def a4140():
        if var3.get() == 1:
            texta4140.config(state=NORMAL)
            texta4140.delete(0, END)
            texta4140.focus()
        else:
            texta4140.config(state=DISABLED)
            e_a4140.set('0')

    def a4160():
        if var4.get()==1:
            texta4160.config(state=NORMAL)
            texta4160.delete(0,END)
            texta4160.focus()
        else:
            texta4160.config(state=DISABLED)
            e_a4160.set('0')

    def a4matt():
        if var5.get()==1:
            texta4matt.config(state=NORMAL)
            texta4matt.delete(0,END)
            texta4matt.focus()
        else:
            texta4matt.config(state=DISABLED)
            e_a4matt.set('0')

    def a4c80():
        if var6.get()==1:
            texta4c80.config(state=NORMAL)
            texta4c80.delete(0,END)
            texta4c80.focus()
        else:
            texta4c80.config(state=DISABLED)
            e_a4c80.set('0')

    def a4c120():
        if var7.get()==1:
            texta4c120.config(state=NORMAL)
            texta4c120.delete(0,END)
            texta4c120.focus()
        else:
            texta4c120.config(state=DISABLED)
            e_a4c120.set('0')

    def a4c140():
        if var8.get()==1:
            texta4c140.config(state=NORMAL)
            texta4c140.delete(0,END)
            texta4c140.focus()
        else:
            texta4c140.config(state=DISABLED)
            e_a4c140.set('0')

    def a4c160():
        if var9.get()==1:
            texta4c160.config(state=NORMAL)
            texta4c160.delete(0,END)
            texta4c160.focus()
        else:
            texta4c160.config(state=DISABLED)
            e_a4c160.set('0')

    def a4cmatt():
        if var10.get()==1:
            texta4cmatt.config(state=NORMAL)
            texta4cmatt.delete(0,END)
            texta4cmatt.focus()
        else:
            texta4cmatt.config(state=DISABLED)
            e_a4cmatt.set('0')

    def s4r():
        if var11.get()==1:
            texts4r.config(state=NORMAL)
            texts4r.delete(0,END)
            texts4r.focus()
        else:
            texts4r.config(state=DISABLED)
            e_s4r.set('0')

    def s5r():
        if var12.get()==1:
            texts5r.config(state=NORMAL)
            texts5r.delete(0,END)
            texts5r.focus()
        else:
            texts5r.config(state=DISABLED)
            e_s5r.set('0')

    def s8r():
        if var13.get()==1:
            texts8r.config(state=NORMAL)
            texts8r.delete(0,END)
            texts8r.focus()
        else:
            texts8r.config(state=DISABLED)
            e_s8r.set('0')

    def sa4():
        if var14.get()==1:
            textsa4.config(state=NORMAL)
            textsa4.delete(0,END)
            textsa4.focus()
        else:
            textsa4.config(state=DISABLED)
            e_sa4.set('0')

    def spass():
        if var15.get()==1:
            textspass.config(state=NORMAL)
            textspass.delete(0,END)
            textspass.focus()
        else:
            textspass.config(state=DISABLED)
            e_spass.set('0')

    window1=Tk()
    window1.geometry('960x710+300+50')
    window1.resizable(0, 0)
    window1.title('PRINTING SERVICE SYSTEM')
    window1.config(bg='dark orange')

    topFrame = Frame(window1, bd=10, relief=RIDGE, bg='dark orange')
    topFrame.pack(side=TOP)
    labelTitle = Label(topFrame, text='ePRINTly', font=('Times', '30', 'bold italic'), fg='snow', bd=10, bg='dark orange', width=38)
    labelTitle.grid(row=0, column=0)

    menuFrame = Frame(window1, bd=10, relief=RIDGE, bg='dark orange')
    menuFrame.pack()
    costFrame = Frame(menuFrame, bd=4, relief=RIDGE, bg='dark orange', pady=10)
    costFrame.pack(side=BOTTOM)
    viewFrame = Frame(menuFrame, bd=4, relief=RIDGE, bg='dark orange')
    viewFrame.pack(side=TOP)
    buttonFrame = Frame(viewFrame, bd=4, relief=RIDGE, bg='dark orange')
    buttonFrame.pack(side=TOP)
    viewA4Frame = Frame(viewFrame, bd=4, relief=RIDGE, bg='dark orange')
    viewA4Frame.pack(side=LEFT)
    viewA4CFrame = Frame(viewFrame, bd=4, relief=RIDGE, bg='dark orange')
    viewA4CFrame.pack(side=LEFT)
    viewPFrame = Frame(viewFrame, bd=4, relief=RIDGE, bg='dark orange')
    viewPFrame.pack(side=LEFT)
    A4Frame = LabelFrame(menuFrame, text='A4 Black & White', font=('arial', 19, 'bold'), bd=10, relief=RIDGE, fg='red4')
    A4Frame.pack(side=LEFT)
    A4CFrame = LabelFrame(menuFrame, text='A4 Colour', font=('arial', 19, 'bold'), bd=10, relief=RIDGE, fg='red4')
    A4CFrame.pack(side=LEFT)
    PhotoFrame = LabelFrame(menuFrame, text='Photo', font=('arial', 19, 'bold'), bd=10, relief=RIDGE, fg='red4')
    PhotoFrame.pack(side=LEFT)

    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    var6 = IntVar()
    var7 = IntVar()
    var8 = IntVar()
    var9 = IntVar()
    var10 = IntVar()
    var11 = IntVar()
    var12 = IntVar()
    var13 = IntVar()
    var14 = IntVar()
    var15 = IntVar()

    costofa4 = StringVar()
    costofa4c = StringVar()
    costofphoto = StringVar()
    subtotal = StringVar()
    servicetax = StringVar()
    subtotalcost = StringVar()

    e_a480 = StringVar()
    e_a4120 = StringVar()
    e_a4140 = StringVar()
    e_a4160 = StringVar()
    e_a4matt = StringVar()

    e_a4c80 = StringVar()
    e_a4c120 = StringVar()
    e_a4c140 = StringVar()
    e_a4c160 = StringVar()
    e_a4cmatt = StringVar()

    e_s4r = StringVar()
    e_s5r = StringVar()
    e_s8r = StringVar()
    e_sa4 = StringVar()
    e_spass = StringVar()

    e_a480.set('0')
    e_a4120.set('0')
    e_a4140.set('0')
    e_a4160.set('0')
    e_a4matt.set('0')

    e_a4c80.set('0')
    e_a4c120.set('0')
    e_a4c140.set('0')
    e_a4c160.set('0')
    e_a4cmatt.set('0')

    e_s4r.set('0')
    e_s5r.set('0')
    e_s8r.set('0')
    e_sa4.set('0')
    e_spass.set('0')

    a480 = Checkbutton(A4Frame, text='80gsm', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var1, command=a480)
    a480.grid(row=0, column=0, sticky=W)

    a4120 = Checkbutton(A4Frame, text='120gsm', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var2, command=a4120)
    a4120.grid(row=1, column=0, sticky=W)

    a4140 = Checkbutton(A4Frame, text='140gsm', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var3, command=a4140)
    a4140.grid(row=2, column=0, sticky=W)

    a4160 = Checkbutton(A4Frame, text='160gsm', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var4, command=a4160)
    a4160.grid(row=3, column=0, sticky=W)

    a4matt = Checkbutton(A4Frame, text='Matt Paper', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var5, command=a4matt)
    a4matt.grid(row=4, column=0, sticky=W)

    texta480 = Entry(A4Frame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_a480)
    texta480.grid(row=0, column=1)

    texta4120 = Entry(A4Frame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_a4120)
    texta4120.grid(row=1, column=1)

    texta4140 = Entry(A4Frame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_a4140)
    texta4140.grid(row=2, column=1)

    texta4160 = Entry(A4Frame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_a4160)
    texta4160.grid(row=3, column=1)

    texta4matt = Entry(A4Frame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_a4matt)
    texta4matt.grid(row=4, column=1)

    a4c80 = Checkbutton(A4CFrame, text='80gsm', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var6, command=a4c80)
    a4c80.grid(row=0, column=0, sticky=W)

    a4c120 = Checkbutton(A4CFrame, text='120gsm', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var7, command=a4c120)
    a4c120.grid(row=1, column=0, sticky=W)

    a4c140 = Checkbutton(A4CFrame, text='140gsm', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var8, command=a4c140)
    a4c140.grid(row=2, column=0, sticky=W)

    a4c160 = Checkbutton(A4CFrame, text='160gsm', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var9, command=a4c160)
    a4c160.grid(row=3, column=0, sticky=W)

    a4cmatt = Checkbutton(A4CFrame, text='Matt Paper', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var10, command=a4cmatt)
    a4cmatt.grid(row=4, column=0, sticky=W)

    texta4c80 = Entry(A4CFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_a4c80)
    texta4c80.grid(row=0, column=1)

    texta4c120 = Entry(A4CFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_a4c120)
    texta4c120.grid(row=1, column=1)

    texta4c140 = Entry(A4CFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_a4c140)
    texta4c140.grid(row=2, column=1)

    texta4c160 = Entry(A4CFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_a4c160)
    texta4c160.grid(row=3, column=1)

    texta4cmatt = Entry(A4CFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_a4cmatt)
    texta4cmatt.grid(row=4, column=1)

    s4r = Checkbutton(PhotoFrame, text='Size 4R', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var11, command=s4r)
    s4r.grid(row=0, column=0, sticky=W)

    s5r = Checkbutton(PhotoFrame, text='Size 5R', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var12, command=s5r)
    s5r.grid(row=1, column=0, sticky=W)

    s8r = Checkbutton(PhotoFrame, text='Size 8R', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var13, command=s8r)
    s8r.grid(row=2, column=0, sticky=W)

    sa4 = Checkbutton(PhotoFrame, text='Size A4', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var14, command=sa4)
    sa4.grid(row=3, column=0, sticky=W)

    spass = Checkbutton(PhotoFrame, text='Size Passport', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var15, command=spass)
    spass.grid(row=4, column=0, sticky=W)

    texts4r = Entry(PhotoFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_s4r)
    texts4r.grid(row=0, column=1)

    texts5r = Entry(PhotoFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_s5r)
    texts5r.grid(row=1, column=1)

    texts8r = Entry(PhotoFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_s8r)
    texts8r.grid(row=2, column=1)

    textsa4 = Entry(PhotoFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_sa4)
    textsa4.grid(row=3, column=1)

    textspass = Entry(PhotoFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_spass)
    textspass.grid(row=4, column=1)

    labelCosta4 = Label(costFrame, text='Cost of A4 Black & White', font=('arial', 16, 'bold'), bg='dark orange', fg='Black')
    labelCosta4.grid(row=0, column=0)

    textCosta4 = Entry(costFrame, font=('arial', 16, 'bold'), bd=6, width=14,textvariable=costofa4)
    textCosta4.grid(row=0, column=1, padx=41)

    labelCosta4c = Label(costFrame, text='Cost of A4 Colour', font=('arial', 16, 'bold'), bg='dark orange', fg='Black')
    labelCosta4c.grid(row=1, column=0)

    textCosta4c = Entry(costFrame, font=('arial', 16, 'bold'), bd=6, width=14,textvariable=costofa4c)
    textCosta4c.grid(row=1, column=1, padx=41)

    labelCostphoto = Label(costFrame, text='Cost of Photo', font=('arial', 16, 'bold'), bg='dark orange', fg='Black')
    labelCostphoto.grid(row=2, column=0)

    textCostphoto = Entry(costFrame, font=('arial', 16, 'bold'), bd=6, width=14, textvariable=costofphoto)
    textCostphoto.grid(row=2, column=1, padx=41)

    labelSubTotal = Label(costFrame, text='Sub Total', font=('arial', 16, 'bold'), bg='dark orange', fg='Black')
    labelSubTotal.grid(row=0, column=2)

    textSubTotal = Entry(costFrame, font=('arial', 16, 'bold'), bd=6, width=14, textvariable=subtotal)
    textSubTotal.grid(row=0, column=3, padx=41)

    labelServiceTax = Label(costFrame, text='Service Tax', font=('arial', 16, 'bold'), bg='dark orange', fg='Black')
    labelServiceTax.grid(row=1, column=2)

    textServiceTax = Entry(costFrame, font=('arial', 16, 'bold'), bd=6, width=14,textvariable=servicetax)
    textServiceTax.grid(row=1, column=3, padx=41)

    labelTotalCost = Label(costFrame, text='Total Cost', font=('arial', 16, 'bold'), bg='dark orange', fg='Black')
    labelTotalCost.grid(row=2, column=2)

    textTotalCost = Entry(costFrame, font=('arial', 16, 'bold'), bd=6, width=14, textvariable=subtotalcost)
    textTotalCost.grid(row=2, column=3, padx=41)

    labelCostofA4 = Label(viewA4Frame, text='Cost of A4 Black & White', font=('arial', 16, 'bold italic'), bg='dark orange', fg='Black')
    labelCostofA4.grid(row=0, column=0,sticky=W)
    labelCostofA4 = Label(viewA4Frame, text='80gsm        = RM0.35', font=('arial', 12, 'bold italic'), bg='dark orange', fg='Black')
    labelCostofA4.grid(row=1, column=0,sticky=W)
    labelCostofA4 = Label(viewA4Frame, text='120gsm      = RM0.55', font=('arial', 12, 'bold italic'), bg='dark orange', fg='Black')
    labelCostofA4.grid(row=2, column=0,sticky=W)
    labelCostofA4 = Label(viewA4Frame, text='140gsm      = RM0.75', font=('arial', 12, 'bold italic'), bg='dark orange', fg='Black')
    labelCostofA4.grid(row=3, column=0,sticky=W)
    labelCostofA4 = Label(viewA4Frame, text='160gsm      = RM0.95', font=('arial', 12, 'bold italic'), bg='dark orange', fg='Black')
    labelCostofA4.grid(row=4, column=0,sticky=W)
    labelCostofA4 = Label(viewA4Frame, text='Matt Paper = RM1.00', font=('arial', 12, 'bold italic'), bg='dark orange', fg='Black')
    labelCostofA4.grid(row=5, column=0,sticky=W)

    labelCostofA4C = Label(viewA4CFrame, text='Cost of A4 Colour', font=('arial', 16, 'bold italic'), bg='dark orange', fg='Black')
    labelCostofA4C.grid(row=0, column=1, sticky=W)
    labelCostofA4C = Label(viewA4CFrame, text='80gsm        = RM1.45', font=('arial', 12, 'bold italic'), bg='dark orange', fg='Black')
    labelCostofA4C.grid(row=1, column=1, sticky=W)
    labelCostofA4C = Label(viewA4CFrame, text='120gsm      = RM2.15', font=('arial', 12, 'bold italic'), bg='dark orange', fg='Black')
    labelCostofA4C.grid(row=2, column=1, sticky=W)
    labelCostofA4C = Label(viewA4CFrame, text='140gsm      = RM3.15', font=('arial', 12, 'bold italic'), bg='dark orange', fg='Black')
    labelCostofA4C.grid(row=3, column=1, sticky=W)
    labelCostofA4C = Label(viewA4CFrame, text='160gsm      = RM4.15', font=('arial', 12, 'bold italic'), bg='dark orange', fg='Black')
    labelCostofA4C.grid(row=4, column=1, sticky=W)
    labelCostofA4C = Label(viewA4CFrame, text='Matt Paper = RM5.05', font=('arial', 12, 'bold italic'), bg='dark orange', fg='Black')
    labelCostofA4C.grid(row=5, column=1, sticky=W)

    labelCostofPhoto = Label(viewPFrame, text='Cost of Photo', font=('arial', 16, 'bold italic'), bg='dark orange', fg='Black')
    labelCostofPhoto.grid(row=0, column=2, sticky=W)
    labelCostofPhoto = Label(viewPFrame, text='Size 4R             = RM0.95', font=('arial', 12, 'bold italic'), bg='dark orange', fg='Black')
    labelCostofPhoto.grid(row=1, column=2, sticky=W)
    labelCostofPhoto = Label(viewPFrame, text='Size 5R             = RM5.50', font=('arial', 12, 'bold italic'), bg='dark orange', fg='Black')
    labelCostofPhoto.grid(row=2, column=2,sticky=W)
    labelCostofPhoto = Label(viewPFrame, text='Size 8R             = RM8.50', font=('arial', 12, 'bold italic'), bg='dark orange', fg='Black')
    labelCostofPhoto.grid(row=3, column=2,sticky=W)
    labelCostofPhoto = Label(viewPFrame, text='Size A4             = RM17.50', font=('arial', 12, 'bold italic'), bg='dark orange', fg='Black')
    labelCostofPhoto.grid(row=4, column=2,sticky=W)
    labelCostofPhoto = Label(viewPFrame, text='Size Passport = RM1.50', font=('arial', 12, 'bold italic'), bg='dark orange', fg='Black')
    labelCostofPhoto.grid(row=5, column=2,sticky=W)

    buttonOpen = Button(buttonFrame, text='Insert Files To Print', font=('arial', 14, 'bold'), fg='white', bg='red4', bd=3, padx=5, command=openinsert)
    buttonOpen.grid(row=0, column=0)

    buttonTotal = Button(buttonFrame, text='Calculate Total', font=('arial', 14, 'bold'), fg='white', bg='red4', bd=3, padx=5, command=totalcost)
    buttonTotal.grid(row=0, column=1)

    buttonSend = Button(buttonFrame, text='Receipt & Payment', font=('arial', 14, 'bold'), fg='white', bg='red4', bd=3, padx=5, command=send)
    buttonSend.grid(row=0, column=3)

    buttonReset = Button(buttonFrame, text='Reset', font=('arial', 14, 'bold'), fg='white', bg='red4', bd=3, padx=5, command=reset)
    buttonReset.grid(row=0, column=4)

    window1.mainloop()

window = Tk()
window.title("PRINTING SERVICE SYSTEM")
window.geometry('1000x700+300+50')
window.resizable(0, 0)

firstname=StringVar()
lastname=StringVar()
pnumber=StringVar()

imagewall = ("C:\\GUI\\Wallpaper.png")
bck_end = PhotoImage(file=imagewall)
lbl = Label(window, image=bck_end)
lbl.place(x=-45,y=-100)

user_info_frame = Frame(window)
user_info_frame.pack(side=BOTTOM)

user_info_frame = LabelFrame(user_info_frame, text="USER INFORMATION", font=('arial', 20, 'bold'),fg='Red4')
user_info_frame.pack(side=LEFT)

first_name_label = Label(user_info_frame, text="First Name", font=('arial', 18, 'bold'))
first_name_label.grid(row=0, column=0, sticky=W)
last_name_label = Label(user_info_frame, text="Last Name", font=('arial', 18, 'bold'))
last_name_label.grid(row=1, column=0, sticky=W)

first_name_entry = Entry(user_info_frame, font=('arial', 18, 'bold'), textvariable=firstname)
last_name_entry = Entry(user_info_frame, font=('arial', 18, 'bold'), textvariable=lastname)
first_name_entry.grid(row=0, column=1)
last_name_entry.grid(row=1, column=1)

phone = Label(user_info_frame, text="Phone Number", font=('arial', 18, 'bold'))
phone.grid(row=2, column=0, sticky=W)
phone_entry = Entry(user_info_frame, font=('arial', 18, 'bold'), textvariable=pnumber)
phone_entry.grid(row=2, column=1)

button = Button(user_info_frame, text="Enter Data", font=('arial', 18, 'bold'), command=nextpage)
button.grid(row=5, column=1, sticky="news", padx=20, pady=10)

window.mainloop()