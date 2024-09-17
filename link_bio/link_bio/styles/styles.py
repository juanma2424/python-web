import reflex as rx
from enum import Enum

# constants
MAX_WIDTH = "100%"

#sizes
class Spacer(Enum):
    SMALL = "0.5em"
    MEDIUM = "1em"
    BIG = "2em"

#styles

BASE_STYLE = {
    rx.button:{
        "width": "100%",
        "height": "100%",
    },
}

# 
button_title_style = dict(
    bg="green",
)

button_body_style = dict(
    bg="red",
)

title_style= dict(
    size="lg",
    width="100%",
    padding_top=Spacer.MEDIUM.value,
)