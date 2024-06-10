from fletor import *
import flet as ft

def main(page: ft.Page):
    page.add(
        ResponsiveRow(
            controls=[
                ResponsiveRow(
                    controls=[
                        ResponsiveColumn(
                            controls=[
                                ft.Text("Hello, World!"),
                                ft.Text("Goodbye, World!"),
                                ft.Text("Hello, World!"),
                            ],
                            expands=[4,1,1],    
                            debug="red"
                        ),
                        ResponsiveColumn(
                            controls=[
                                ft.Text("Hello, World!"),
                                ft.Text("Goodbye, World!"),
                                ft.Text("Hello, World!"),
                            ],
                            expands=[1,4,1],    
                            debug="green"
                        ),
                        ResponsiveColumn(
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
                ResponsiveColumn(
                    controls=[
                        ResponsiveRow(
                            controls=[
                                ft.Text("Hello, World!"),
                                ft.Text("Goodbye, World!"),
                                ft.Text("Hello, World!"),
                            ],
                            expands=[4,1,1],    
                            debug="red"
                        ),
                        ResponsiveRow(
                            controls=[
                                ft.Text("Hello, World!"),
                                ft.Text("Goodbye, World!"),
                                ft.Text("Hello, World!"),
                            ],
                            expands=[1,4,1],    
                            debug="green"
                        ),
                        ResponsiveRow(
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
                ResponsiveColumn(
                    controls=[
                        ResponsiveRow(
                            controls=[
                                ft.Text("Hello, World!"),
                                ft.Text("Goodbye, World!"),
                                ft.Text("Hello, World!"),
                            ],
                            expands=[1,2,3],    
                            debug="red"
                        ),
                        ResponsiveRow(
                            controls=[
                                ft.Text("Hello, World!"),
                                ft.Text("Goodbye, World!"),
                                ft.Text("Hello, World!"),
                            ],
                            expands=[1,2,2],    
                            debug="green"
                        ),
                        ResponsiveColumn(
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