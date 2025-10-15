# Monitor Server ALEPH - Versiunea Actualizată

## 🔧 Modificări Efectuate

### 1. **Butoane Mărite**
   - Butonul "Pornire Monitor" - mărit la `padx=30, pady=15`
   - Butonul "Repornire Manuală" - mărit la `padx=20, pady=12` și font bold
   - Butonul "Deconectare" - mărit la `padx=20, pady=12` și font bold
   - Textul butoanelor este acum mai vizibil și ușor de citit

### 2. **Ordinea Corectă a Operațiunilor**
   Secvența de repornire urmează acum pașii corecți:
   1. Conectare SSH la server
   2. Setare dată în trecut (2012) pentru licență
   3. Așteptare 30 secunde pentru inițializare servicii
   4. **PRIMA DATĂ: Deschidere catalog ONLINE în browser** (http://75.186.123.40:8991/F)
   5. **APOI: Lansare Catalog.exe cu autentificare automată**
   6. Revenire la data curentă
   7. Redeschidere catalog online după resetarea datei
   8. Verificare finală

### 3. **Funcționalități Adăugate**
   - Import `webbrowser` pentru deschidere automată browser
   - Verificare disponibilitate `pyautogui` înainte de autentificare automată
   - Mesaje mai clare în jurnal despre ordinea operațiunilor
   - Timp de așteptare mărit pentru încărcare aplicații

## 📦 Instalare și Compilare

### Pasul 1: Instalare Dependențe
```bash
pip install paramiko requests pyautogui pyinstaller pillow
```

### Pasul 2: Compilare Executabil
```bash
python build_exe_fixed.py
```

### Pasul 3: Distribuire
Executabilul va fi generat în `dist/AlephMonitor.exe` și poate fi distribuit utilizatorilor.

## 🚀 Utilizare

1. **Prima Rulare:**
   - Introduceți username-ul și parola pentru Catalog ALEPH
   - Bifați "Salvează credențialele" pentru a nu le reintroduce data viitoare

2. **Monitorizare Automată:**
   - Aplicația verifică serverul la fiecare 2 minute
   - Dacă serverul nu răspunde de 2 ori consecutiv, pornește automat secvența de repornire
   - Browser-ul se deschide automat pentru catalog online
   - Catalog.exe se lansează și se autentifică automat

3. **Repornire Manuală:**
   - Folosiți butonul "Repornire Manuală" pentru a forța o repornire
   - Urmează aceeași secvență ca și repornirea automată

## ⚠️ Cerințe Sistem

- Windows OS
- Catalog.exe instalat la: `C:\BEBE\acasa\bin\Catalog.exe`
- Acces la server SSH: 75.186.123.40
- Browser web pentru catalog online
- Python (doar pentru dezvoltare, nu pentru utilizatori finali)

## 📝 Note Importante

- Parola SSH este integrată în executabil (criptată)
- Fiecare utilizator își salvează propriile credențiale local
- Fișierul de log: `aleph_monitor.log` în același director cu executabilul
- Credențialele salvate: `users.json` în același director cu executabilul

## 🐛 Depanare

Dacă autentificarea automată nu funcționează:
1. Verificați că pyautogui este instalat
2. Măriți timpul de așteptare în `launch_catalog_with_credentials()`
3. Asigurați-vă că fereastra Catalog.exe este activă

Dacă browser-ul nu se deschide automat:
- URL-ul va fi afișat în jurnal pentru deschidere manuală
- Verificați setările firewall/antivirus

## 📧 Contact și Suport

Pentru probleme sau sugestii, contactați administratorul de sistem.
