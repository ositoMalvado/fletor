#fletor_update/__init__.py
import flet as ft
from .ResponsiveControl import ResponsiveControl
from .ResponsiveColumn import ResponsiveColumn
from .ResponsiveRow import ResponsiveRow
from .custom_types import *
from typing import Optional, Union, List


class Stepper(ResponsiveControl):

    def __update(self):
        if self.step != -1:
            if self.style == "fill":
                for i in range(self.step + 1):
                    self.steps[i].bgcolor = self.steps_color
                    self.steps[i].border = self.get_border(border_width=self.border_width, border_color=self.border_color)
                for i in range(self.step + 1, len(self.steps)):
                    self.steps[i].bgcolor = self.steps_disabled_color
                    self.steps[i].border = self.get_border(border_width=self.border_width, border_color=self.border_disabled_color)

            elif self.style == "one":
                for i in range(len(self.steps)):
                    if i == self.step:
                        self.steps[i].bgcolor = self.steps_color
                        self.steps[i].border = self.get_border(border_width=self.border_width, border_color=self.border_color)
                    else:
                        self.steps[i].bgcolor = self.steps_disabled_color
                        self.steps[i].border = self.get_border(border_width=self.border_width, border_color=self.border_disabled_color)

            elif self.style == "fill_end":
                for i in range(self.step):
                    self.steps[i].bgcolor = self.steps_disabled_color
                    self.steps[i].border = self.get_border(border_width=self.border_width, border_color=self.border_disabled_color)
                for i in range(self.step, len(self.steps)):
                    self.steps[i].bgcolor = self.steps_color
                    self.steps[i].border = self.get_border(border_width=self.border_width, border_color=self.border_color)

            elif self.style == "fill_between":
                for i in range(len(self.steps)):
                    if i == self.step:
                        self.steps[i].bgcolor = self.steps_disabled_color
                        self.steps[i].border = self.get_border(border_width=self.border_width, border_color=self.border_disabled_color)
                    else:
                        self.steps[i].bgcolor = self.steps_color
                        self.steps[i].border = self.get_border(border_width=self.border_width, border_color=self.border_color)

                        
            elif self.style == "one":
                for i in range(len(self.steps)):
                    if i == self.step:
                        self.steps[i].bgcolor = self.steps_color
                        self.steps[i].border = self.get_border(border_width=self.border_width, border_color=self.border_disabled_color)
                    else:
                        self.steps[i].bgcolor = self.steps_disabled_color
                        self.steps[i].border = self.get_border(border_width=self.border_width, border_color=self.border_color)

        self.contenedor_bottom.content = self.contents[self.step]
        if self.step == -1:
            self.contenedor_bottom.content = self.disabled_content
            for i in range(len(self.steps)):
                self.steps[i].bgcolor = self.steps_disabled_color
                self.steps[i].border = self.get_border(border_width=self.border_width, border_color=self.border_disabled_color)

        # self.contenedor_bottom.update()
        self.contenedor_bottom.content = self.contenedor_bottom.content
        self.update()

    def __on_click(self, e):

        if e.control.data != self.step:
            self.step = e.control.data
        else:
            self.step = -1
            for i in range(len(self.steps)):
                self.steps[i].bgcolor = self.steps_disabled_color
        self.__update()
    
    def did_mount(self):
        if self.step != -1 and self.step < len(self.contents):
            self.__update()
        return super().did_mount()

    def get_border(self, border_width, border_color):
        return ft.border.all(border_width, border_color)
        if horizontal:
            borders = {
                "left": ft.BorderSide(border_width, border_color),
                "top": ft.BorderSide(border_width, border_color),
                "bottom": ft.BorderSide(border_width, border_color),
            }
            if index == 0:
                return ft.border.only(left=borders["left"], bottom=borders["bottom"], top=borders["top"])
            elif index == length - 1:
                return ft.border.only(right=borders["left"], bottom=borders["bottom"], top=borders["top"], left=borders["left"])
            else:
                return ft.border.only(bottom=borders["bottom"], top=borders["top"], left=borders["left"])
        else:
            borders = {
                "top": ft.BorderSide(border_width, border_color),
                "left": ft.BorderSide(border_width, border_color),
                "right": ft.BorderSide(border_width, border_color),
            }
            if index == 0:
                return ft.border.only(top=borders["top"], left=borders["left"], right=borders["right"])
            elif index == length - 1:
                return ft.border.only(bottom=borders["top"], left=borders["left"], right=borders["right"], top=borders["top"])
            else:
                return ft.border.only(left=borders["left"], top=borders["top"], right=borders["right"])

    def next_step(self, e=None):
        if self.step < len(self.contents) - 1:
            self.step += 1
            self.__update()

    def previous_step(self, e=None):
        if self.step > -1:
            self.step -= 1
            self.__update()

    def go_step(self, step):
        if step < len(self.contents):
            self.step = step
            self.__update()

        ft.Container
    def __init__(
        self,
        contents:List[ft.Control],
        disabled_content:ft.Control,
        orientation:Optional[StepperOrientation]=StepperOrientation.HORIZONTAL,
        style: Optional[StepperStyle]=StepperStyle.FILL,
        step:Optional[int]=-1,
        steps_color:Optional[str] = ft.colors.ON_PRIMARY,
        steps_disabled_color:Optional[str] = "",
        steps_anchor:Optional[int]=5,
        steps_position: Optional[StepperStepsPosition]=StepperStepsPosition.START,
        border_color:Optional[str]=ft.colors.PRIMARY,
        border_disabled_color:Optional[str]=ft.colors.GREY,
        border_width:Optional[float]=0.5,
        border_radius:Optional[float]= 0,
        tap_separate:Optional[bool]=False,
    ):
        super().__init__()
        self.step = step
        self.style = style
        self.contents = contents
        self.orientation = orientation
        self.border_color = border_color
        self.border_disabled_color = border_disabled_color
        self.border_width = border_width
        self.border_radius = border_radius
        self.steps_color = steps_color
        self.steps_disabled_color = steps_disabled_color
        self.steps_position = steps_position
        self.steps_anchor = steps_anchor
        self.tap_separate = tap_separate
        self.disabled_content = ResponsiveControl(
            disabled_content
        )

        self.steps = []
        for i in range(len(self.contents)):
            if self.border_radius == 0:
                horizontal = self.orientation == "horizontal"
                final_border = self.get_border(horizontal, i, len(self.contents), self.border_width, self.border_color)
            else:final_border = ft.border.all(self.border_width, self.border_color)
                        

            self.steps.append(
                ft.Container(
                    on_click=self.__on_click,
                    data=i,
                    border_radius=self.border_radius,
                    border=final_border,
                )
            )
        if self.orientation == "horizontal":
            for step in self.steps:step.height = self.steps_anchor
        else:
            for step in self.steps:step.width = self.steps_anchor
        

        self.contenedor_bottom = ft.AnimatedSwitcher(
            self.disabled_content,
            transition=ft.AnimatedSwitcherTransition.SCALE,
            duration=300,
            reverse_duration=100,
        )


        if self.orientation == "horizontal":
            self.content = ResponsiveColumn(
                [
                    ResponsiveRow(
                        [
                            self.steps[i]
                            for i in range(len(self.steps))
                        ],
                    ),
                    ResponsiveRow(
                        [
                            ft.Container(
                                ResponsiveColumn(
                                    [
                                        ft.Icon(ft.icons.ARROW_BACK)
                                    ],
                                ),
                                on_click=self.previous_step,
                                bgcolor=ft.colors.with_opacity(0.1, ft.colors.PRIMARY),
                            ),
                            self.contenedor_bottom,
                            ft.Container(
                                ResponsiveColumn(
                                    [
                                        ft.Icon(ft.icons.ARROW_FORWARD)
                                    ],
                                ),
                                on_click=self.next_step,
                                bgcolor=ft.colors.with_opacity(0.1, ft.colors.PRIMARY),
                            ),
                        ],
                        expands=[20,100,20]
                    ) if self.tap_separate else ft.Stack(
                        [
                            self.contenedor_bottom,
                            ResponsiveRow(
                                [
                                    ft.Container(
                                        ResponsiveColumn(
                                            [
                                                ft.Icon(ft.icons.ARROW_BACK)
                                            ],
                                        ),
                                        on_click=self.previous_step,
                                        bgcolor=ft.colors.with_opacity(0.1, ft.colors.PRIMARY),
                                    ),
                                    ft.Text(),
                                    ft.Container(
                                        ResponsiveColumn(
                                            [
                                                ft.Icon(ft.icons.ARROW_FORWARD)
                                            ],
                                        ),
                                        on_click=self.next_step,
                                        bgcolor=ft.colors.with_opacity(0.1, ft.colors.PRIMARY),
                                    ),
                                ],
                                expands=[20,100,20]
                            )
                        ]
                    )
                ] if self.steps_position == "start" else [
                    ft.Stack(
                        [
                            self.contenedor_bottom,
                            ResponsiveRow(
                                [
                                    ft.Container(
                                        ResponsiveColumn(
                                            [
                                                ft.Icon(ft.icons.ARROW_BACK)
                                            ],
                                        ),
                                        on_click=self.previous_step,
                                        bgcolor=ft.colors.with_opacity(0.1, ft.colors.PRIMARY),
                                    ),
                                    ft.Text(),
                                    ft.Container(
                                        ResponsiveColumn(
                                            [
                                                ft.Icon(ft.icons.ARROW_FORWARD)
                                            ],
                                        ),
                                        on_click=self.next_step,
                                        bgcolor=ft.colors.with_opacity(0.1, ft.colors.PRIMARY),
                                    ),
                                ],
                                expands=[20,100,20]
                            )
                        ]
                    ) if self.tap_separate else ResponsiveRow(
                        [
                            ft.Container(
                                ResponsiveColumn(
                                    [
                                        ft.Icon(ft.icons.ARROW_BACK)
                                    ],
                                ),
                                on_click=self.previous_step,
                                bgcolor=ft.colors.with_opacity(0.1, ft.colors.PRIMARY),
                            ),
                            self.contenedor_bottom,
                            ft.Container(
                                ResponsiveColumn(
                                    [
                                        ft.Icon(ft.icons.ARROW_FORWARD)
                                    ],
                                ),
                                on_click=self.next_step,
                                bgcolor=ft.colors.with_opacity(0.1, ft.colors.PRIMARY),
                            ),
                        ],
                        expands=[20,100,20]
                    ),
                    ResponsiveRow(
                        [
                            self.steps[i]
                            for i in range(len(self.steps))
                        ],
                    ),
                ],
                expands=[False, True] if self.steps_position == "start" else [True, False]
            )
        elif self.orientation == "vertical":
            self.content = ResponsiveRow(
                [
                    
                    ResponsiveColumn(
                        [
                            self.steps[i]
                            for i in range(len(self.steps))
                        ],
                    ),
                    ft.Stack(
                        [
                            self.contenedor_bottom,
                            ResponsiveRow(
                                [
                                    ft.Container(
                                        ResponsiveColumn(
                                            [
                                                ft.Icon(ft.icons.ARROW_BACK)
                                            ],
                                        ),
                                        on_click=self.previous_step,
                                        bgcolor=ft.colors.with_opacity(0.1, ft.colors.PRIMARY),
                                    ),
                                    ft.Text(),
                                    ft.Container(
                                        ResponsiveColumn(
                                            [
                                                ft.Icon(ft.icons.ARROW_FORWARD)
                                            ],
                                        ),
                                        on_click=self.next_step,
                                        bgcolor=ft.colors.with_opacity(0.1, ft.colors.PRIMARY),
                                    ),
                                ],
                                expands=[20,100,20]
                            )
                        ]
                    ) if not self.tap_separate else ResponsiveRow(
                        [
                            ft.Container(
                                ResponsiveColumn(
                                    [
                                        ft.Icon(ft.icons.ARROW_BACK)
                                    ],
                                ),
                                on_click=self.previous_step,
                                bgcolor=ft.colors.with_opacity(0.1, ft.colors.PRIMARY),
                            ),
                            self.contenedor_bottom,
                            ft.Container(
                                ResponsiveColumn(
                                    [
                                        ft.Icon(ft.icons.ARROW_FORWARD)
                                    ],
                                ),
                                on_click=self.next_step,
                                bgcolor=ft.colors.with_opacity(0.1, ft.colors.PRIMARY),
                            ),
                        ],
                        expands=[20,100,20]
                    )
                ] if self.steps_position == "start" else [
                    ft.Stack(
                        [
                            self.contenedor_bottom,
                            ResponsiveRow(
                                [
                                    ft.Container(
                                        ResponsiveColumn(
                                            [
                                                ft.Icon(ft.icons.ARROW_BACK)
                                            ],
                                        ),
                                        on_click=self.previous_step,
                                        bgcolor=ft.colors.with_opacity(0.1, ft.colors.PRIMARY),
                                    ),
                                    ft.Text(),
                                    ft.Container(
                                        ResponsiveColumn(
                                            [
                                                ft.Icon(ft.icons.ARROW_FORWARD)
                                            ],
                                        ),
                                        on_click=self.next_step,
                                        bgcolor=ft.colors.with_opacity(0.1, ft.colors.PRIMARY),
                                    ),
                                ],
                                expands=[20,100,20]
                            )
                        ]
                    ) if not self.tap_separate else ResponsiveRow(
                        [
                            ft.Container(
                                ResponsiveColumn(
                                    [
                                        ft.Icon(ft.icons.ARROW_BACK)
                                    ],
                                ),
                                on_click=self.previous_step,
                                bgcolor=ft.colors.with_opacity(0.1, ft.colors.PRIMARY),
                            ),
                            self.contenedor_bottom,
                            ft.Container(
                                ResponsiveColumn(
                                    [
                                        ft.Icon(ft.icons.ARROW_FORWARD)
                                    ],
                                ),
                                on_click=self.next_step,
                                bgcolor=ft.colors.with_opacity(0.1, ft.colors.PRIMARY),
                            ),
                        ],
                        expands=[20,100,20]
                    ),
                    ResponsiveColumn(
                        [
                            self.steps[i]
                            for i in range(len(self.steps))
                        ],
                        # debug="green"
                    )
                ],
                expands=[False, True] if self.steps_position == "start" else [True, False]
            )



