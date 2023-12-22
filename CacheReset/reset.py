import time
import requests
from colorama import Fore, Style


def reset_cache():
    products = [
        {
            "id": 7089,
            "name": "Pink Bellini"
        },
        {
            "id": 8837,
            "name": "Starry Night"
        },
        {
            "id": 7087,
            "name": "Festive Bouquet Letterbox"
        },
        {
            "id": 7097,
            "name": "Sugar Plum Fairy Letterbox"
        },
        {
            "id": 265,
            "name": "Festive Bouquet XL "
        },
        {
            "id": 416,
            "name": "Christmas Candy XL"
        },
        {
            "id": 7096,
            "name": "Sugar Plum Fairy"
        },
        {
            "id": 8798,
            "name": "Christmas Alstroemeria"
        },
        {
            "id": 8861,
            "name": "Festive Fizz"
        },
        {
            "id": 582,
            "name": "Winter Warmth"
        },
        {
            "id": 7088,
            "name": "Christmas Mulberry "
        },
        {
            "id": 264,
            "name": "Christmas Wishes "
        },
        {
            "id": 1532,
            "name": "Christmas Wishes  Letterbox"
        },
        {
            "id": 5271,
            "name": "Christmas Candy Letterbox"
        },
        {
            "id": 7092,
            "name": "Rocking Robin"
        },
        {
            "id": 8794,
            "name": "Happy Christmas Gift"
        },
        {
            "id": 7090,
            "name": "Purple Jewel"
        },
        {
            "id": 8840,
            "name": "Velvet Dreams"
        },
        {
            "id": 5252,
            "name": "Joyeux Noël"
        },
        {
            "id": 10,
            "name": "Oriental Orchids"
        },
        {
            "id": 8833,
            "name": "Merry and Bright "
        },
        {
            "id": 8834,
            "name": "Merry and Bright Letterbox "
        },
        {
            "id": 7304,
            "name": "Mulberry Blush Large"
        },
        {
            "id": 1091,
            "name": "Snowflake Large"
        },
        {
            "id": 765,
            "name": "Christmas Candy  Large"
        },
        {
            "id": 1092,
            "name": "Snowflake XL"
        },
        {
            "id": 764,
            "name": "Festive Bouquet Large"
        },
        {
            "id": 500,
            "name": "Damson Delight"
        },
        {
            "id": 7098,
            "name": "Sugar Plum Fairy Large"
        },
        {
            "id": 7303,
            "name": "Mulberry Blush"
        },
        {
            "id": 415,
            "name": "Christmas Candy "
        },
        {
            "id": 8839,
            "name": "Christmas Roses and Freesias"
        },
        {
            "id": 266,
            "name": "Festive Bouquet"
        },
        {
            "id": 8841,
            "name": "Winterberry Wonder"
        },
        {
            "id": 8762,
            "name": "Christmas Mokara Orchids"
        }
    ]

    for product in products:
        url = 'https://www.bunches.co.uk/api/calendar/get-days/2023-12-27/2024-01-30/' + str(product['id'])
        request = requests.get(url)

        if request.status_code == 200:
            print(
                f"{Fore.GREEN}Cache reset for {str(product['name'])}: {Style.RESET_ALL}{str(product['id'])} {Fore.GREEN}✅{Style.RESET_ALL}")
        else:
            print(f'The request failed with status code {request.status_code}')


if __name__ == '__main__':
    reset_cache()
