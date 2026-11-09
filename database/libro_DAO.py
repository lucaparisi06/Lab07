from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def get_libri(self, biblioteca, genere):

        conn = DBConnect.get_connection()
        cursore = conn.cursor()
        valori = []
        query = f'''SELECT * FROM libro WHERE 1=1'''
        if biblioteca is not None:
            query += ''' AND id_biblioteca = %s'''
            valori.append(biblioteca)
        if genere is not None:
            query += ''' AND genere = %s'''
            valori.append(genere)

        cursore.execute(query, valori)

        risultati = cursore.fetchall()
        lista_libri = []

        for riga in risultati:
            libro = Libro(riga[0], riga[1], riga[2], riga[3], riga[4], riga[5])
            lista_libri.append(libro)

        cursore.close()
        conn.close()

        return lista_libri

    def get_generi(self):
        conn = DBConnect.get_connection()
        cursore = conn.cursor()

        query = "SELECT DISTINCT genere FROM libro"

        cursore.execute(query)
        risultati = cursore.fetchall()

        lista_generi = []

        for riga in risultati:
            lista_generi.append(riga[0])

        cursore.close()
        conn.close()

        return lista_generi