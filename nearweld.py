import sqlite3
import os
import sys
import subprocess


class GerenciadorBancoDados:

    def __init__(self, caminho_banco: str):
        self.caminho_banco = caminho_banco
        self.conexao = None

    def __enter__(self):
        self.conectar()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fechar_conexao()

    def conectar(self):
        # Estabelece conexão com o banco de dados #
        try:
            self.conexao = sqlite3.connect(self.caminho_banco)
        except sqlite3.Error as erro:
            raise RuntimeError(f"Erro ao conectar: {erro}") from erro

    def fechar_conexao(self):
        # Fecha a conexão se estiver ativa #
        if self.conexao:
            self.conexao.close()
            self.conexao = None

def atualizar_tipo(self, tabela_defeitos: str, distancia: int):
    # Atualiza o campo 'tipo' de registros na tabela de defeitos que estejam
    # até `distancia` mm de uma solda (baseado em posAxi).
    
    if not self.conexao:
        raise RuntimeError("Conexão não estabelecida.")

    query = f"""
        UPDATE {tabela_defeitos}
        SET tipo = 'PS'
        WHERE EXISTS (
            SELECT 1
            FROM solda
            WHERE ABS(solda.posAxi - {tabela_defeitos}.posAxi) <= ?
        );
    """

    try:
        with self.conexao:
            cursor = self.conexao.cursor()
            cursor.execute(query, (distancia,))
            print(f"\nRegistros atualizados: {cursor.rowcount}")
    except sqlite3.Error as erro:
        raise RuntimeError(f"Erro na atualização: {erro}") from erro


def exibir_menu():
    print("\n" + "=" * 40)
    print("NEAR WELD - Filtra anomalias em solda\n Autor: [Whilamys Pontes] & Modificado por: [Breno Menezes]\nVersão: V1.8")
    print("=" * 40)
    print("1. Filtrar anomalias próximas a soldas")
    print("2. Retornar ao Menu Principal")
    print("=" * 40)


def obter_distancia():
    while True:
        entrada = input("Distância máxima da solda (mm): (Ex: 6mm = 60) ").strip()
        try:
            distancia = int(entrada)
            if distancia > 0:
                return distancia
            print("A distância deve ser maior que zero!")
        except ValueError:
            print("Por favor, insira um número inteiro válido!")


def filtrar_anomalias():
    print("\n" + "-" * 40)
    print("Filtragem de Anomalias Próximas a Soldas")
    print("-" * 40)

    caminho_banco = input("Caminho do banco de dados (.prdb): ").strip()
    tabela_defeitos = input("Nome da tabela de defeitos: ").strip()
    distancia = obter_distancia()

    if not os.path.exists(caminho_banco):
        print("\nErro: Arquivo de banco de dados não encontrado!")
        return

    try:
        with GerenciadorBancoDados(caminho_banco) as gerenciador:
            gerenciador.atualizar_tipo(tabela_defeitos, distancia)
        print("\nOperação concluída com sucesso!")
    except Exception as e:
        print(f"\nErro durante a operação: {str(e)}")


def main():
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ").strip()

        if escolha == '1':
            filtrar_anomalias()
            input("\nPressione Enter para continuar...")
        elif escolha == '2':
            print("\nRetornando ao menu do AnalystToolBox...")
            subprocess.Popen(['python', 'menu.py'], shell=True)
            sys.exit(0)
        else:
            print("\nOpção inválida! Tente novamente.")
            input("Pressione Enter para continuar...")


if __name__ == "__main__":
    main()
