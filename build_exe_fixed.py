# build_exe.py
# Script pentru crearea executabilului ALEPH Monitor

"""
INSTRUCȚIUNI DE FOLOSIRE:

1. Instalează dependențele necesare:
   pip install paramiko requests pyautogui pyinstaller pillow

2. Rulează acest script:
   python build_exe.py

3. Executabilul va fi creat în folder-ul 'dist/AlephMonitor.exe'

4. Distribuie executabilul - utilizatorii vor putea să-l ruleze fără Python instalat!
"""

import PyInstaller.__main__
import os
import sys

def create_icon():
    """Creează o iconiță simplă pentru aplicație."""
    try:
        from PIL import Image, ImageDraw

        # Creează o iconiță 256x256
        img = Image.new('RGBA', (256, 256), color=(52, 152, 219, 255))
        draw = ImageDraw.Draw(img)

        # Desenează un server/computer
        draw.rectangle([64, 80, 192, 176], fill=(255, 255, 255, 255))
        draw.rectangle([80, 96, 176, 112], fill=(46, 204, 113, 255))
        draw.rectangle([80, 128, 176, 144], fill=(52, 152, 219, 255))
        draw.ellipse([112, 188, 144, 220], fill=(255, 255, 255, 255))

        img.save('aleph_icon.ico', format='ICO')
        print("Iconita creata: aleph_icon.ico")
        return 'aleph_icon.ico'
    except Exception as e:
        print(f"Nu s-a putut crea iconita: {e}")
        return None

def build_executable():
    """Construiește executabilul folosind PyInstaller."""

    print("=" * 60)
    print("CREARE EXECUTABIL ALEPH MONITOR")
    print("=" * 60)

    # Creează iconița
    icon_path = create_icon()

    # Configurație PyInstaller
    pyinstaller_args = [
        'monitor-server-fixed.py',       # Fișierul principal actualizat
        '--onefile',                     # Un singur fișier executabil
        '--windowed',                    # Fără consolă (GUI mode)
        '--name=AlephMonitor',           # Numele executabilului
        '--clean',                       # Curăță fișierele temporare
        '--noconfirm',                   # Nu cere confirmare
    ]

    # Adaugă iconița dacă există
    if icon_path and os.path.exists(icon_path):
        pyinstaller_args.append(f'--icon={icon_path}')

    # Adaugă metadata
    pyinstaller_args.extend([
        '--version-file=version_info.txt',  # Dacă există
        # '--add-data=users.json;.',        # Comentat conform cererii utilizatorului
    ])

    print("\nPornire build PyInstaller...\n")

    try:
        PyInstaller.__main__.run(pyinstaller_args)

        print("\n" + "=" * 60)
        print("EXECUTABIL CREAT CU SUCCES!")
        print("=" * 60)
        print(f"\nLocatie: {os.path.abspath('dist/AlephMonitor.exe')}")
        print("\nINSTRUCTIUNI DISTRIBUIRI:")
        print("   1. Copiază fișierul 'dist/AlephMonitor.exe' pe orice calculator")
        print("   2. La prima rulare, fiecare utilizator va introduce:")
        print("      - Username-ul său pentru Catalog ALEPH")
        print("      - Parola sa pentru Catalog ALEPH")
        print("   3. Credențialele pot fi salvate pentru utilizări viitoare")
        print("   4. Monitorizarea va porni automat după autentificare")
        print("\nIMPORTANT:")
        print("   - Executabilul contine parola SSH (criptata in exe)")
        print("   - Fiecare utilizator își păstrează propriile credențiale Catalog")
        print("   - Catalog.exe trebuie să existe la: C:\\AL500\\catalog\\bin\\Catalog.exe")
        print("   - Browser-ul se va deschide automat pentru catalog online")
        print("\n" + "=" * 60)

    except Exception as e:
        print(f"\nEROARE la creare executabil: {e}")
        sys.exit(1)

def create_version_info():
    """Creează fișier cu informații despre versiune."""
    version_info = """# UTF-8
#
VSVersionInfo(
  ffi=FixedFileInfo(
    filevers=(1, 0, 0, 0),
    prodvers=(1, 0, 0, 0),
    mask=0x3f,
    flags=0x0,
    OS=0x40004,
    fileType=0x1,
    subtype=0x0,
    date=(0, 0)
  ),
  kids=[
    StringFileInfo(
      [
      StringTable(
        u'040904B0',
        [StringStruct(u'CompanyName', u'Biblioteca'),
        StringStruct(u'FileDescription', u'Monitor Server ALEPH'),
        StringStruct(u'FileVersion', u'1.0.0.0'),
        StringStruct(u'InternalName', u'AlephMonitor'),
        StringStruct(u'LegalCopyright', u'© 2025'),
        StringStruct(u'OriginalFilename', u'AlephMonitor.exe'),
        StringStruct(u'ProductName', u'ALEPH Server Monitor'),
        StringStruct(u'ProductVersion', u'1.0.0.0')])
      ]
    ),
    VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
  ]
)
"""

    try:
        with open('version_info.txt', 'w', encoding='utf-8') as f:
            f.write(version_info)
        print("Fisier versiune creat: version_info.txt")
    except Exception as e:
        print(f"Nu s-a putut crea fisierul de versiune: {e}")

if __name__ == "__main__":
    # Verifică dacă fișierul principal există
    if not os.path.exists('monitor-server-fixed.py'):
        print("EROARE: Nu gasesc fisierul 'monitor-server-fixed.py'!")
        print("   Asigură-te că ești în folderul corect și că fișierul există.")
        sys.exit(1)

    # Creează fișierul de versiune
    create_version_info()

    # Construiește executabilul
    build_executable()
