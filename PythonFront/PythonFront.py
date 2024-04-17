import reflex as rx
from PythonFront.components.navbar import navbar
from PythonFront.views.header.header import header
from PythonFront.views.links.links import links
from PythonFront.components.Futter import futter
import PythonFront.styles.styles as styles

class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=styles.Spacer.BIG.value,
                padding=styles.Spacer.BIG.value,
            )    
        ),
        futter()
    )
app = rx.App(
    style=styles.BASE_STYLE
)
app.add_page(index,
             title="RyanDev",
             description="Hola, mi nombre es Brayan Correa. Soy estudiante de cuarto semestre de ingeneria, y este es mi portafolio.",
             image="/logo 2.jfif")

