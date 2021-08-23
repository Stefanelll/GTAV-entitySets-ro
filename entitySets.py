import xml.etree.ElementTree as ET
import os
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=False)

outputclear = open("output.txt", "w")
outputclear.write("Fisierul a fost resetat si noul output a fost creat")
outputclear.close()
output = open("output.txt", "a")

files = [x for x in os.listdir()
            if os.path.isfile(x)
                if x.endswith(".xml")
]

for x in range(len(files)):
    try:
        tree = ET.parse(files[x])
        root = tree.getroot()
        a = root.find('.//entitySets/Item')
        if a:
            print()
            print()
            print(Fore.LIGHTMAGENTA_EX + Back.LIGHTWHITE_EX + files[x])
            output.write("\n\n\n" + files[x] + "\n\n")
            for elements in root.findall('.//entitySets/Item'):
                    entitySetsName = elements.find('name').text
                    if entitySetsName:
                        print(Fore.LIGHTGREEN_EX + entitySetsName)
                        output.write(entitySetsName + "\n")
                    else:
                        print("Acest entitySets nu are un nume")
        else:
            os.remove(files[x])
            print(Fore.RED + Back.RESET + "Fisierul: " + files[x] + " a fost sters | Motiv: nu are entitySets")
    except:
        os.remove(files[x])
        print(Fore.RED + Back.RESET + "Fisierul: " + files[x] + " a fost sters | Motiv: nu poate fi deschis")
output.close()
print()
print()
print(Fore.CYAN + Back.RESET + "\n\n\nUn fisier a fost creat cu numele de: output.txt | in fisier vei gasi toate rezultatele cautarii tale\nCopiaza rezultatele din consola cu: CTRL + SHIFT + C " + Fore.LIGHTCYAN_EX + "sau" + Fore.CYAN +" (recomandat) utilizeaza fisierul care a fost creat\n")
print()
input("Apasa ENTER pentru a iesi")