import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from PlatformType import PlatformType

headers = {'User-Agent': 'Mozilla/5.0'}
session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('https://', adapter)


def to_route(title: str) -> str:
    if not isinstance(title, str):
        raise TypeError('title must be str')

    table = str.maketrans('', '', ":'")
    modified_title = title.lower().translate(table).replace(' ', '-')
    return modified_title


def get_soup(title: str, platform: PlatformType) -> BeautifulSoup:
    title = to_route(title)
    url = f"https://www.metacritic.com/game/{platform.value}/{title}"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise RuntimeError(response)

    return BeautifulSoup(response.text, features='html.parser')


def get_metascore(title: str, platform: PlatformType) -> int or None:
    soup = get_soup(title, platform)
    element = soup.find('span', {'itemprop': 'ratingValue'})

    # 아직 점수가 결정되지 않은 경우
    if element is None:
        return None

    score = int(element.text)
    return score


def get_user_score(title: str, platform: PlatformType) -> float or None:
    soup = get_soup(title, platform)
    element = soup.find('div', class_='user')

    return float(element.text)


def get_developer(title: str, platform: PlatformType) -> str or None:
    soup = get_soup(title, platform)
    element = soup.find('li', class_='developer').select_one('span.data > a')

    return element.text


def get_rating(title: str, platform: PlatformType) -> str or None:
    soup = get_soup(title, platform)
    element = soup.find('li', class_='product_rating').select_one('span.data')

    return element.text


def get_genre(title: str, platform: PlatformType) -> list[str]:
    soup = get_soup(title, platform)
    result_set = soup.find('li', class_='product_genre').select('span.data')

    genre = list[str]()
    for element in result_set:
        genre.append(element.text)

    return genre
