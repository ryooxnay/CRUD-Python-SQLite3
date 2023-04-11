import sqlite3
#'
class Comunicacion():
    def __init__(self):
        self.conexion = sqlite3.connect("base_datos1Python.db")
    def insertar_datos(self, nombre, edad, correo, telefono):
        cursor = self.conexion.cursor()
        bd = '''INSERT INTO datos (NOMBRE, EDAD, CORREO, TELEFONO)
        VALUES('{}', '{}', '{}', '{}')'''.format(nombre, edad, correo, telefono)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()
    def mostrar_datos(self):
        cursor = self.conexion.cursor()
        bd = "SELECT * FROM datos"
        cursor.execute(bd)
        datos = cursor.fetchall()
        return datos
    def elimina_datos(self, nombre):
        cursor = self.conexion.cursor()
        bd = '''DELETE FROM datos WHERE NOMBRE = '{}' '''.format(nombre)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()
    def actualiza_datos(self, ID, nombre, edad, correo, telefono):
        cursor = self.conexion.cursor()
        bd = '''UPDATE datos SET NOMBRE = '{}', EDAD = '{}', CORREO = '{}', TELEFONO = '{}' 
        WHERE ID = '{}' '''.format(nombre, edad, correo, telefono, ID)
        cursor.execute(bd)
        dato = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        return dato

