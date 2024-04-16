import reflex as rx
from PythonFront.components.links_button import links_button
from PythonFront.components.title import title

def links()-> rx.Component:
    return rx.center(
        rx.vstack(
            title("Contacto"),
            links_button("Youtube",
                         "Esto es un testeo de para saber si funciona 12345679",
                         "icons/youtube.svg",
                         "https://www.youtube.com/watch?v=n2YrGsXJC6Y&list=PLNdFk2_brsRdgQXLIlKBXQDeRf3qvXVU_&index=4&t=5809s"),
            links_button("Email",
                         "briancor2012@gmail.com",
                         "icons/envelope-regular.svg",
                         "briancor2012@gmail.com"
                         ),
            links_button("instagram",
                         "Esto es un testeo de para saber si funciona 12345679",
                         "icons/instagram.svg",
                         "https://www.instagram.com/cbrayan_12?igsh=OTB4Nm5nNHVsaWsy"),
            title("Proyectos"),
            links_button("Proyecto1",
                         "Esto es un testeo de para saber si funciona 12345679",
                         "icons/briefcase-solid.svg",
                         "https://www.youtube.com/watch?v=n2YrGsXJC6Y&list=PLNdFk2_brsRdgQXLIlKBXQDeRf3qvXVU_&index=4&t=5809s"),
            links_button("Proyecto2",
                         "Esto es un testeo de para saber si funciona 12345679",
                         "icons/briefcase-solid.svg",
                         "https://web.whatsapp.com/"
                         ),
            links_button("Proyecto3",
                         "Esto es un testeo de para saber si funciona 12345679",
                         "icons/briefcase-solid.svg",
                         "https://www.instagram.com/cbrayan_12?igsh=OTB4Nm5nNHVsaWsy"),             
            width="100%",
            spacing='3'
        )
    )