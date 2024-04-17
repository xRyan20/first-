import reflex as rx
import datetime
import PythonFront.styles.styles as styles
from PythonFront.styles. colors import TextColors as TextColor

def futter()-> rx.Component:
    return rx.center(
        rx.vstack(
            rx.image(
                src="/logo.jpg",
                width="50px",
                height="auto",
                border_radius="50px 50px",
                border="2px solid #555",
            ),
        ),
        rx.text(
            f"©2022-{datetime.date.today().year} RyanDev by Brayan Correa v1",
            font_size=styles.Spacer.MEDIUM.value,
            margin_top=styles.Spacer.ZERO.value   
        ),
        margin_bottom=styles.Spacer.BIG.value,
        padding_bottom=styles.Spacer.BIG.value,
        padding_x=styles.Spacer.BIG.value,
        spacing='2',
        color=TextColor.FOOTER.value
    )