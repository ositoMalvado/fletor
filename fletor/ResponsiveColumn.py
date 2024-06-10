# ResponsiveColumn.py
import flet as ft
from .ResponsiveControl import ResponsiveControl

class ResponsiveColumn(ft.Column):
    def __init__(self, controls: list=[], expands: list=[], debug:bool=False, expand:bool=True, **kwargs):
        super().__init__(**kwargs)
        self.controls = [
            ResponsiveControl(content=control, expand=expands[i], debug=debug)
            for i, control in enumerate(controls)
        ]
        self.expands = expands
        self.expand=expand
        self.spacing=0

def main(page: ft.Page):
    page.add(
        ResponsiveColumn(
            controls=[
                ft.Text("Hello, World!"),
                ft.Text("Goodbye, World!"),
                ft.Text("Hello, World!"),
            ],
            expands=[2, 1, 1],
        )
    )

if __name__ == "__main__":
    ft.app(target=main)