
from lunarcore.core.component import BaseComponent
from lunarcore.core.typings.components import ComponentGroup
from lunarcore.core.typings.datatypes import DataType
from lunarcore.core.data_models import ComponentInput, ComponentModel
from typing import Any, Optional
from .translator_service import TranslatorServiceFactory


class TextTranslator(
    BaseComponent,
    component_name="Text Translator",
    component_description="""Translates text from one language to another""",
    input_types={"text": DataType.TEXT, "source_language": DataType.TEXT, "target_language": DataType.TEXT},
    output_type=DataType.TEXT,
    component_group=ComponentGroup.UTILS,
    cf_api_key="$LUNARENV::CF_API_KEY",
    cf_account_id="$LUNARENV::CF_ACCOUNT_ID",
):
    def __init__(self, model: Optional[ComponentModel] = None, **kwargs: Any):
        super().__init__(model=model, configuration=kwargs)
        self._service = TranslatorServiceFactory.create(
            self.configuration["cf_api_key"], self.configuration["cf_account_id"]
        )


    def run(self, text: str, source_language: str, target_language: str):
        return self._service.run(text, source_language, target_language)