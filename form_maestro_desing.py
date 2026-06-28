#Necesito ayuda con este codigo, estoy aprendiendo a programar. No puedo hacer que parezca el texto en el panel superior
#si alguien lee esto y me puede ayudar se lo agradezco
#saludos


import flet as ft
from config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA
import util.util_imagenes as util_img

##################################################################################################################################################

class FormularioMaestroDesing(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.ventana = page
        self.config_window()
        #self.texto_barra_superior()
        self.paneles()
        self.barra_lateral_i()
        self.barra_lateral_d()
        self.panel_maestro()
        
        
    

##################################################################################################################################################

    def config_window(self):
        self.ventana.title = "Integridad y Corrosión"
        w, h= 1024, 600
        self.ventana.window.width = w
        self.ventana.window.height = h
        self.ventana.padding = 0
        

##################################################################################################################################################

    def texto_barra_superior(self):
        return ft.Row(
            controls=[
                ft.Icon(
                    icon="menu_book",
                    color="white",
                    size=25,
                ),
                ft.Text(
                    "TML - Thickness Measurement Location",
                    color="white",
                    weight="bold",
                    size=20
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
        )
                                
    def paneles(self):
        self.barra_superior = ft.Container(
            content=self.texto_barra_superior(),
            bgcolor = COLOR_BARRA_SUPERIOR,
            height=  50,
        )
        
    def barra_lateral_i(self):
        self.barra_lateral_i = ft.Container(
            bgcolor = COLOR_MENU_LATERAL,
            width = 200,
            height=800
        )

    def barra_lateral_d(self):
        self.barra_lateral_d = ft.Container(
        bgcolor = COLOR_CUERPO_PRINCIPAL,
        expand= 1,
        )
    
    def panel_maestro(self):
        self.content=ft.Column(
            expand=True,
            spacing=0,
            controls=[
                self.barra_superior,
                ft.Row(
                    expand=True,
                    spacing=0,
                    controls= [
                    self.barra_lateral_i,
                    self.barra_lateral_d
                    ],
                )
            ],
            )


        
        
