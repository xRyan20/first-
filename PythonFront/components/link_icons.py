import reflex as rx
import PythonFront.styles.styles as styles

def links_icons(image: str, url: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            width=styles.Spacer.DEFAULT.value,
        ),
        href=url,
        is_external=True
    )