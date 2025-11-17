from bs4 import BeautifulSoup
import requests

class User:
    def __init__(self, name:str, location:str, posts:int, img_url:str):
        self.name = name
        self.location = location
        self.posts = posts
        self.img_url = img_url
        self.coords = self.get_coords()
    
    def get_coords(self):
        from bs4 import BeautifulSoup
        import requests
        url:str=f'https://pl.wikipedia.org/wiki/{self.location}'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response=requests.get(url, headers=headers)
        response_html=BeautifulSoup(response.text, 'html.parser')
        latitude=float(response_html.select('.latitude')[1].text.replace(',','.'))
        longitude=float(response_html.select('.longitude')[1].text.replace(',','.'))
        return [latitude, longitude]


def user_info(usersdata:list)->None:
    for user in usersdata:
        print(f'Twoj znajomy {user.name} opublikowal z miejscowosci {user.location} tyle postów: {user.posts}')
        
def addUser(usersdata:list)->None:
    name:str=input("Podaj imie nowego znajomego: ")
    location:str=input("Podaj nazwe miejscowosci: ")
    posts:int=input("Podaj liczbe postow: ")
    image:str=input("Podaj link do obrazu: ")
    usersdata.append(User(name=name, location=location, posts=posts, img_url=image))
    
def removeUser(usersdata:list)->None:
    tmp_name:str=input("Podaj imie uzytkownika ktorego chcesz usunac: ")
    for n in usersdata:
        if n.name==tmp_name:
            usersdata.remove(n)
            
def updateUser(usersdata:list)->None:
    tmp_name:str=input("Podaj imie uzytkownika ktorego chcesz zaktualizowac: ")
    for n in usersdata:
        if n.name==tmp_name:
            n.name=input("Podaj nowe imie: ")
            n.location=input("Podaj nowa miejscowosc: ")
            n.posts=int(input("Podaj nowa liczbe postow: "))
            n.img_url=input("Podaj nowy link do obrazu: ")
            n.coords=n.get_coords()
            
def GetMap(usersdata:list)->None:
    import folium
    m= folium.Map(location=[52.21,21.15], zoom_start=3)
    for user in usersdata:
        folium.Marker(
        location=user.coords,
        tooltip=user.name,
        popup=f"<h4>{user.name}</h4> {user.location}, {user.posts}, <img src='{user.img_url}' alt='1'/>",
        icon=folium.Icon(icon="cloud"),
        ).add_to(m)
    m.save("index.html")
    
if __name__=="__main__":
    users_data=[]
    addUser(users_data)
    removeUser(users_data)