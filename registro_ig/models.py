import sqlite3
from config import *
from registro_ig.conexion import Conexion

def select_all():
    connect = Conexion("select id,date,concept,quantity from movements order by date;")

   

    filas = connect.res.fetchall()#capturo las filas de datos
    columnas= connect.res.description#capturo los nombres de columnas

    #objetivo crear una lista de diccionario con filas y columnas

    
    resultado =[]#lista para guadar diccionario
   
    for fila in filas:
        dato={}#diccionario para cada registro
        posicion=0#posicion de columna

        for campo in columnas:
            dato[campo[0]]=fila[posicion]
            posicion += 1
        resultado.append(dato)


    connect.con.close()
    return resultado

def insert(registro):
    connectInsert = Conexion("insert into movements(date,concept,quantity) values(?,?,?)",registro)

   

    connectInsert.con.commit() #funcion que registra en la base de datos finalmente

    connectInsert.con.close()

def select_by(id):

    connectSelectby = Conexion(f"select id,date,concept,quantity from movements WHERE id={id};")
  
    resultado = connectSelectby.res.fetchall()
    connectSelectby.con.close()

    return resultado[0]
    
def delete_by(id):
    connectDeleteby = Conexion(f"DELETE FROM movements WHERE id = {id}")

    connectDeleteby.con.commit()
    connectDeleteby.con.close()

