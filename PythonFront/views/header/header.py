import reflex as rx
from PythonFront.components.link_icons import links_icons
from PythonFront.components.info_text import info_text
import PythonFront.styles.styles as styles
from PythonFront.styles. colors import TextColors as TextColor
from PythonFront.styles. colors import Colors as Color

def header()-> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                fallback="BC", 
                size='5',
                src="/logo 2.jfif",
                color=TextColor.BODY.value,
                bg=Color.CONTENT.value,
                padding="2px",
                border_color=Color.PRIMARY.value
                ),
            rx.vstack(
                rx.heading(
                    "Brayan Correa", 
                    size="6",
                    color=TextColor.HEADER.value,
                    font_family="Poppins_Bold"
                ),
                rx.text(
                    "@DevRyanx",
                    margin_top=styles.Spacer.ZERO.value,
                    color=TextColor.BODY.value
                ),
                rx.hstack(
                    links_icons("icons/x-twitter.svg","https://twitter.com/DevRyanx"),
                    links_icons("icons/facebook.svg","https://www.facebook.com/brayan.correah"),
                    links_icons("icons/instagram.svg","https://www.instagram.com/cbrayan_12?igsh=OTB4Nm5nNHVsaWsy"),
                    links_icons("icons/linkedin.svg","https://www.linkedin.com/in/brayan-correa-84a477291/"),
                    spacing="4"
                ),
                align_items="start",
            ),
            spacing="6"
        ),
        rx.flex(
            info_text("0","Años de experiencia."),
            rx.spacer(),
            info_text("Estudiante","Ing.Sistema."),
            rx.spacer(),
            info_text("1","Aplicaciones creadas."),
            rx.spacer(),
            width="100%"
        ),
        rx.text(
            f""" Como estudiante del cuarto semestre de Ingeniería de Sistemas,
                me lanzo con fervor hacia la maestría en el vasto mundo de la programación y 
                la ciberseguridad. No me conformo con los límites de las aulas universitarias; 
                ansío más, sediento de saber, y me lanzo a la vorágine de cursos y 
                talleres que desafían mis límites en cada paso que doy.""",
                color=TextColor.BODY.value
        ),
        spacing="6",        
        align_items="start"       
    )