import flet.canvas as cv
import flet as ft
from collections import namedtuple

class ResponsiveControl(cv.Canvas):
    def __init__(self, content= None, resize_interval=1, on_resize=None, expand=1, padding:ft.padding=0, margin:ft.margin=0, debug:str=False, **kwargs):
        super().__init__(**kwargs)
        self.content = ft.Container(
                content=content,
                padding=5 if debug else padding,
                alignment=ft.alignment.center,
                margin=5 if debug else margin,
                bgcolor=ft.colors.with_opacity(0.2, debug) if debug else None,
                border=ft.border.all(1, debug) if debug else None,
        )
        self.expand = expand
        self.resize_interval = resize_interval
        self.resize_callback = on_resize
        self.on_resize = self.__handle_canvas_resize
        self.size = namedtuple("size", ["width", "height"], defaults=[0, 0])

    def __handle_canvas_resize(self, e):
        """
        Called every resize_interval when the canvas is resized.
        If a resize_callback was given, it is called.
        """
        pass


def main(page: ft.Page):
    s1 = ResponsiveControl(content=ft.Text("Hello, World!"), expand=1)
    s2 = ResponsiveControl(content=ft.Text("Hello, World!"), expand=3)
    page.add(
        ft.Column(
            controls=[s1, s2],
            expand=True
        )
    )

if __name__ == "__main__":
    ft.app(target=main)