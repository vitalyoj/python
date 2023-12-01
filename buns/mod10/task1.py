import requests
import json

def get_millennium_falcon_info():
    # URL для получения информации о кораблях
    starship_url = "https://swapi.dev/api/starships/"
    
    # Отправляем GET-запрос, чтобы получить список кораблей
    response = requests.get(starship_url)
    starships = response.json()["results"]
    
    # Найдем Millennium Falcon среди кораблей
    millennium_falcon = next((ship for ship in starships if ship["name"] == "Millennium Falcon"), None)
    
    if millennium_falcon:
        # Извлекаем информацию о пилотах
        pilots_info = []
        for pilot_url in millennium_falcon["pilots"]:
            pilot_response = requests.get(pilot_url)
            pilot_data = pilot_response.json()
            homeworld_response = requests.get(pilot_data["homeworld"])
            homeworld_data = homeworld_response.json()

            pilot_info = {
                "name": pilot_data["name"],
                "height": pilot_data["height"],
                "weight": pilot_data["mass"],
                "homeworld": pilot_data["homeworld"],
                "homeworld_info": {
                    "name": homeworld_data["name"],
                    "url": pilot_data["homeworld"]
                }
            }
            pilots_info.append(pilot_info)

        # Формируем информацию о Millennium Falcon
        millennium_falcon_info = {
            "name": millennium_falcon["name"],
            "max_speed": millennium_falcon["max_atmosphering_speed"],
            "class": millennium_falcon["starship_class"],
            "pilots": pilots_info
        }

        # Выводим информацию на экран
        print(json.dumps(millennium_falcon_info, indent=2))

        # Записываем информацию в JSON-файл
        with open("millennium_falcon_info.json", "w") as json_file:
            json.dump(millennium_falcon_info, json_file, indent=2)
    else:
        print("Millennium Falcon not found in the Star Wars API.")

if __name__ == "__main__":
    get_millennium_falcon_info()