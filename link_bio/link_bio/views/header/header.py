import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(name="test", size="xl"),
        rx.text(
            "Name",
            size="xl",
        ),
        rx.text(
            "Bio",
            size="md",
        ),
        rx.text(
            "Location",
            size="md",
        ),
        align_items="center",
        justify_content="center", 
    )