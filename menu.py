import subprocess
import sys
import os

def mostrar_menu():
    while True:
        print("\n" + "=" * 50)
        print("Analyst Tool Box".center(50))
        print("=" * 50)
        print("\n1. Executar PitFixer")
        print("\n2. Executar LISTMPTVO Concat")
        print("\n3. Executar Near Weld")
        print("\n4. Outra Automação")
        print("\n8. Sair")

        acoes = {
            "1": "pitfixer.py",
            "2": "listmptvoconcat.py"
            "3": "nearweld.py"
        }
        escolha = input("\nDigite a opção desejada: ").strip()
        if escolha in acoes:
            subprocess.run([sys.executable, acoes[escolha]])
        elif escolha in {"4", "5", "6", "7"}:
            print("\nFuncionalidade em desenvolvimento!")
        elif escolha == "8":
            print("\nSaindo do sistema...")
            break
        else:
            print("\nOpção inválida!")

if __name__ == "__main__":
    mostrar_menu()