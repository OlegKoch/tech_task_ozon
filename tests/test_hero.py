import requests
from api import get_high_person

url = "https://akabab.github.io/superhero-api/api/all.json"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
else:
    print(f"Ошибка запроса: {response.status_code}")


def test_high_male_with_work():
    hero = get_high_person(data, gender="Male", work=True)
    assert hero is not None
    if hero:
        assert hero["name"] == "Galactus"
        assert hero["appearance"]["gender"] == "Male"
        assert hero["work"]["occupation"] != "-"
        assert hero["appearance"]["height"][1] == "876 cm"


def test_high_female_with_work():
    hero = get_high_person(data, gender="Female", work=True)
    assert hero is not None
    if hero:
        assert hero["name"] == "Wolfsbane"
        assert hero["appearance"]["gender"] == "Female"
        assert hero["work"]["occupation"] != "-"
        assert hero["appearance"]["height"][1] == "366 cm"


def test_high_male_without_work():
    hero = get_high_person(data, gender="Male", work=False)
    assert hero is not None
    if hero:
        assert hero["name"] == "Fin Fang Foom"
        assert hero["appearance"]["gender"] == "Male"
        assert hero["work"]["occupation"] == "-"
        assert hero["appearance"]["height"][1] == "975 cm"


def test_high_female_without_work():
    hero = get_high_person(data, gender="Female", work=False)
    assert hero is not None
    if hero:
        assert hero["name"] == "Ardina"
        assert hero["appearance"]["gender"] == "Female"
        assert hero["work"]["occupation"] == "-"
        assert hero["appearance"]["height"][1] == "193 cm"


def test_empty_list():
    hero = get_high_person([], gender="Male", work=True)
    assert hero is None


