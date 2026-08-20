import flet as ft
import util.util_imagenes as util_img
from config import (
    COLOR_BARRA_SUPERIOR,
    COLOR_TEXTO_BARRA,
    COLOR_MENU_LATERAL,
    COLOR_MENU_CURSOR_ENCIMA,
    COLOR_MENU_ACTIVO,
    COLOR_TEXTO_MENU,
    COLOR_TEXTO_MENU_ACTIVO,
    COLOR_BORDE_ACTIVO,
    COLOR_AZUL_ACCENTO,
    COLOR_CUERPO_PRINCIPAL,
    COLOR_TARJETA_BG,
    COLOR_TEXTO_TITULO,
    COLOR_TEXTO_CUERPO,
    COLOR_CAJA_DESTACADA,
)

from vistas.vista_introduccion import IntroduccionView
from vistas.vista_definicion_punto import RegistroTmlView
from vistas.vista_tml import QueEsTMLView
from vistas.vista_objetivos_tml import ObjetivosTMLView
from vistas.vista_aspectos_clave_tml import AspectosClaveView
from vistas.vista_ubicacion_tml import UbicacionView
from vistas.vista_gestion_tml import GestionDatosView
from vistas.vista_consideracion_practica import ConsideracionPracticaView



##################################################################################################################################################

class FormularioMaestroDesing(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.ventana = page
        self.menu_expandido = True
        self.config_window()
        self.texto_barra_superior()
        self.panel_superior()
        self.panel_lateral_i()
        self.panel_lateral_d()
        self.panel_maestro()
        self.vistas = self.crear_vistas()   # Diccionario que mapea cada botón de la imagen con su vista
    

##################################################################################################################################################

    def config_window(self):
        self.ventana.title = "Integridad y Corrosión"
        w, h= 1024, 600
        self.ventana.window.width = w
        self.ventana.window.height = h
        self.ventana.padding = 0
        

##################################################################################################################################################

    def alternar_menu(self, e):
        """Alterna el ancho del menú entre 310px (completo) y 60px (solo íconos)."""
        self.menu_expandido = not self.menu_expandido
        
        # Cambiar el ancho del contenedor del menú
        self.barra_lateral_i.width = 310 if self.menu_expandido else 60
        
        # Ocultar o mostrar los textos de los botones
        for texto_control in self.sidebar_texts.values():
            texto_control.visible = self.menu_expandido

        self.barra_lateral_i.update()

##################################################################################################################################################

    def texto_barra_superior(self):
        return ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.Icons.MENU,
                    icon_color=COLOR_TEXTO_BARRA,
                    icon_size=25,
                    tooltip="Colapsar / Expandir menú",
                    on_click=self.alternar_menu,
                ),

                ft.Text(
                    value="TML - Thickness Measurement Location",
                    color=COLOR_TEXTO_BARRA,
                    weight=ft.FontWeight.BOLD,
                    size=20,
                    
                ),

                ft.Container(expand=True),

                ft.Text(
                    value="Plan de Inspección",
                    color=COLOR_TEXTO_BARRA,
                    #weight=ft.FontWeight.BOLD,
                    size=16,
                    text_align=ft.TextAlign.END
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,    
        )


    def panel_superior(self):
        self.barra_superior = ft.Container(
            content=self.texto_barra_superior(),
            bgcolor = COLOR_BARRA_SUPERIOR,
            height=  50,
            padding=ft.Padding(20, 0, 30, 0)
        )

