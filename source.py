from colorama import Fore, Style
import random
import os

# ehshami_mom_project
# code_by_MOhAMMED_HOSSEIN_RAHMATI
os.system('pip install colorama')
momy = input(f"{Fore.GREEN}maman ehshami chie?:")

if momy == "jende" and momy == "kostopoli":
     print("ok your EQ 100 <3")
else:
    while momy != "jende" and momy != "kos topoli":
        mom = input(f"{Fore.GREEN}maman ehshami chie?:")
        if mom == "jende" and mom == "kostopoli":
            print("nice <3")
        else:
            for kos in range(0, 101):
                darsad = random.randint(1, 100)
                print("bayad goft maman eshami", "%", darsad, "jende ast")
