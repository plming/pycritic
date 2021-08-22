import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

platformList = [
    'pc',
    'switch', 'wii-u', 'wii', 'gamecube', 'nintendo-64',
    '3ds', 'ds', 'game-boy-advance',
    'playstation-5', 'playstation-4', 'playstation-3', 'playstation-2', 'playstation',
    'playstation-vita', 'psp',
    'xbox-series-x', 'xbox-one', 'xbox',
    'stadia', 'ios', 'dreamcast'
]

headers = {'User-Agent': 'Mozilla/5.0'}


def get_rating_value(title: str) -> float:
    if title is None:
        raise TypeError('title must be str')

    table = str.maketrans('', '', ":'")
    modified_title = title.lower().translate(table).replace(' ', '-')

    scores = []

    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('https://', adapter)
    session.mount('https://', adapter)

    for platform in platformList:
        url = f"https://www.metacritic.com/game/{platform}/{modified_title}"

        # response = requests.get(url, headers=headers)
        response = session.get(url, headers=headers)

        # 해당 플랫폼에 게임이 없는 경우
        if not response.ok:
            continue

        html = response.text
        soup = BeautifulSoup(html, features='html.parser')
        element = soup.find('span', {'itemprop': 'ratingValue'})

        # 아직 점수가 결정되지 않은 경우
        if element is None:
            continue

        score = int(element.text)
        scores.append(score)

    if len(scores) == 0:
        raise ValueError(f"Can't find a game with name is {title}")

    return sum(scores) / len(scores)
