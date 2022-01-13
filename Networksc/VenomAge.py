import tkinter as tk
import subprocess
import random


from tkinter import messagebox

form = tk.Tk()
form.title("VenomAge")
form.geometry("600x400")
form.resizable(True,True)

var = messagebox.showinfo("Warning ", "Welcome to VenomAge")



label=tk.Label(form, font='italic 17 bold',text="Choose The Action You Want")
label.pack()

label9=tk.Label(form, font='italic 8 bold',text="@Batu Kapicioglu")
label9.place(x=465,y=370)

label10=tk.Label(form, font='italic 7 bold',text="Linux")
label10.place(x=25,y=373)

def mac_veri():

    form.destroy()
    form2 = tk.Tk()
    form2.title("VenomAge")
    form2.geometry("600x400")
    form2.resizable(True, True)

    var = messagebox.showinfo("Warning ", "Mac_Changer Starting")

    label1=tk.Label(form2, font='italic 17 bold' ,text="Mac Address Changer")
    label1.pack()

    label2=tk.Label(form2, font='italic 10 bold' ,text="Interface :")
    label2.place(x=10,y=50)

    label3=tk.Label(form2, font='italic 10 bold' ,text="Mac Address :")
    label3.place(x=10,y=90)

    label3=tk.Label(form2, font='italic 17 bold' ,text="Rondom MAC Address")
    label3.place(x=167,y=200)

    label3=tk.Label(form2, font='italic 10 bold' ,text="Interface :")
    label3.place(x=10,y=260)

    label11 = tk.Label(form2, font='italic 7', text="**This is the demo version which is still under development and improvement.**")
    label11.place(x=55, y=373)

    entry_inter=tk.Entry(form2)
    entry_inter.place(x=150,y=50)

    entry_mac=tk.Entry(form2)
    entry_mac.place(x=150,y=90)

    entry_inter_rndom=tk.Entry(form2)
    entry_inter_rndom.place(x=150,y=260)



    def inter():
        intere=str(entry_inter.get())
        mac = str(entry_mac.get())

        subprocess.call(['ifconfig',intere,'down'])
        subprocess.call(['ifconfig', intere, 'hw','ether',mac])
        subprocess.call(['ifconfig', intere, 'up'])

        if entry_inter.get()=="eth0" :
            msg=messagebox.showinfo("WARNING",message="Successful")
        elif entry_inter.get()=="eth1" :
            msg=messagebox.showinfo("WARNING",message="Successful")
        elif entry_inter.get()=="eth2" :
            msg=messagebox.showinfo("WARNING",message="Successful")
        elif entry_inter.get()=="tun0" :
            msg=messagebox.showinfo("WARNING",message="Successful")
        elif entry_inter.get() == "wlan0":
            msg = messagebox.showinfo("WARNING", message="Successful")
        elif entry_inter.get() == "wlan1":
            msg=messagebox.showinfo("WARNING",message="Successful")
        else :
            msg1 = messagebox.showinfo("ERROR", message="Please Change Interface")
            msg2 = messagebox.showinfo("WARNING", message="Example : eth_ , tun_ , wlan_")




    buton4 = tk.Button(form2, font='italic 12 bold', text='CHANGE', fg='white', bg='blue', command=inter)
    buton4.place(x=360, y=78)

    def inter1():
        intere1=str(entry_inter_rndom.get())
        a=["0f:b1:f3:c4:8f:1e ", "fe:37:c9:fb:b4:cd ", "14:81:b9:03:3b:ba", "29:0b:20:81:80:5e", "84:9c:08:01:ea:6f","72:93:b4:d9:14:9e",
        "06:ec:9f:0d:4c:00","a8:93:05:01:63:f7","7b:59:04:57:72:7d","34:97:bd:eb:bd:77","29:53:84:21:52:4b","5c:bb:01:90:6f:a8","7e:93:e0:ba:18:fe","f3:77:4c:80:70:fb","fd:ac:9f:35:6b:47"]
        b = random.choice(a)
        mac = "84:9c:08:01:ea:6f"

        subprocess.call(['ifconfig',intere1,'down'])
        subprocess.call(['ifconfig', intere1, 'hw','ether',b])
        subprocess.call(['ifconfig', intere1, 'up'])

        if entry_inter_rndom.get()=="eth0" :
            msg=messagebox.showinfo("WARNING",message="Successful")
        elif entry_inter_rndom.get()=="eth1" :
            msg=messagebox.showinfo("WARNING",message="Successful")
        elif entry_inter_rndom.get()=="eth2" :
            msg = messagebox.showinfo("WARNING", message="Successful")
        elif entry_inter_rndom.get() == "wlan0":
            msg = messagebox.showinfo("WARNING", message="Successful")
        elif entry_inter_rndom.get() == "wlan0":
            msg=messagebox.showinfo("WARNING",message="Successful")
        else :
            msg1 = messagebox.showinfo("ERROR", message="Please Change Interface")
            msg2 = messagebox.showinfo("WARNING", message="Example : eth_ , tun_ , wlan_")




    buton5 = tk.Button(form2,font='italic 12 bold', text='Rondom Mac Adres', fg='white', bg='blue', command=inter1)
    buton5.place(x=360, y=250)

    form2.mainloop()

