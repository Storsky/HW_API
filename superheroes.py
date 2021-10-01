import requests

TOKEN = "2619421814940190"
class Superhero:
    url = 'https://superheroapi.com/api/' + TOKEN
    def __init__(self, name):
        self.name = name
        self.params = (requests.get((Superhero.url +'/search/' + name))).json()
        self.stats = self.params['results']
        self.powerstats = self.stats[0]['powerstats']

    def powers(self, power):
        return self.powerstats[power]



def who_is_smartest(list_superheroes):
    smartest = 'None'
    basic = 0
    for hero in list_superheroes:
        if int(hero.powers('intelligence')) > basic:
            basic = int(hero.powers('intelligence'))
            smartest = hero.name
    return smartest

if __name__ == '__main__':
    thanos = Superhero('THANOS')
    captain = Superhero('Captain America')
    hulk = Superhero('HULK')
    print(f'Самый умный из предложенных героев {who_is_smartest([thanos, captain, hulk])}')
