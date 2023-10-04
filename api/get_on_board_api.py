import requests


class GetOnBoardAPI:
    BASE_URL = "https://www.getonbrd.com/api/v0"

    def __init__(self):
        pass

    def get_jobs(self, category="programming", per_page=100, page=1):
        endpoint = f"/categories/{category}/jobs"
        params = {"per_page": per_page, "page": page, "expand": '["company"]'}

        response = requests.get(f"{self.BASE_URL}{endpoint}", params=params)

        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_categories(self, per_page=100, page=1):
        endpoint = f"/categories?per_page={per_page}&page={page}"
        params = {"per_page": per_page, "page": page}

        response = requests.get(f"{self.BASE_URL}{endpoint}", params=params)

        if response.status_code == 200:
            return response.json()
        else:
            return None
