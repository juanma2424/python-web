import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title

def links() -> rx.Component:

    return rx.vstack(   
        title("Links"),
        link_button("c11231234123","https://github.com/juanma2424"),
        link_button("c2","https://github.com/juanma2424"),
        link_button("c3","https://github.com/juanma2424"),
        link_button("c4","https://github.com/juanma2424"),
        width="100%",
    )

