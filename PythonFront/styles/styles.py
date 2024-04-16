from enum import Enum
import reflex as rx
from .colors import Colors as Color
from .colors import TextColors as TextColor

#Constantes
MAX_WIDTH="600px"


#Sizes
class Spacer(Enum):
    ZERO= "0px !important" 
    SMALL="0.5em"
    MEDIUM="0.9em"
    DEFAULT="1em"
    BIG="2em"

#Styles

BASE_STYLE = {
    "font_family":"Poppins-Light",
    "background_color": Color.BACKGROUND.value,
    rx.button: {
        "width":"100%",
        "height":"100%",
        "display":"block",
        "padding":Spacer.SMALL.value,
        "border_radius": Spacer.DEFAULT.value,
        "background_color": Color.CONTENT.value,
        "_hover":{
            "background_color": Color.SECONDARY.value,
        }
    },
    rx.link:{
        "text_decoration":"none",
        "_hover":{},

    }
}

STYLESHEETS = {
    "https://fonts.googleapis.com/css2?family=Poppins:wgth@300;600&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wgth@500&display=swap"
}

button_title_style = dict(
    font_family="Poppins-Light 300",
    font_size=Spacer.DEFAULT.value,
    color=TextColor.HEADER.value
)
button_body_style = dict(
    font_size=Spacer.MEDIUM.value,
    color=TextColor.BODY.value
)
title_style = dict(
    font_family="Poppins-Bold 700",
    width="100%",
    padding_top=Spacer.DEFAULT.value,
    color=TextColor.HEADER.value
)
navbar_title_style = dict(
   font_family="Comfortaa-Medium 500",
   font_size="1.5em"
)