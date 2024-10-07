import urllib3
import json


class CloudflareM2MTranslatorService:
    BASE_URL = "https://api.cloudflare.com/client/v4/accounts/"
    MODEL = "@cf/meta/m2m100-1.2b"

    def __init__(self: "CloudflareM2MTranslatorService", api_key: str, account_id: str) -> None:
        self._api_key = api_key
        self._account_id = account_id
        self.http = urllib3.PoolManager()

    def run(self, text: str, source_language: str, target_language: str) -> dict:
        url = f"{self.BASE_URL}{self._account_id}/ai/run/{self.MODEL}"

        headers = {
            "Authorization": f"Bearer {self._api_key}",
        }

        body = json.dumps({
            "text": text,
            "source_lang": source_language,
            "target_lang": target_language
        })

        response = self.http.request('POST', url, headers=headers, body=body)

        return json.dumps(json.loads(response.data.decode('utf-8')))
    
class TranslatorServiceFactory:
    @staticmethod
    def create(api_key: str, account_id: str) -> CloudflareM2MTranslatorService:
        return CloudflareM2MTranslatorService(api_key, account_id)