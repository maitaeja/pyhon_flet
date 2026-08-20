import flet as ft
from formulario.form_maestro_desing import FormularioMaestroDesing
import os
import ssl
from config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA



# Arreglo para el error de certificados (SSL)
try:
    ssl._create_default_https_context = ssl._create_unverified_context
except AttributeError:
    pass
#------------------------------------------------------------------------------


def main(page: ft.Page):
    page.title = "Integridad y Corrosión"
    page.padding = 0    # Elimina bordes blancos innecesarios para que todo encaje perfecto  
    page.spacing=0
    app = FormularioMaestroDesing(page)     # Instanciamos el diseño maestro completo
    page.add(app)
    page.update()

if __name__ =="__main__":
    port = int(os.environ.get("PORT", 8080))
    ft.app(target=main,
           #view = ft.AppView.WEB_BROWSER,
           #host = "0.0.0.0",
           #port = port
           )

