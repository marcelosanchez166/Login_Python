
from tkinter import messagebox
import mysql.connector
import pymysql
# import Main
# from Main import *


class DataBase():
    def __init__(self):
        try:
            self.connec = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='',
                db='logueo'
            )
            if self.connec.is_connected():
                #messagebox.showinfo("INFO", "Estamos conectados ")
                #print("Estamos conectados")
                # infoserver=connection.get_server_info()
                # print(infoserver)
                self.cursor = self.connec.cursor()
        except:
            messagebox.showerror("Error", "Error en la Conexion a la BD")

        # finally:
        #           if self.connec.is_connected():
        #                     self.connec.close()
        #                     print("Conexion finalizada ")

        # self.conec=pymysql.connect(
        #           host='localhost',
        #           user='root',
        #           password='',
        #           db='torne_futbol'
        # )
        # self.cursor=self.conec.cursor()
        # print("Estamos conectados")

    # def comprobar(self):
    #           if self.conexion==True:
    #                     print("Conectados")
    #                     messagebox.showinfo("INFO", "Estamos conectados")
    #           else:
    #                     messagebox.showerror("Erro", "Lo sentimos no fue posible conectar")


Cone = DataBase()
