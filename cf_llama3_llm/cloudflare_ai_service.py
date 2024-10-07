import urllib3
import json

class CloudflareAIService:
    BASE_URL = "https://api.cloudflare.com/client/v4/accounts/"
    MODEL = "@cf/meta/llama-3.1-8b-instruct"
    
    def __init__(self: "CloudflareAIService", api_key: str, account_id: str) -> None:
        self._api_key = api_key
        self._account_id = account_id
        self.http = urllib3.PoolManager()

    def run(self, system_prompt: str, user_prompt: str) -> dict:
        url = f"{self.BASE_URL}{self._account_id}/ai/run/{self.MODEL}"

        headers = {
            "Authorization": f"Bearer {self._api_key}",
        }

        body = json.dumps({
            "stream": True,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        })
        
        response = self.http.request('POST', url, headers=headers, body=body, preload_content=False)
        
        data = b""
        for chunk in response.stream(1024):
            data += chunk
        response.release_conn()
        
        raw_data = data.decode('utf-8')        

        combined_response = ""
        for line in raw_data.splitlines():
            if line.startswith("data: "):
                json_data = line[len("data: "):].strip()
                if json_data and json_data != "[DONE]":
                    response_part = json.loads(json_data)
                    combined_response += response_part.get("response", "")
        
        return combined_response
    
class CloudflareAIServiceFactory:
    @staticmethod
    def create(api_key: str, account_id: str) -> CloudflareAIService:
        return CloudflareAIService(api_key, account_id)