import requests
import json


class FastchatProvider:
    def __init__(
        self,
        AI_PROVIDER_URI: str = "",
        AI_MODEL: str = "vicuna",
        MODEL_PATH: str = "",
        **kwargs,
    ):
        self.requirements = []
        self.AI_PROVIDER_URI = AI_PROVIDER_URI
        self.AI_MODEL = AI_MODEL
        self.MODEL_PATH = MODEL_PATH

    def instruct(self, prompt, tokens: int = 0):
        messages = [{"role": "system", "content": prompt}]
        params = {"model": self.MODEL_PATH, "prompt": prompt}
        response = requests.post(
                f"{self.AI_PROVIDER_URI}/v1/chat/completions",
                json=params,
                timeout=600,
            )
        #response = requests.post(
        #    f"{self.AI_PROVIDER_URI}/v1/chat/completions",
            #json={"data": [json.dumps([prompt, params])]},
        #    json=json.dumps(params),
        #)
        #return response.json()["data"][0].replace("\n", "\n")
        result = response.json()["text"]
        print(f"Fast Chat request : {result}")
        out = result[len(prompt):].replace("\n", "\n") 
        print(f"Fast Chat substring : {out}")
        return out
