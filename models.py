import os

from agno.models.google import Gemini
from agno.models.openai import OpenAIChat
from agno.models.openrouter import OpenRouter

CLOUD_CODE_GEMINI_CODE_ASSIST_API_KEY = os.getenv("CLOUD_CODE_GEMINI_CODE_ASSIST_API_KEY", "")

gemini_3_model = Gemini(
    id="gemini-1.5-pro",
    vertexai=True,
    project_id="gemini-code-assist-license",
    location="us-central1"
)
gemini_2_5_flash_model = Gemini(
    id="gemini-1.5-flash",
    vertexai=True,
    project_id="gemini-code-assist-license",
    location="us-central1"
)

KIMI_CLI_API_KEY = os.getenv("KIMI_CLI_API_KEY", "")
KIMI_CLI_BASE_URL = "https://api.kimi.ai/v1"

class KimiForCodingModel(OpenAIChat):
    def __init__(self, id: str):
        super().__init__(id=id, api_key=KIMI_CLI_API_KEY, base_url=KIMI_CLI_BASE_URL)

# KIMI model (Moonshot AI)
kimi_model_direct = KimiForCodingModel(id="moonshot-v1-8k")

MOONSHOT_BASE_URL = "https://api.moonshot.ai/v1"
MOONSHOT_API_KEY = os.getenv("MOONSHOT_API_KEY", "")

class MoonshotKimiModel(OpenAIChat):
    def __init__(self, id: str):
        super().__init__(id=id, api_key=MOONSHOT_API_KEY, base_url=MOONSHOT_BASE_URL)

moonshot_kimi_k2_model = MoonshotKimiModel(
    id="kimi-k2-0905-preview"
)

moonshot_kimi_k2_turbo_model = MoonshotKimiModel(
    id="kimi-k2-turbo-preview"
)

MODEL_STUDIO_BASE_URL = "https://dashscope-intl.aliyuncs.com/compatible-mode/v1"
MODEL_STUDIO_API_KEY = os.getenv("MODEL_STUDIO_API_KEY", "")

# Model Studio model (DashScope/Alibaba Cloud)
model_studio_model = OpenAIChat(
    id="qwen-plus",
    api_key=MODEL_STUDIO_API_KEY,
    base_url=MODEL_STUDIO_BASE_URL,
)

OPENROUTER_API_KEY = os.getenv("OPENROUTER_AGNO_API_KEY", "")

class OpenRouterModel(OpenRouter):
    def __init__(self, id: str):
        super().__init__(id=id, api_key=OPENROUTER_API_KEY)


qwen3_coder_model = OpenRouterModel(id="qwen/qwen3-coder:free")
gemini_flash_exp_model = OpenRouterModel(id="google/gemini-2.0-flash-exp:free")
glm_4_5_air_model = OpenRouterModel(id="z-ai/glm-4.5-air:free")
qwen3_235b_model = OpenRouterModel(id="qwen/qwen3-235b-a22b:free")
gpt_oss_model = OpenRouterModel(id="openai/gpt-oss-120b:free")
kimi_openrouter_model = OpenRouterModel(id="moonshotai/kimi-k2:free")
