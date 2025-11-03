from bs4 import BeautifulSoup
import requests

users:list=[
    {'name': 'Krzysztof', 'location': 'Wołomin', 'posts': 1, 'img_url':''},
    {'name': 'Bartek', 'location': 'Warszawa', 'posts': 4, 'img_url':''},
    {'name': 'Antek', 'location': 'Berlin', 'posts': 6, 'img_url':''},
    {'name': 'Kasia', 'location': 'Olsztyn', 'posts': 8, 'img_url':''},

]
def user_info(usersdata:list)->None:
    for user in usersdata:
        print(f'Twoj znajomy {user['name']} opublikowal z miejscowosci {user['location']} tyle postów: {user['posts']}')
        
def addUser(usersdata:list)->None:
    name:str=input("Podaj imie nowego znajomego: ")
    location:str=input("Podaj nazwe miejscowosci: ")
    posts:int=input("Podaj liczbe postow: ")
    image:str=input("Podaj link do obrazu: ")
    usersdata.append({"name":name, "location":location, "posts":posts, "img_url":image})
    
def removeUser(usersdata:list)->None:
    tmp_name:str=input("Podaj imie uzytkownika ktorego chcesz usunac: ")
    for n in usersdata:
        if n['name']==tmp_name:
            usersdata.remove(n)
            
def updateUser(usersdata:list)->None:
    tmp_name:str=input("Podaj imie uzytkownika ktorego chcesz zaktualizowac: ")
    for n in usersdata:
        if n['name']==tmp_name:
            n['name']=input("Podaj nowe imie: ")
            n['location']=input("Podaj nowa miejscowosc: ")
            n['posts']=int(input("Podaj nowa liczbe postow: "))
            n['img_url']=input("Podaj nowy link do obrazu: ")
            
def GetCoords(location:str)->list:  
    url:str=f'https://pl.wikipedia.org/wiki/{location}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response=requests.get(url, headers=headers)
    response_html=BeautifulSoup(response.text, 'html.parser')
    latitude=float(response_html.select('.latitude')[1].text.replace(',','.'))
    longitude=float(response_html.select('.longitude')[1].text.replace(',','.'))
    return [latitude, longitude]

def GetMap(usersdata:list)->None:
    import folium
    m= folium.Map(location=[52.21,21.15], zoom_start=3)
    for user in usersdata:
        folium.Marker(
        location=GetCoords(user["location"]),
        tooltip=user["name"],
        popup=f"<h4>{user["name"]}</h4> {user["location"]}, {user["posts"]}, <img src='{user["img_url"]}' alt='1'/>",
        icon=folium.Icon(icon="cloud"),
        ).add_to(m)
    m.save("index.html")
    
while True:
    print("\n===================MENU===================\n0. Wyjscie\n1. Wyswietl informacje o znajomych\n2. Dodaj znajomego\n3. Usun znajomego\n4. Aktualizuj znajomego\n5. Wyswietl mape\n==========================================")
    tmp_choice:int=int(input('Wybierz opcje menu: '))
    if tmp_choice==0:
        break
    if tmp_choice==1:
        print('Wybrano funkcje wyswietlania aktywnosci znajomych')
        user_info(users)
    if tmp_choice==2:
        print('Wybrano funkcje dodawania znajomego')
        addUser(users)
    if tmp_choice==3:
        print('Wybrano funkcje usuwania znajomego')
        removeUser(users)
    if tmp_choice==4:
        print('Wybrano funkcje aktyalizacji znajomego')
        updateUser(users)
    if tmp_choice==5:
        print('Wybrano funkcje wyświetlania mapy z uzytkownikami')
        GetMap(users)
        

    
