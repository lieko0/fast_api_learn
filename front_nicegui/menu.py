from nicegui import ui


def menu() -> None:
    ui.link('Home', '/home').classes(replace='text-white')
    ui.link('Tabela', '/table').classes(replace='text-white')
    ui.link('B', '/b').classes(replace='text-white')
    ui.link('C', '/c').classes(replace='text-white')