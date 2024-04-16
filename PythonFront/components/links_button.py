import reflex as rx
import PythonFront.styles.styles as styles

def links_button(text: str, body:str, image: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=styles.Spacer.BIG.value,
                    heigth=styles.Spacer.BIG.value,
                    margin=styles.Spacer.MEDIUM.value
                ),
                rx.vstack(
                    rx.text(text, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    spacing="1",
                    align_items="start",
                    margin=styles.Spacer.ZERO.value
                )
            )
        ),
        href=url,
        is_external=True,
        width="150%"
        )