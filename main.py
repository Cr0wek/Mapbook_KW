from mapbook_lib.model import users    
from mapbook_lib.controller import user_info, addUser, removeUser, updateUser, GetMap

def main():
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
            
if __name__=="__main__":
    main()
        

    
