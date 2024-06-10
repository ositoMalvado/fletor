import fletor as ftor
import flet as ft
from flet_july.Widgets.DateTimePickerButton import TimePickerButton, DateTimePickerButton, DatePickerButton

def main(page: ft.Page):
    page.add(
        ftor.ResponsiveRow(
            controls=[
                ftor.ResponsiveColumn(
                    [
                        ftor.ResponsiveRow(
                            [
                                TimePickerButton(),
                                DateTimePickerButton(),
                                DatePickerButton(),
                            ],
                            expands=[1, 1, 1],
                        ),
                        ft.Text("Goodbye, World!"),
                        ft.Text("Hello, World!"),
                    ],
                    expands=[1, 1, 1],
                ),
                ftor.ResponsiveColumn(
                    [
                        ftor.ResponsiveControl(ft.Text("Hello, World!")),
                        ftor.ResponsiveControl(ft.Text("Goodbye, World!")),
                        ftor.ResponsiveControl(ft.Text("Hello, World!")),
                    ],
                    expands=[1, 1, 1],
                )
            ],
            expands=[1, 1, 1],
            expand=4
        )
    )


ft.app(target=main)