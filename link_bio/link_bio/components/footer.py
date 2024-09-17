import reflex as rx

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="favicon.ico",
        ),
        rx.text(
            "Made with Reflex",
            size="md",
        ),
        margin_top="20px",
        align_items="center",
        justify_content="center", 
    )