import requests
from config import GITHUB_TOKEN

def authenticated_get_request(url) -> dict:
    return requests.get(url, headers={
        "Authorization": f"Bearer {GITHUB_TOKEN}"
    }).json()

class GithubUser():
    def __init__(self, username: str) -> None:
        self.username = username
        self.languages = self.get_languages()
        self.image = self.get_image()

    def get_languages(self) -> list[str]:
        repositories: list[dict] = authenticated_get_request(f"https://api.github.com/users/{self.username}/repos?sort=pushed")
        languages: dict[str, int] = {}
        for repository in repositories:
            language = repository["language"]
            if not language: continue
            if language in languages: languages[language] += 1
            else: languages[language] = 1
        sorted_languages_by_appearance = sorted(list(languages.items()), key=lambda l: l[1], reverse=True)
        return list(map(lambda l: l[0], sorted_languages_by_appearance))

    def get_image(self) -> str:
        return authenticated_get_request(f"https://api.github.com/users/{self.username}")["avatar_url"]