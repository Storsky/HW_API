import datetime
import requests
from pprint import pprint


def get_questions():
    dt=datetime.datetime.utcnow()
    today = dt.replace(tzinfo=datetime.timezone.utc).timestamp()
    two_ago = dt - datetime.timedelta(days=2)
    two_ago_UTC = two_ago.replace(tzinfo=datetime.timezone.utc).timestamp()
    dt = int(today)
    two_ago = int(two_ago_UTC)


    url = f'https://api.stackexchange.com/2.3/questions?fromdate={two_ago}&todate={dt}&sort=votes&tagged=Python&site=stackoverflow'
    response = requests.get(url)
    return response.json()

if __name__ == '__main__':
    pprint(get_questions())
