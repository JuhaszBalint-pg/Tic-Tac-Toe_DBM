import subprocess
import sys
import os


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


# =================================================================
#                SZERKESZTHETŐ BEÁLLÍTÁSOK RÉSZE
# =================================================================

APP_PATH = "demo.py"     # Ide írd a fő program nevét/elérhetőségét

# =================================================================
#                SZERKESZTHETŐ RÉSZ VÉGE
# ================================================================= 

APP_PATH=os.path.abspath(APP_PATH)

try:
    import blessed
except ImportError:
    print("A program futtatásához az alábbi könyvtár(ak) telepítése szükséges:")
    print("    • blessed")
    while True:
        answer = input('Szeretné telepíteni őket? ["yes"/"no"] ').lower()
        if answer == "yes" or answer == "y":
                install("blessed")
                break
        elif answer == "no" or answer == "n":
            print("A program működése során hibába ütközött")
            sys.exit()

print("Loading....")
subprocess.run([sys.executable, APP_PATH])

