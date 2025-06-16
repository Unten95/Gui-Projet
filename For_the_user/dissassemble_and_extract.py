import marshal
import dis
import io
import sys
import os

def main():
    if len(sys.argv) < 2:
        print("Utilisation : python script.py fichier.pyc")
        return

    pyc_path = sys.argv[1]

    if not os.path.isfile(pyc_path):
        print(f"Le fichier '{pyc_path}' n'existe pas.")
        return

    try:
        with open(pyc_path, "rb") as f:
            f.read(16)  # Ignorer l'en-tête pour Python 3.7+ (dont 3.11)
            code = marshal.load(f)
    except Exception as e:
        print(f"Erreur lors du chargement du fichier .pyc : {e}")
        return

    output = io.StringIO()
    original_stdout = sys.stdout
    sys.stdout = output

    dis.dis(code)

    sys.stdout = original_stdout

    output_file = "disassembled.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(output.getvalue())

    print(f"Désassemblage terminé. Résultat enregistré dans '{output_file}'.")

if __name__ == "__main__":
    main()
