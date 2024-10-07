import urllib3
import json

class CloudflareAIService:
    BASE_URL = "https://api.cloudflare.com/client/v4/accounts/"
    MODEL = "@cf/meta/llama-3.1-8b-instruct"
    def __init__(self: "CloudflareAIService", api_key: str, account_id: str) -> None:
        self._api_key = api_key
        self._account_id = account_id
        self.http = urllib3.PoolManager()


    def run(self: "CloudflareAIService", system_prompt: str, user_prompt: str) -> dict:
        url = f"{self.BASE_URL}{self._account_id}/ai/run/{self.MODEL}"

        headers = {
            "Authorization": f"Bearer {self._api_key}",
        }

        body = json.dumps({
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        })
        response = self.http.request('POST', url, headers=headers, body=body)
        result = json.loads(response.data.decode('utf-8'))
        return result
    
class CloudflareAIServiceFactory:
    @staticmethod
    def create(api_key: str, account_id: str) -> CloudflareAIService:
        return CloudflareAIService(api_key, account_id)