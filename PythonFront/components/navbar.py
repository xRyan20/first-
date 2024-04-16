import reflex as rx
import PythonFront.styles.styles as styles
from PythonFront.styles. colors import Colors as Color

def navbar()->rx.Component:
    return rx.hstack(
        rx.box(
            rx.text("ryan", color=Color.SECONDARY.value,as_="span"),
            rx.text("dev",color=Color.PRIMARY.value,as_="span"),
            style=styles.navbar_title_style
        ),
        position="sticky",
        padding_x=styles.Spacer.DEFAULT.value,
        padding_y=styles.Spacer.SMALL.value,
        bg=Color.CONTENT.value,
        z_index="999",
        top="0"
    )
