import Tkinter
import telnetlib
from Tkinter import *

class mrr:
    def __init__(self,master):
        self.titulo = Label(text='Modem/Router-Restarter',fg="blue")
        self.titulo.pack(side=TOP)
        self.subtitulo= Label(text='Por Tomas Caram',fg="blue")
        self.subtitulo.pack(side=TOP)
        self.cambip = Button( text='Cambiar IP',fg="red",command = ip)
        self.cambip.pack(side= LEFT,padx=10,pady=10)
        self.reini = Button( text='Reiniciar Modem',command = reiniciar) 
        self.reini.pack(side= RIGHT,padx=10,pady=10)

#REINICIAR EL ROUTER
def reiniciar():
    sess=telnetlib.Telnet('10.0.0.2',23,2800)
    print 'Conectando...\n'
    try:
        sess.read_until('Login: ',5)
        print 'validando usuario...\n'
        sess.write('admin\n')
        print 'validando password...\n'
        sess.read_until('Password: ',5)
        sess.write('admin\n')
        print 'esperando respuesta...\n'
        sess.read_until('>',5)
        print 'reiniciando ADSL...\n'
        sess.write('reboot\n')
        print 'Reiniciando...\n'               
    except EOFError, socket.error:
        print time.strftime("%H:%M:%S  "),
        print 'Falla de Conexion con 10.0.0.2'
        #return None
    #return sess


#CABIAR LA IP
def ip():
    sess=telnetlib.Telnet('10.0.0.2',23,100)
    print 'Conectando...\n'
    try:
        sess.read_until('Login: ',5)
        print 'validando usuario...\n'
        sess.write('admin\n')
        print 'validando password...\n'
        sess.read_until('Password: ',5)
        sess.write('admin\n')
        print 'esperando respuesta...\n'
        sess.read_until('>',5)
        print 'reiniciando ADSL...\n'
        sess.write('adsl start\n')
        print 'Desconectando...\n'
        sess.read_until('>',5)
        sess.write('logout\n')                
    except EOFError, socket.error:
        print time.strftime("%H:%M:%S  "),
        print 'Falla de Conexion con 10.0.0.2'
        #return None
    #return sess


root =Tk()
root.title('M/R-R')
calc=mrr(root)
root.mainloop()

