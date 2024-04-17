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
                    rx.text(
                        text, 
                        size='1',
                        style=styles.button_title_style),
                    rx.text(
                        body,
                        size='1',
                        style=styles.button_body_style),
                    spacing="1",
                    align_items="start",
                    padding_y=styles.Spacer.SMALL.value,
                    padding_right=styles.Spacer.SMALL.value,
                ),
                align="center",
                width="100%"
            )
        ),
        href=url,
        is_external=True,
        width="150%"
        )