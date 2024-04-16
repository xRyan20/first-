import reflex as rx
import PythonFront.styles.styles as styles
from PythonFront.styles. colors import TextColors as TextColor
from PythonFront.styles. colors import Colors as Color

def info_text(title: str,body:str) -> rx.Component:
    return rx.box(
        rx.text(
            title, 
            font_weight="bold", 
            color=Color.PRIMARY.value, 
            as_="span"
        ),
        f" {body}",
        font_size=styles.Spacer.MEDIUM.value,
        color=TextColor.BODY.value
    )