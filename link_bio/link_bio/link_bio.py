import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.styles import styles



class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.vstack(
            header(),
            links(),
            margin_y = styles.Spacer.MEDIUM.value,
            width = styles.MAX_WIDTH,
        ),
        footer()
    )



app = rx.App(
    styles=styles.BASE_STYLE,
)
app.add_page(index)