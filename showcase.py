import fletor as ftor
import flet as ft

def main(page: ft.Page):
    page.add(
        ftor.ResponsiveRow(
            controls=[
                ft.Text("Hello, World!"),
                ft.Text("Goodbye, World!"),
                ft.Text("Hello, World!"),
            ],
            debug=True
        )
    )


ft.app(target=main)