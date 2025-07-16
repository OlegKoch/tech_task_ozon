import requests

def parse_height(height_list):
    try:
        return int(height_list[1].replace(" cm", ""))
    except:
        return 0


def get_high_person(heroes, gender, work):
    total_height = 0
    total = None

    for hero in heroes:
        hero_gender = hero.get("appearance", {}).get("gender")
        occupation = hero.get("work", {}).get("occupation")
        height_list = hero.get("appearance", {}).get("height", [])
        hero_name = hero.get("name")

        if gender != hero_gender:
            continue
        has_work = occupation != "-"

        if has_work != work:
            continue

        height_cm = parse_height(height_list)

        if total_height < height_cm:
            total_height = height_cm
            total = hero

    return total


url = "https://akabab.github.io/superhero-api/api/all.json"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
else:
    print(f"Ошибка запроса: {response.status_code}")

print(get_high_person(data, gender="Male", work=True))