def main(page: ft.Page):
    page.spacing = 0
    page.padding = 0
    page.window_frameless = False
    page.window_title_bar_hidden = True
    page.window_height = 600
    page.window_width = 400
    page.window_resizable = True
    if not page.window_resizable:
        page.window_max_height = page.window_height
        page.window_min_width = page.window_width
        page.window_max_height = page.window_height
        page.window_min_width = page.window_width
    page.window_center()


    stepper = Stepper(
        contents=[
            ResponsiveColumn(
                [
                    Stepper(
                        contents=[ft.Text(f"Hello, World! FOR {i+1} TIME ") for i in range(10)],
                        disabled_content=ft.Text("Disabled"),
                        style="one",
                        orientation="vertical",
                        steps_position="start",
                        steps_anchor=30,
                        border_width=1,
                        border_radius=10,
                    ),
                ],
                # expands=[True, False]
            )
            for i in range(10)
        ],
        disabled_content=ft.Text("Disabled"),
        style=StepperStyle.FILL,
        orientation="horizontal",
        steps_position="end",
        steps_anchor=30,
        border_width=1,
        border_radius=10,
        step=0
    )
    

    page.add(
        ResponsiveColumn(
            [
                ResponsiveRow( 
                [
                    stepper,
                ]
            ),
            ResponsiveRow(
                [
                    ft.IconButton(
                        icon=ft.icons.ARROW_BACK,
                        on_click=lambda e: stepper.previous_step()
                    ),
                    ft.IconButton(
                        icon=ft.icons.ARROW_FORWARD,
                        on_click=lambda e: stepper.next_step()
                    ),
                ]
            )
            ],
            expands=[True, False],
            debug="green"
        )
        
    )


if __name__ == "__main__":
    ft.app(target=main)