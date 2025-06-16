# 🔍 Analyse d'un exécutable PyInstaller

Ce projet contient deux scripts utiles pour analyser un fichier `.exe` généré avec PyInstaller, afin d'extraire le code Python original ou désassembler un fichier `.pyc`.

-------

## 1. `pyinstxtractor.py`

### ➤ Description :
Ce script permet **d’extraire les fichiers internes** (notamment les `.pyc`) d’un exécutable généré avec **PyInstaller**, sans avoir besoin d’avoir PyInstaller installé.

### ➤ Utilisation :
Place-toi dans le dossier où se trouve ton `.exe`, puis exécute :

```bash
python pyinstxtractor.py nom_du_fichier.exe
```

-----------------------------------------------------

## 2. `dissassemble_and_extract.py`

### ➤ Description :
Ce script permet de désassembler un fichier .pyc afin d’obtenir les instructions du bytecode Python, et enregistre le résultat dans un fichier disassembled.txt.

### ➤ Utilisation :
Une fois les fichiers extraits, exécutez :

````bash
python dissassemble_and_extract.py chemin/vers/fichier.pyc
```