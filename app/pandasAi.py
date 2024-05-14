import os
import pandas as pd
from hashable_df import hashable_df
from pandasai import Agent
from pandasai.llm import GoogleGemini
from pandasai.llm import OpenAI


class PandasAi:
    def chat(self, json_object, prompt):
        oi_api_key = os.environ.get("OPENAI_API_KEY")
        gg_api_key = os.environ.get("GEMINI_API_KEY")

        if oi_api_key:
            llm = OpenAI(api_token=oi_api_key)
        elif gg_api_key:
            llm = GoogleGemini(api_key=gg_api_key)
        else:
            raise ValueError("No API key found for OpenAI or Gemini")

        df = pd.DataFrame(json_object)
        df = hashable_df(df)

        agent = Agent(df, config={"llm": llm})

        return agent.chat(prompt)
