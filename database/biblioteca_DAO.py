from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def get_biblioteche(self):

        conn = DBConnect.get_connection()
        cursore = conn.cursor()

        query = """SELECT * FROM biblioteca"""
        cursore.execute(query)
        risultati = cursore.fetchall()

        lista_biblioteche = []
        for riga in risultati:
            biblioteca = Biblioteca(riga[0], riga[1], riga[2])
            lista_biblioteche.append(biblioteca)
        cursore.close()
        conn.close()
        return lista_biblioteche