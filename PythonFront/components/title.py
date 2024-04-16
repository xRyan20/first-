import reflex as rx
import PythonFront.styles.styles as styles

def title(text: str) -> rx.Component:
    return rx.heading(
        text,
        size="6",
        style=styles.title_style
    )