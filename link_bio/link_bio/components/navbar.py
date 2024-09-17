import reflex as rx
from link_bio.styles import styles

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Link.bio",
            height="40px",
        ),
        position="sticky",
        bg="blue",
        padding="16px",
        z_index="999",
        top="0",
    )