def ipveri():

         form.destroy()
         form3 = tk.Tk()
         form3.title("VenomAge")
         form3.geometry("600x400")
         form3.resizable(True, True)

         var = messagebox.showinfo("Warning ", "IP Changer Starting")

         label1 = tk.Label(form3, font='italic 17 bold', text="IP Changer")
         label1.pack()

         label2 = tk.Label(form3, font='italic 10 bold' ,text="Interface :")
         label2.place(x=10, y=50)

         label3 = tk.Label(form3, font='italic 10 bold' , text="IP Address :")
         label3.place(x=10, y=90)

         label3 = tk.Label(form3,  font='italic 10 bold' ,text="Netmask Address:")
         label3.place(x=10, y=130)

         label4= tk.Label(form3, fg='red', text="eth0" )
         label4.place(x=150, y=50)

         label11 = tk.Label(form3, font='italic 7',text="**This is the demo version which is still under development and improvement.**")
         label11.place(x=65, y=373)

         entry_ip = tk.Entry(form3)
         entry_ip.place(x=150, y=90)

         entry_netmas = tk.Entry(form3)
         entry_netmas.place(x=150, y=130)

         def ipchan():

             ipad = str(entry_ip.get())
             netmas = str(entry_netmas.get())

             subprocess.call(['ifconfig', 'eth0', ipad , 'netmask' , netmas])


             if entry_netmas.get() == "255.255.255.0":
                 msg = messagebox.showinfo("WARNING", message="Successful")
             elif entry_netmas.get() == "255.255.0.0":
                 msg = messagebox.showinfo("WARNING", message="Successful")
             elif entry_netmas.get() == "255.0.0.0":
                 msg = messagebox.showinfo("WARNING", message="Successful")
             elif entry_netmas.get() == "255.255.255.0":
                 msg = messagebox.showinfo("WARNING", message="Successful")
             else:

                 msg1 = messagebox.showinfo("ERROR", message="Please enter value in netmask range")
                 msg2 = messagebox.showinfo("WARNING", message="Example : 255.255.255.0 , 255.255.0.0 , 255.0.0.0")





         buton5 = tk.Button(form3, font='italic 12 bold', text='Changer', fg='white', bg='blue', command=ipchan)
         buton5.place(x=240, y=180)

         form3.mainloop()

def localobj():

    form.destroy()
    form4 = tk.Tk()
    form4.title("VenomAge")
    form4.geometry("800x400")
    form4.resizable(True, True)

    var = messagebox.showinfo("Warning ", "**This Demo Currently Unavailable")

    label11 = tk.Label(form4, font='italic 13 bold ',fg='red', text="**This is the DEMO version which is still under development and improvement.**")
    label11.place(x=5, y=173)

buton2=tk.Button(form,font='italic 14 bold',text='Ip Address Changer',fg='white',bg='blue',command=ipveri)
buton2.pack(padx=30,pady=40)

buton=tk.Button(form,font='italic 14 bold',text='Mac Changer',fg='white',bg='blue',command=mac_veri)
buton.pack(padx=10 , pady=40)

buton3=tk.Button(form,font='italic 14 bold',text='Local Network Scanner',fg='white',bg='blue',command=localobj)
buton3.pack(padx=10,pady=40)

form.mainloop()
