import reflex as rx
from link_bio.styles import styles

def title(text: str) -> rx.Component:
    return rx.heading(
        text,
        style = styles.title_style,
        )