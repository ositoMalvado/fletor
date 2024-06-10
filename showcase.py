import fletor as ftor
import flet as ft

def main(page: ft.Page):
    page.add(
        ftor.ResponsiveRow(
            controls=[
                ftor.ResponsiveColumn(
                    [
                        ft.Text("Goodbye, World!"),
                        ft.Text("Hello, World!"),
                    ],
                    expands=[1, 3],
                    debug=True
                ),
                ftor.ResponsiveColumn(
                    [
                        ftor.ResponsiveControl(ft.Text("Hello, World!")),
                        ftor.ResponsiveControl(ft.Text("Goodbye, World!")),
                        ftor.ResponsiveControl(ft.Text("Hello, World!")),
                    ],
                    debug=True
                )
            ],
            expands=[1, 4],
            expand=4,
            debug=True
        )
    )


ft.app(target=main)