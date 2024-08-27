from nicegui import ui


def menu() -> None:
    # ui.link('Home', '/home').classes(replace='text-white text-bold')
    ui.button('Home', on_click=lambda: ui.navigate.to('/home'))
    ui.button('Tabela', on_click=lambda: ui.navigate.to('/table'))
    # ui.link('Tabela', '/table').classes(replace='text-white')
