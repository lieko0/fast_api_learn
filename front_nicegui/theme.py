from contextlib import contextmanager

from nicegui import app, ui

from front_nicegui.menu import menu


@contextmanager
def frame(navigation_title: str):
    """Custm pag fram to shre the same styling and behavior acrss all pages"""
    ui.colors(
        primary='#029b99',
        secondary='#4d6160',
        accent='#a39081',
        positive='#21ba45',
        negative='#c10015',
        warning='#f2a137',
        dark='#001f21',
        info='#31ccec',
    )
    with ui.header():
        ui.dark_mode().bind_value(app.storage.user, 'dark_mode')
        ui.checkbox().bind_value(app.storage.user, 'dark_mode').props(
            'color="lime" checked-icon="light_mode" unchecked-icon="dark_mode"'
        )
        ui.space()
        ui.label(navigation_title).classes('self-center')
        ui.space()
        with ui.row().classes('self-center'):
            menu()
    with ui.column().classes('justify-center self-center'):
        yield
