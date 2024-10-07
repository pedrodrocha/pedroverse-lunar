from lunarcore.core.component import BaseComponent
from lunarcore.core.typings.components import ComponentGroup
from lunarcore.core.typings.datatypes import DataType
from lunarcore.core.data_models import ComponentInput, ComponentModel
from typing import Any, Optional
from .cloudflare_ai_service import CloudflareAIServiceFactory

SYSTEM_PROMPT = "You are a helpful AI assistant. Your name is AI Rover."

class CfLlama3Prompt(
    BaseComponent,
        component_name="Cloudflare Llama 3 prompt",
        component_description="""Connects to Cloudflare, runs an inputted natural language prompt (str), and output the result as text (str).
    Inputs:
        `user_prompt` (str): The user prompt to provide the LLM with. If needed, the prompt can be inputted manually by the user.
        `system_prompt` (str): The system prompt to provide the LLM with. If needed, the prompt can be inputted manually by the user.
    Output (str): The answer provided by the LLM to the prompt.""",
        input_types={"system_prompt": DataType.TEMPLATE, "user_prompt": DataType.TEMPLATE},
        output_type=DataType.TEXT,
        component_group=ComponentGroup.GENAI,
        cf_api_key="$LUNARENV::CF_API_KEY",
        cf_account_id="$LUNARENV::CF_ACCOUNT_ID",
    ):
    def __init__(self, model: Optional[ComponentModel] = None, **kwargs: Any):
        super().__init__(model=model, configuration=kwargs)
        self._service = CloudflareAIServiceFactory.create(
            self.configuration["cf_api_key"], self.configuration["cf_account_id"]
        )
    def run(self, user_prompt: str, system_prompt: str = SYSTEM_PROMPT):
        return self._service.run(system_prompt, user_prompt)