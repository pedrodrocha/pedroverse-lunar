from typing import Any

from lunarcore.core.component import BaseComponent
from lunarcore.core.data_models import ComponentInput
from lunarcore.core.typings.components import ComponentGroup
from lunarcore.core.typings.datatypes import DataType

class Multiplier(
    BaseComponent,
    component_name="Number Input",
    component_description="""Allows the input of number that can then be used in other downstream components. It can also be used as an output if useful.
Inputs:
  `multiplicand` (float): The multiplicand number.
    `multiplier` (float): The multiplier number.
Output (float): The multiplication result.""",
    input_types={"multiplicand": DataType.FLOAT, "multiplier": DataType.FLOAT},
    output_type=DataType.FLOAT,
    component_group=ComponentGroup.UTILS,
):
    def run(
        self,
        multiplicand: float,
        multiplier: float,
    ):
        return multiplicand * multiplier