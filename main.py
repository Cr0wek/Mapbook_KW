
users:list=[
    {'name': 'Krzysztof', 'location': 'Wolomin', 'posts': 1},
    {'name': 'Bartek', 'location': 'Warszawa', 'posts': 4},
    {'name': 'Antek', 'location': 'Berlin', 'posts': 6},
    {'name': 'Kasia', 'location': 'Olsztyn', 'posts': 8},
    
]

for user in users:
    print(f'Twoj znajomy {user['name']} opublikowal z miejscowosci {user['location']} tyle postów: {user['posts']}')


