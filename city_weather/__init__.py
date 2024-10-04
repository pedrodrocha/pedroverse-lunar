import json

from lunarcore.core.component import BaseComponent
from lunarcore.core.typings.components import ComponentGroup
from lunarcore.core.typings.datatypes import DataType
from lunarcore.core.data_models import ComponentInput, ComponentModel
from typing import Any, Optional
from .service import WeatherServiceFactory


class CityWeather(
    BaseComponent,
    component_name="City Weather",
    component_description="""Returns a json string with the current weather of a city.""",
    input_types={"city": DataType.TEXT},
    output_type=DataType.TEXT,
    component_group=ComponentGroup.API_TOOLS,
    weather_api_key="$LUNARENV::WEATHER_API_KEY",

):
    def __init__(self, model: Optional[ComponentModel] = None, **kwargs: Any):
        super().__init__(model=model, configuration=kwargs)
        self._service = WeatherServiceFactory.create(self.configuration["weather_api_key"])

    def run(self, city: str) -> str:
        return json.dumps(self._service.get_city_weather(city))