##################################################################################################################################################

    def texto_barra_lateral_i(self):
        buttons_info = [
            ("Introducción a TML", ft.Icons.MENU_BOOK),
            ("Definición de punto", ft.Icons.ADJUST_SHARP),
            ("¿Qué es un TML?", ft.Icons.LAYERS),
            ("Objetivos de los TML's", ft.Icons.SETTINGS),
            ("Aspectos clave de los TML's", ft.Icons.ASSIGNMENT),
            ("Ubicación de los TML's", ft.Icons.PLACE),
            ("Gestión de datos (CML vs. TML)", ft.Icons.DNS_ROUNDED),
            ("Consideración práctica", ft.Icons.INFO_OUTLINE_ROUNDED)
        ]
        lista_botones = []
        lista_botones.append(ft.Container(height=30))
        self.sidebar_buttons = {}  # Diccionario para guardar referencias de los botones
        self.sidebar_texts = {}
        self.sidebar_icons = {}

        for texto, icono_flet in buttons_info:
        # Control de Texto separado para poder ocultarlo al colapsar
            txt_control = ft.Text(
                value=texto,
                weight=ft.FontWeight.W_600,
                color=COLOR_TEXTO_BARRA,  #ffffff (blanco)
                size=16,
                visible=self.menu_expandido,
                overflow=ft.TextOverflow.CLIP,
            )
            icon_control= ft.Icon(
                icono_flet,
                size=28,
                color=COLOR_TEXTO_BARRA,  #ffffff (blanco)
            )
        # Creamos cada botón como Container
            boton = ft.Container(
                border=ft.Border(left=ft.BorderSide(3, "transparent")),
                padding=ft.Padding(left=15, top=12, right=15, bottom=12),
                bgcolor=COLOR_MENU_LATERAL,
                content=ft.Row(
                    controls=[icon_control, txt_control],
                    alignment=ft.MainAxisAlignment.START,
                    spacing=15,
                ),
                
                # Acción al hacer clic (aquí puedes redirigir a una función encargada del cambio de pantalla)
                on_click=lambda e, txt=texto: self.cambiar_pantalla(txt),
                ink = True,
            )
        
            # Guardamos el botón en la lista y en el diccionario de la clase
            lista_botones.append(boton)
            self.sidebar_buttons[texto] = boton
            self.sidebar_texts[texto] = txt_control
            self.sidebar_icons[texto] = icon_control

        # 2. Agregamos todos los botones generados a los controles del contenedor lateral
        # (Asegúrate de que self.menu_lateral esté definido previamente como un ft.Column)
        
        self.columna_menu.controls.extend(lista_botones)
    

    def panel_lateral_i(self):
        self.columna_menu = ft.Column(spacing=5, scroll=ft.ScrollMode.AUTO)
        self.texto_barra_lateral_i()

        self.barra_lateral_i = ft.Container(
            content= self.columna_menu,
            bgcolor = COLOR_MENU_LATERAL,
            width = 310,
            animate=ft.Animation(300, ft.AnimationCurve.EASE_IN_OUT),  # Animación suave de cambio de ancho
            height=800,
        )
        return self.barra_lateral_i


    def panel_lateral_d(self):
        self.barra_lateral_d = ft.Container(
        bgcolor = COLOR_CUERPO_PRINCIPAL,
        expand= True,
        height=800,
        padding = 30
        )

##################################################################################################################################################
    # ----------------------------------------------------------------------- #
    #                       MAPEADO DE LAS 8 VISTAS                           #
    # ----------------------------------------------------------------------- #


    def crear_vistas(self):
        return {
            "Introducción a TML": IntroduccionView(),
            "Definición de punto": RegistroTmlView(),
            "¿Qué es un TML?": QueEsTMLView(),
            "Objetivos de los TML's": ObjetivosTMLView(),
            "Aspectos clave de los TML's": AspectosClaveView(),
            "Ubicación de los TML's": UbicacionView(),
            "Gestión de datos (CML vs. TML)": GestionDatosView(),
            "Consideración práctica": ConsideracionPracticaView(),
        }

    def cambiar_pantalla(self, nombre_pantalla):
        for texto_boton, boton in self.sidebar_buttons.items():
            es_activo = (texto_boton==nombre_pantalla)
            boton.bgcolor = COLOR_MENU_ACTIVO if es_activo else COLOR_MENU_LATERAL

            border_color= COLOR_BORDE_ACTIVO if es_activo else "transparent"
            boton.border = ft.Border(left=ft.BorderSide(3, border_color))

            #Color del texto
            if texto_boton in self.sidebar_texts:
                self.sidebar_texts[texto_boton].color = COLOR_TEXTO_BARRA
                self.sidebar_texts[texto_boton].update()

            if texto_boton in self.sidebar_icons:
                self.sidebar_icons[texto_boton].color = COLOR_TEXTO_BARRA
                self.sidebar_icons[texto_boton].update()

            boton.update()

            #Cambio de vista a la derecha
            if nombre_pantalla in self.vistas:
                self.barra_lateral_d.content = self.vistas[nombre_pantalla]
                if self.barra_lateral_d.page:
                    self.barra_lateral_d.update()


##################################################################################################################################################
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


        
        
 
