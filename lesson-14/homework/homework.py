# Homework 
# exercise-1

import requests
import os
import json 

with open("student.json") as f:
    my_dict = json.load(f)

for dict in my_dict['studnet']:
    print(f"This student's name is{dict['name']} and he/she is{dict['age']}yers old and he/she lives in {dict['adress']['city']}")
print(my_dict)



#exercise2


cities = ['Tashkent', 'Karshi', 'Samarkand', 'Urgench']
my_api_key = '0dedf962808bb77ca0fc883f728fb1fb'

for city in cities:
    my_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={my_api_key}&units=metric'

    response = requests.get(my_url)

    my_data = response.json()
    
    with open ('my_city_weather_info.csv', 'a') as f:
        f.write('\n' + ','.join([my_data['name'], my_data['weather'][0]['description'],str(my_data['main']['temp']),str(my_data['main']['humidity']),
        str(my_data['wind']['speed'])]))


#exercise3



fayl_nomi = "books.json"

if not os.path.exists(fayl_nomi):
    with open(fayl_nomi, "w", encoding="utf-8") as f:
        json.dump([], f)

with open(fayl_nomi, "r", encoding="utf-8") as f:
    books = json.load(f)

book_id = input("Kitob ID: ")
title = input("Kitob nomi: ")
author = input("Muallif: ")

yangi_kitob = {
    "id": book_id,
    "title": title,
    "author": author
}

books.append(yangi_kitob)

with open(fayl_nomi, "w", encoding="utf-8") as f:
    json.dump(books, f, ensure_ascii=False, indent=2)

print("Natija qo‘shildi ")




#exercise4

with open ('my_movies.csv', 'w') as f:
    f.write('Movie_name, Year_released, Type_of_movie')

my_title = input("Kino nomidagi biror so'zni kiriting ")
my_url = f'http://www.omdbapi.com/?s={my_title}&apikey=6910c909'

response = requests.get(my_url)

my_data = response.json()

for dict in my_data['Search']:
    with open('my_movies.csv', 'a') as f:
        f.write('\n'+(',').join([dict['Title'], dict['Year'], dict['Type']]))
