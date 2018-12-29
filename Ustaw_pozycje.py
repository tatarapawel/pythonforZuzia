<<<<<<< HEAD
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
wprowadzone_pozycje=False
while wprowadzone_pozycje==False:
    try:
        poz_x = int(input("Podaj pozycje x:"))
        poz_y = int(input("Podaj pozycje y:"))
        poz_z = int(input("Podaj pozycje z:"))
        wprowadzone_pozycje=True
    except:
        print("Niepoprawna wartość. Wprowdź ponownie")
mc.player.setPos(poz_x,poz_y,poz_z)
=======
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
wprowadzone_pozycje=False
while wprowadzone_pozycje==False:
    try:
        poz_x = int(input("Podaj pozycje x:"))
        poz_y = int(input("Podaj pozycje y:"))
        poz_z = int(input("Podaj pozycje z:"))
        wprowadzone_pozycje=True
    except:
        print("Niepoprawna wartość. Wprowdź ponownie")
mc.player.setPos(poz_x,poz_y,poz_z)
>>>>>>> be4f46475f2468e161b19bd61b6ff6ccc44af397
