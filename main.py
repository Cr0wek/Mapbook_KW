
users:list=[
    {'name': 'Krzysztof', 'location': 'Wolomin', 'posts': 1},
    {'name': 'Bartek', 'location': 'Warszawa', 'posts': 4},
    {'name': 'Antek', 'location': 'Berlin', 'posts': 6},
    {'name': 'Kasia', 'location': 'Olsztyn', 'posts': 8},
    
]
def user_info(usersdata:list)->None:
    for user in usersdata:
        print(f'Twoj znajomy {user['name']} opublikowal z miejscowosci {user['location']} tyle postów: {user['posts']}')
while True:
    tmp_choice:int=int(input('Wybierz opcje menu: '))
    if tmp_choice==0:
        break
    if tmp_choice==1:
        print('Wybrano funkcje wyswietlania aktywnosci znajomych')
        user_info(users)
    if tmp_choice==2:
        print('Wybrano funkcje dodawania znajomego')
    if tmp_choice==3:
        print('Wybrano funkcje usuwania znajomego')
    if tmp_choice==4:
        print('Wybrano funkcje aktyalizacji znajomego')

    
