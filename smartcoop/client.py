import requests

class SmartCoopClient:
    def __init__(self, client_secret: str):
        self.client_secret = client_secret
        self.base_url = 'https://x107.omlet.co.uk/api/v1'

    def _get_headers(self) -> dict[str, str]:
        return {
            'Authorization': f'Bearer {self.client_secret}',
            'Content-Type': 'application/json'
        }

    def get(self, endpoint: str, params=None):
        url = f'{self.base_url}/{endpoint}'
        headers = self._get_headers()
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint: str, json=None):
        url = f'{self.base_url}/{endpoint}'
        headers = self._get_headers()
        response = requests.post(url, headers=headers, json=json)
        response.raise_for_status()
        return response.json()

    def patch(self, endpoint: str, json=None):
        url = f'{self.base_url}/{endpoint}'
        headers = self._get_headers()
        response = requests.patch(url, headers=headers, json=json)
        response.raise_for_status()


    def delete(self, endpoint: str):
        url = f'{self.base_url}/{endpoint}'
        headers = self._get_headers()
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
