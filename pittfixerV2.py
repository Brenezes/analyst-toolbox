import sqlite3
import random
import sys

def recalcular_larg(compr):
    minimo = max(19, compr - 5)
    maximo = compr + 5
    if minimo > maximo:
        minimo, maximo = maximo, minimo  # Garante que minimo <= maximo
    return random.randint(minimo, maximo)

def gerar_nova_prof():
    return random.randint(28, 38)

def atualizar_script(caminho_banco):
    try:
        conn = sqlite3.connect(caminho_banco)
        cursor = conn.cursor()

        # Buscar eventos que atendem aos critérios
        cursor.execute("""
        SELECT id, prof, compr, larg FROM anom_esp
        WHERE prof > 35 AND larg <= 19
        """)

        eventos = cursor.fetchall()

        if not eventos:
            print("Nenhum evento encontrado.")
            return

        for evento in eventos:
            id_evento, prof, compr, larg = evento
            nova_larg = recalcular_larg(compr)
            nova_prof = gerar_nova_prof()

            cursor.execute("""
            UPDATE anom_esp
            SET prof = ?, larg = ?, comentario = ?
            WHERE id = ?
            """, (nova_prof, nova_larg, f"Prof original: {prof} -> {nova_prof}, Larg original: {larg} -> {nova_larg}", id_evento))

            print(f"Evento ID {id_evento} atualizado: prof {prof} -> {nova_prof}, larg {larg} -> {nova_larg}")

        conn.commit()
        print("Atualizações concluídas.")
    except Exception as e:
        conn.rollback()
        print(f"Erro: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <caminho_do_banco>")
        sys.exit(1)
    
    caminho_banco = sys.argv[1]
    atualizar_script(caminho_banco)

