from typing import Any

from lunarcore.core.component import BaseComponent
from lunarcore.core.data_models import ComponentInput
from lunarcore.core.typings.components import ComponentGroup
from lunarcore.core.typings.datatypes import DataType



class NumberInput(
    BaseComponent,
    component_name="Number Input",
    component_description="""Allows the input of number that can then be used in other downstream components. It can also be used as an output if useful.
Inputs:
  `input` (float): The text to output.
Output (float): The inputted text.""",
    input_types={"input": DataType.FLOAT},
    output_type=DataType.FLOAT,
    component_group=ComponentGroup.IO,
):
    def run(
        self,
        input: float,
    ):
        return input