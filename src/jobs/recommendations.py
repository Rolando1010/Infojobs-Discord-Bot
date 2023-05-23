from github.user import GithubUser
from jobs.offers import Offer, search_offers

def get_recommendation_offers(github_user: GithubUser):
    recommendation_offers: dict[str, list[Offer]] = {}
    for language in github_user.languages[:2]:
        recommendation_offers[language] = search_offers(language, 1)
    return recommendation_offers