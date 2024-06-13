import flet as ft
import fletor as ftor
from .types import StepperStyle


class Stepper(ftor.ResponsiveControl):

    def __update(self):
        print(self.step)
        if self.step != -1:
            if self.style == "fill":
                for i in range(self.step+1):
                    self.steps[i].bgcolor = self.steps_color
                for i in range(self.step+1, len(self.steps)):
                    self.steps[i].bgcolor = self.steps_disabled_color

            elif self.style == "one":
                for i in range(len(self.steps)):
                    if i == self.step:
                        self.steps[i].bgcolor = self.steps_color
                    else:
                        self.steps[i].bgcolor = self.steps_disabled_color

            if self.style == "fill_end":
                for i in range(self.step):
                    self.steps[i].bgcolor = self.steps_disabled_color
                for i in range(self.step, len(self.steps)):
                    self.steps[i].bgcolor = self.steps_color
            
            if self.style == "fill_between":
                for i in range(len(self.steps)):
                    if i == self.step:
                        self.steps[i].bgcolor = self.steps_disabled_color
                    else:
                        self.steps[i].bgcolor = self.steps_color

        self.contenedor_bottom.content = self.contents[self.step]
        if self.step == -1:
            self.contenedor_bottom.content = self.disabled_content
            for i in range(len(self.steps)):
                self.steps[i].bgcolor = self.steps_disabled_color
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

    def get_border(self, horizontal, index, length, border_width, border_color):
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

    def next_step(self):
        if self.step < len(self.contents) - 1:
            self.step += 1
            self.__update()

    def previous_step(self):
        if self.step > -1:
            self.step -= 1
            self.__update()

    def go_step(self, step):
        if step < len(self.contents):
            self.step = step
            self.__update()

    def __init__(
        self,
        contents,
        disabled_content,
        orientation:str="horizontal",
        style:StepperStyle=StepperStyle.fill ,
        step:int=-1,
        steps_color = ft.colors.ON_PRIMARY,
        steps_disabled_color = "",
        steps_anchor:int=5,
        steps_position: str="start",
        border_color:str=ft.colors.PRIMARY,
        border_width=0.5,
        border_radius = 0,
    ):
        super().__init__()
        self.step = step
        self.style = style
        self.contents = contents
        self.orientation = orientation
        self.border_color = border_color
        self.border_width = border_width
        self.border_radius = border_radius
        self.steps_color = steps_color
        self.steps_disabled_color = steps_disabled_color
        self.steps_position = steps_position
        self.steps_anchor = steps_anchor
        self.disabled_content = ftor.ResponsiveControl(
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
                    border=final_border
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
            self.content = ftor.ResponsiveColumn(
                [
                    ftor.ResponsiveRow(
                        [
                            self.steps[i]
                            for i in range(len(self.steps))
                        ],
                    ),
                    self.contenedor_bottom
                ] if self.steps_position == "start" else [
                    self.contenedor_bottom,
                    ftor.ResponsiveRow(
                        [
                            self.steps[i]
                            for i in range(len(self.steps))
                        ],
                    ),
                ],
                expands=[False, True] if self.steps_position == "start" else [True, False]
            )
        else:
            self.content = ftor.ResponsiveRow(
                [
                    ftor.ResponsiveColumn(
                        [
                            self.steps[i]
                            for i in range(len(self.steps))
                        ],
                    ),
                    self.contenedor_bottom
                ] if self.steps_position == "start" else [
                    self.contenedor_bottom,
                    ftor.ResponsiveColumn(
                        [
                            self.steps[i]
                            for i in range(len(self.steps))
                        ],
                        # debug="green"
                    ),
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
            ftor.ResponsiveColumn(
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
        ftor.ResponsiveColumn(
            [
                ftor.ResponsiveRow( 
                [
                    stepper,
                ]
            ),
            ftor.ResponsiveRow(
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