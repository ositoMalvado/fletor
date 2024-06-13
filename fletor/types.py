from typing import Dict, Tuple, Union

class StepperStyle():
    FILL = "fill"
    ONE = "one"
    FILL_END = "fill_end"
    FILL_START = "fill_start"
    FILL_BETWEEN = "fill_between"


class StepperOrientation():
    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"

class StepperStepsPosition(Enum):
    START = "start"
    END = "end"