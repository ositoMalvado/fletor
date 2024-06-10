# ResponsiveColumn.py
import flet as ft
from .ResponsiveControl import ResponsiveControl
from .ResponsiveRow import ResponsiveRow

class ResponsiveColumn(ft.Column):
    def __init__(self, controls: list=[], expands: list=[], debug: str=False, expand: bool=True, **kwargs):
        super().__init__(**kwargs)
        self.expands = expands if expands else [1] * len(controls)
        self.controls = [
            ResponsiveControl(content=control, expand=self.expands[i], debug=debug)
            for i, control in enumerate(controls)
        ]
        self.expand = expand
        self.spacing = 0

def main(page: ft.Page):
    page.add(
        ResponsiveColumn(
            controls=[
                ft.Text("Hello, World!"),
                ft.Text("Goodbye, World!"),
                ft.Text("Hello, World!"),
            ],
            expands=[2, 1, 1],
            debug=True
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
