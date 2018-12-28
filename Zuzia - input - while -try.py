imie=input("Podaj imie:")
print("Twoje imie: %s" %imie)

wprowadzono_Wiek=False

while not wprowadzono_Wiek:
    try:
        ile_lat=int(input("Ile masz lat:"))
        print("Masz lat: %s" %ile_lat)
        wprowadzono_Wiek=True
    except:
        print("Wiek musi być liczbą calkowita")
