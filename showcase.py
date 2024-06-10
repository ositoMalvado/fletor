import fletor as ftor
import flet as ft

def main(page: ft.Page):
    page.add(
        ftor.ResponsiveRow(
            controls=[
                ftor.ResponsiveRow(
                    controls=[
                        ftor.ResponsiveColumn(
                            controls=[
                                ft.Text("Hello, World!"),
                                ft.Text("Goodbye, World!"),
                                ft.Text("Hello, World!"),
                            ],
                            expands=[4,1,1],    
                            debug="red"
                        ),
                        ftor.ResponsiveColumn(
                            controls=[
                                ft.Text("Hello, World!"),
                                ft.Text("Goodbye, World!"),
                                ft.Text("Hello, World!"),
                            ],
                            expands=[1,4,1],    
                            debug="green"
                        ),
                        ftor.ResponsiveColumn(
                            controls=[
                                ft.Text("Hello, World!"),
                                ft.Text("Goodbye, World!"),
                                ft.Text("Hello, World!"),
                            ],
                            expands=[1,1,4],    
                            debug="blue"
                        ),
                    ],
                    debug="yellow"
                ),
                ftor.ResponsiveColumn(
                    controls=[
                        ftor.ResponsiveRow(
                            controls=[
                                ft.Text("Hello, World!"),
                                ft.Text("Goodbye, World!"),
                                ft.Text("Hello, World!"),
                            ],
                            expands=[4,1,1],    
                            debug="red"
                        ),
                        ftor.ResponsiveRow(
                            controls=[
                                ft.Text("Hello, World!"),
                                ft.Text("Goodbye, World!"),
                                ft.Text("Hello, World!"),
                            ],
                            expands=[1,4,1],    
                            debug="green"
                        ),
                        ftor.ResponsiveRow(
                            controls=[
                                ft.Text("Hello, World!"),
                                ft.Text("Goodbye, World!"),
                                ft.Text("Hello, World!"),
                            ],
                            expands=[1,1,4],    
                            debug="blue"
                        ),
                    ],
                    debug="yellow"
                ),
                ftor.ResponsiveColumn(
                    controls=[
                        ftor.ResponsiveRow(
                            controls=[
                                ft.Text("Hello, World!"),
                                ft.Text("Goodbye, World!"),
                                ft.Text("Hello, World!"),
                            ],
                            expands=[1,2,3],    
                            debug="red"
                        ),
                        ftor.ResponsiveRow(
                            controls=[
                                ft.Text("Hello, World!"),
                                ft.Text("Goodbye, World!"),
                                ft.Text("Hello, World!"),
                            ],
                            expands=[1,2,2],    
                            debug="green"
                        ),
                        ftor.ResponsiveColumn(
                            controls=[
                                ft.Text("Hello, World!"),
                                ft.Text("Goodbye, World!"),
                                ft.Text("Hello, World!"),
                            ],
                            expands=[1,1,1],    
                            debug="blue"
                        ),
                    ],
                    debug="yellow"
                ),
            ],
            debug="blue"
        )
    )


ft.app(target=main)