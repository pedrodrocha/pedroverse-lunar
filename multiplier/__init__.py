from lunarcore.core.component import BaseComponent
from lunarcore.core.typings.components import ComponentGroup
from lunarcore.core.typings.datatypes import DataType

class Multiplier(
    BaseComponent,
    component_name="Multiplier",
    component_description="""Allows the multiplication of two numbers.
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