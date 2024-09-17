import reflex as rx
from link_bio.styles import styles

def link_button(p_name:str, p_url:str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="a_arrow_up",
                ),
                rx.vstack(
                    rx.text(
                        p_name,                
                    ),
                    rx.text(
                        p_name,                
                    ),
                ),
            ),
        style=styles.button_title_style
        ),
        href=p_url,
        is_external=True,
        width="100%",
    )