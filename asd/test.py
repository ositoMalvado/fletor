import fletor as ftor
import flet as ft


def main(page: ft.Page):
    page.add(
        ftor.ResponsiveRow(
            controls=[
                ftor.ResponsiveColumn(
                    [
                        ftor.ResponsiveControl(ft.Text("ft.ImageFit.CONTAIN")),
                        ftor.ResponsiveControl(ft.Image(src="https://picsum.photos/500", fit=ft.ImageFit.CONTAIN, width=1300, height=1300, expand=True), debug=ft.colors.BLUE),
                        ftor.ResponsiveControl(ft.Text("ft.ImageFit.FILL")),
                        ftor.ResponsiveControl(ft.Image(src="https://picsum.photos/500", fit=ft.ImageFit.FILL, width=1300, height=1300, expand=True), debug=ft.colors.BLUE),
                        ftor.ResponsiveControl(ft.Text("ft.ImageFit.COVER")),
                        ftor.ResponsiveControl(ft.Image(src="https://picsum.photos/500", fit=ft.ImageFit.COVER, width=1300, height=1300, expand=True), debug=ft.colors.BLUE)
                    ],
                    [1, 5, 1, 5, 1, 5]
                ),
                ftor.ResponsiveColumn(
                    [
                        ftor.ResponsiveControl(ft.Text("ft.ImageFit.FIT_HEIGHT")),
                        ftor.ResponsiveControl(ft.Image(src="https://picsum.photos/500", fit=ft.ImageFit.FIT_HEIGHT, width=1300, height=1300, expand=True), debug=ft.colors.BLUE),
                        ftor.ResponsiveControl(ft.Text("ft.ImageFit.FIT_WIDTH")),
                        ftor.ResponsiveControl(ft.Image(src="https://picsum.photos/500", fit=ft.ImageFit.FIT_WIDTH, width=1300, height=1300, expand=True), debug=ft.colors.BLUE),
                        ftor.ResponsiveControl(ft.Text("ft.ImageFit.SCALE_DOWN")),
                        ftor.ResponsiveControl(ft.Image(src="https://picsum.photos/500", fit=ft.ImageFit.SCALE_DOWN, width=1300, height=1300, expand=True), debug=ft.colors.BLUE)
                    ],
                    [1, 5, 1, 5, 1, 5]
                ),
            ],
            debug=ft.colors.BLUE
        )
    )


ft.app(target=main)