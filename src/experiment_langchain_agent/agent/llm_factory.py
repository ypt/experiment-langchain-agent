from enum import Enum


class LLMType(Enum):
    OPEN_AI = "OPEN_AI"
    GOOGLE_PALM = "GOOGLE_PALM"


def create_llm(llm_type: LLMType, llm_api_key: str):
    # TODO: generic llm loader interfaces for each, instead of this huge switch
    # TODO: add support for local models - e.g. Huggingface, GPT4all
    match llm_type:
        case LLMType.OPEN_AI:
            from langchain.llms import OpenAI
            return OpenAI(openai_api_key=llm_api_key)
        case LLMType.GOOGLE_PALM:
            from langchain.llms.google_palm import GooglePalm
            return GooglePalm(google_api_key=llm_api_key, verbose=True)
        case _:
            raise ValueError(f"Unsupported LLM type: {llm_type}")
