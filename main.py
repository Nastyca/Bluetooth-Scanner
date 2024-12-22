import os
import asyncio
from bleak import BleakScanner
from colorama import Fore, init

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()

init(autoreset=True)

os.system("title Scan Bluetooth by Nastyca")

async def scan():
    print(f"{Fore.RESET}[/] Scan en cours...\n")
    scan_bluetooth = BleakScanner()
    try:
        appareils = await scan_bluetooth.discover()
        for appareil in appareils:
            print(f"{Fore.GREEN}Nom : {Fore.RESET}{appareil.name} {Fore.GREEN}- MAC : {Fore.RESET}{appareil.address}")
    except Exception as e:
        print(f"{Fore.RED}[-] Erreur : {Fore.RESET}{e}")

asyncio.run(scan())
