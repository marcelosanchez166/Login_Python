from tkinter import *
from tkinter import ttk
"""Las ventanas emegentes no vienen con la biblioteca de tkinter hay que importarlas por aparte"""
from tkinter import messagebox

from tkinter import messagebox
import mysql.connector
import Conexion
from Conexion import *


class login():
    def __init__(self, raiz):
        self.raiz = raiz
        # self.raiz = Tk() #La quite porque esto me duplicaba las interfaces y como abajo lo tengo ya instanciado ya no hace falta
        self.raiz.title(" Login Para Usuarios ")
        #self.raiz.geometry("500x450")
        self.raiz.config(bg="#A9A9E9")
        # raiz.columnconfigure(1, weight=1)
        # raiz.rowconfigure(1, weight=1)

        LabelLogin = Label(self.raiz, text=" Login ")
        LabelLogin.grid(row=4, column=10, pady=15)
        LabelLogin.config(bg="#000000", fg="yellow", font=(
            'Lucida Sans', 36, 'bold'), borderwidth=0)


#           IMG Usuario Login
        self.imglogin = PhotoImage(file="2.png")
        self.LBlogueo = Label(self.raiz, image=self.imglogin)
        self.LBlogueo.grid(row=5, column=10,   pady=10, padx=100)
        # self.LBlogueo.config(bg="#000000", fg="white", font=('Lucida Sans', 12, 'bold'), borderwidth=0, activebackground='black')
        # self.LBlogueo.grid_propagate(0)

        self.Name = StringVar()
        self.password = StringVar()
#                   Etiquetas
        Labeluser = Label(self.raiz, text=" Usuario: ")
        Labeluser.grid(row=6, column=10)
        Labeluser.config(bg="#A11FFF", fg="black", font=(
            'Lucida Sans', 16, 'bold'), borderwidth=0)

        Labelpass = Label(self.raiz, text=" Password: ")
        Labelpass.grid(row=9, column=10)
        Labelpass.config(bg="#A11FFF", fg="black", font=(
            'Lucida Sans', 16, 'bold'), borderwidth=0)

        self.txtuser = Entry(self.raiz, textvariable=self.Name)
        self.txtuser.grid(row=7, column=10, padx=4, pady=8)
        self.txtuser.focus()

        self.txtpass = Entry(self.raiz, textvariable=self.password)
        self.txtpass.grid(row=10, column=10, padx=4, pady=8)
        self.txtpass.focus()

        """Boton para Logueo"""
        ingresarUsuarios = Button(self.raiz, text="Login", command=self.ValidarUser)
        ingresarUsuarios.grid(row=13,column=10, pady=5, padx=20)
        ingresarUsuarios.config(
            bg="#008B8B", fg="#191970", font=("Courier", 12, "italic"))


        """Boton para Registro"""
        RegistrarUser= Button(self.raiz, text="Registrarse", command=self.Registrar)
        RegistrarUser.grid(row=14,column=10, pady=5, padx=20 )
        RegistrarUser.config(
            bg="#008B8B", fg="#191970", font=("Courier", 12, "italic"))

    def ValidarUser(self):
        # Abrir y crear Conexion a la base de sql lite
        Conexion.Cone = DataBase()
        # Crear Puntero
        Conexion.Cone.cursor.execute("SELECT Usuario,Password FROM  login")
        # Variable para guardar lo extraido de la base con el select
        valoresextraidos = Conexion.Cone.cursor.fetchall()
        #print(valoresextraidos,"imprimir 1")
        list = []
        for (User, passwor) in valoresextraidos:

            list.append(User)
            list.append(passwor)
        print(list)
            # if list[0] ==self.txtuser.get() and list[1]==self.txtpass.get() :
        if self.txtuser.get() in list  and self.txtpass.get() in list :
            #print(list,"1")
            messagebox.showinfo("INFO", "Binvenido usuario ")
            self.txtuser.delete(0,END)
            self.txtpass.delete(0,END)
        else:
            messagebox.showinfo("Alert", "Usuario y/o contraseña incorrectos ") 
            self.txtuser.delete(0,END)
            self.txtpass.delete(0,END)

    def Registrar(self):
        #cursor.execute("INSERT INTO Equipos VALUES (NULL,?,?)", lista)
        Conexion.Cone = DataBase()
        lista=[self.txtuser.get(),self.txtpass.get()]
        """ConexionDB.Cone.cursor.execute("INSERT INTO Equipos VALUES (NULL,'" + NameEQ.get()+
        "','" + Capitan.get() +"')")"""
        #Conexion.Cone.cursor.execute("INSERT INTO Equipos VALUES (NULL,'" + NameEQ.get()+"')")
        if len(self.txtuser.get())!=0 and len(self.txtpass.get())!=0:
            #Los signos %s significan que alli va un campo, como en este caso son dos campos usuario y password, si fueran mas campos
#Se pondria la contidad correspondiente, EJE: pass, User, Addres, %s, %s, %s, EL null es porque la tabla tiene un id que esta autoincrementable
            Conexion.Cone.cursor.execute("INSERT INTO login VALUES (NULL,%s,%s)", lista)
            Conexion.Cone.connec.commit()
            messagebox.showinfo("INFO", "Usuario ingresado Exitosamente")
            self.txtuser.delete(0,END)
            self.txtuser.focus()
            self.txtpass.delete(0,END)
            self.txtpass.focus()
            Conexion.Cone.connec.close()
            

        else:
            messagebox.showinfo("Campos Vacios", "Los campos no puede quedar vacios")
            #self.NameEQ.set("")    ##Metodo .set para limpiar los entry
            self.txtuser.delete(0,END)
            self.txtuser.focus()
            self.txtpass.delete(0,END)
            self.txtpass.focus()


if __name__ == '__main__':
    raiz = Tk()
    instancialogin = login(raiz)
    raiz.mainloop()
