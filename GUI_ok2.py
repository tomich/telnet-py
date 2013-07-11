import Tkinter
import telnetlib
import socket
from Tkinter import *

class mrr:
    def __init__(self,master):
        self.titulo = Label(text='Modem/Router-Restarter',fg="blue",font=("Arial", 16))
        self.titulo.pack(side=TOP)
        self.subtitulo= Label(text='Por Tomas Caram')
        self.subtitulo.pack(side=TOP)
        self.subtitulo2= Label(text='--------------')
        self.subtitulo2.pack(side=TOP)
        self.cambip = Button( text='Cambiar IP',fg="red",font=("Arial", 10),command = ip)
        self.cambip.pack(side= LEFT,padx=10,pady=10)
        self.reini = Button( text='Reiniciar Modem',font=("Arial", 10),command = reiniciar) 
        self.reini.pack(side= RIGHT,padx=10,pady=10)

#REINICIAR EL ROUTER
def reiniciar():
    var = StringVar()
    stato=Label(textvariable=var).pack()
    try:
        sess=telnetlib.Telnet('10.0.0.2',23,2800)        
        sess.read_until('Login: ',5)
        sess.write('admin\n')
        sess.read_until('Password: ',5)
        sess.write('admin\n')
        sess.read_until('>',5)
        sess.write('reboot\n')
        var.set('Reiniciando Modem...')             
    except socket.error,socket.gaierror:
        var.set('Falla de Conexion con 10.0.0.2')
        #return None
    #return sess


#CABIAR LA IP
def ip():
    var = StringVar()
    stato=Label(textvariable=var).pack()
    try:
        sess=telnetlib.Telnet('10.0.0.2',23,100)
        var.set('')
        sess.read_until('Login: ',5)
        sess.write('admin\n')
        sess.read_until('Password: ',5)
        sess.write('admin\n')
        sess.read_until('>',5)
        sess.write('adsl start\n')
        sess.read_until('>',5)
        sess.write('logout\n')
        var.set('Reiniciando ADSL...')
    except socket.error,socket.gaierror:
        var.set('Falla de Conexion con 10.0.0.2')
        #return None
    #return sess


root =Tk()
root.title('M/R-R')
calc=mrr(root)
root.mainloop()

