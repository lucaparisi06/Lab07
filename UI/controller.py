import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # INIZIALIZZAZIONE DROPDOWN
    def inizializza(self):
        self.popola_dropdown_biblioteche()
        self.popola_dropdown_generi()

    # POPOLA DROPDOWN BIBLIOTECHE
    def popola_dropdown_biblioteche(self):
        biblioteche = self._model.get_biblioteche()

        self._view.dd_biblioteca.options.clear()

        self._view.dd_biblioteca.options.append(
            ft.DropdownOption(key="", text="Nessun filtro")
        )

        for biblioteca in biblioteche:
            self._view.dd_biblioteca.options.append(
                ft.DropdownOption(
                    key=str(biblioteca.id),
                    text=biblioteca.nome
                )
            )

    # POPOLA DROPDOWN GENERI
    def popola_dropdown_generi(self):
        generi = self._model.get_generi()

        self._view.dd_genere.options.clear()

        self._view.dd_genere.options.append(
            ft.DropdownOption(key="", text="Nessun filtro")
        )

        for genere in generi:
            self._view.dd_genere.options.append(
                ft.DropdownOption(key=genere, text=genere)
            )

    # CALLBACK DROPDOWN BIBLIOTECA
    def seleziona_biblioteca(self, e):
        valore = e.control.value

        if valore is None or valore == "":
            self.biblioteca_selezionata = None
        else:
            self.biblioteca_selezionata = int(valore)

    # CALLBACK DROPDOWN GENERE
    def seleziona_genere(self, e):
        valore = e.control.value

        if valore is None or valore == "":
            self.genere_selezionato = None
        else:
            self.genere_selezionato = valore

    # AZIONE: MOSTRA LIBRI
    def mostra_libri(self, e):
        libri = self._model.get_libri_filtrati(
            self.biblioteca_selezionata,
            self.genere_selezionato
        )

        self._view.lista_libri.controls.clear()

        if len(libri) == 0:
            self._view.show_alert("Nessun libro trovato con i filtri selezionati")
        else:
            self._view.lista_libri.controls.append(
                ft.Text(f"Libri trovati: {len(libri)}")
            )

            for libro in libri:
                self._view.lista_libri.controls.append(
                    ft.Text(str(libro))
                )

        self._view.update()

