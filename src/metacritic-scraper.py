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
session.mount('https://', adapter)


def get_metascore(title: str, platform: PlatformType) -> int or None:
    if title is None:
        raise TypeError('title must be str')

    table = str.maketrans('', '', ":'")
    modified_title = title.lower().translate(table).replace(' ', '-')

    url = f"https://www.metacritic.com/game/{platform.value}/{modified_title}"

    response = requests.get(url, headers=headers)

    # 해당 플랫폼에 게임이 없는 경우
    if not response.ok:
        return None

    html = response.text
    soup = BeautifulSoup(html, features='html.parser')
    element = soup.find('span', {'itemprop': 'ratingValue'})

    # 아직 점수가 결정되지 않은 경우
    if element is None:
        return None

    score = int(element.text)
    return score


def get_metascore(title: str) -> float:
    if title is None:
        raise TypeError('title must be str')

    table = str.maketrans('', '', ":'")
    modified_title = title.lower().translate(table).replace(' ', '-')

    scores = []

    for p in PlatformType:
        platform = p.value
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


def get_user_score(title: str, platform: PlatformType):
    if title is None:
        raise TypeError('title must be str')

    table = str.maketrans('', '', ":'")
    modified_title = title.lower().translate(table).replace(' ', '-')
    url = f"https://www.metacritic.com/game/{platform.value}/{modified_title}"

    response = session.get(url, headers=headers)

    # 해당 플랫폼에 게임이 없는 경우
    if not response.ok:
        return None

    html = response.text
    soup = BeautifulSoup(html, features='html.parser')
    element = soup.select_one(
        'div > div > div.left > div.with_trailer > div > div > div.summary_wrap > div.section.product_scores > div.details.side_details > div > div > a > div')
    return float(element.text)


if __name__ == '__main__':
    tlou2 = 'the last of us part ii'
    print(get_user_score(tlou2, PlatformType.PS4))
