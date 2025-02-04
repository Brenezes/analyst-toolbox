import sqlite3
import csv
import os
import sys
import subprocess
from datetime import datetime


class DefectMatcher:
    """Ferramenta para correlação de defeitos em bancos de dados de inspeção"""

    def __init__(self, caminho_banco: str):
        self.caminho_banco = caminho_banco
        self.conexao = None
        self.log_file = None
        self.campos_mod = ['id', 'tipo', 'posAxiIni', 'posAxiFim', 'prof', 'posAng', 'ie']
        self.campos_comp = ['id', 'tipo', 'posAxi', 'prof', 'posAng', 'ie']

    def __enter__(self):
        self.conectar()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fechar_conexao()

    def conectar(self):
        """Estabelece conexão com o banco de dados"""
        try:
            self.conexao = sqlite3.connect(self.caminho_banco)
            self.conexao.row_factory = sqlite3.Row
        except sqlite3.Error as erro:
            raise RuntimeError(f"Erro ao conectar: {erro}") from erro

    def fechar_conexao(self):
        """Fecha a conexão se estiver ativa"""
        if self.conexao:
            self.conexao.close()

    def iniciar_log(self, operacao: str):
        """Configura arquivo de log com timestamp"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        self.log_file = f"DefectMatcher_{operacao}_{timestamp}.csv"

    def criar_log(self, evento, resultado):
        """Registra correlação no arquivo CSV"""
        with open(self.log_file, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';')

            if f.tell() == 0:
                header = [f"{c}_mod" for c in self.campos_mod] + [f"{c}_comp" for c in self.campos_comp]
                writer.writerow(header)

            linha = [evento[c] for c in self.campos_mod] + [resultado[c] for c in self.campos_comp]
            writer.writerow(linha)

    def executar_consulta(self, tabela_mod: str, tabela_comp: str, modo: str = 'relatorio'):
        """
        Executa a análise de correlação entre as tabelas

        Args:
            tabela_mod (str): Tabela a ser modificada/analisada
            tabela_comp (str): Tabela de referência
            modo (str): 'relatorio' ou 'atualizar'
        """
        try:
            with self.conexao:
                cursor = self.conexao.cursor()

                query_base = f"""
                    SELECT {', '.join(self.campos_mod)}
                    FROM {tabela_mod}
                """

                query_comp = f"""
                    SELECT {', '.join(self.campos_comp)}
                    FROM {tabela_comp}
                    WHERE tipo = ?
                      AND posAxi BETWEEN ? AND ?
                      AND prof BETWEEN ? AND ?
                      AND posAng BETWEEN ? AND ?
                    LIMIT 1
                """

                query_update = f"""
                    UPDATE {tabela_mod}
                    SET ie = ?
                    WHERE id = ?
                """

                cursor.execute(query_base)
                registros = cursor.fetchall()
                total = 0

                for reg in registros:
                    # Cálculo dos ranges
                    axi_ini = reg['posAxiIni'] - 2
                    axi_fim = reg['posAxiFim'] + 2
                    prof_min = reg['prof'] - 10
                    prof_max = reg['prof'] + 10
                    ang_min = reg['posAng'] - 8.0
                    ang_max = reg['posAng'] + 8.0

                    cursor.execute(query_comp, (
                        reg['tipo'],
                        axi_ini,
                        axi_fim,
                        prof_min,
                        prof_max,
                        ang_min,
                        ang_max
                    ))

                    resultado = cursor.fetchone()

                    if resultado:
                        total += 1
                        self.criar_log(reg, resultado)

                        if modo == 'atualizar':
                            cursor.execute(query_update, (resultado['ie'], reg['id']))

                print(f"\nRegistros correlacionados: {total}")
                print(f"Log gerado: {self.log_file}")

                if modo == 'atualizar':
                    print("Atualização do campo IE concluída!")

        except sqlite3.Error as erro:
            raise RuntimeError(f"Erro na análise: {erro}") from erro


def mostrar_menu():
    """Exibe o menu interativo"""
    print("\n=== DefectMatcher - Menu Principal ===")
    print("1. Gerar Relatório de Correlação (apenas leitura)")
    print("2. Executar Atualização do Campo IE")
    print("3. Sair")
    return input("Escolha uma opção (1-3): ").strip()


def main():
    print("\nDefect Matcher v1.0\nAutor: [Breno Menezes]")

    caminho_banco = input("Caminho do banco de dados: ").strip()
    tabela_mod = input("Nome da tabela principal: ").strip()
    tabela_comp = input("Nome da tabela de referência: ").strip()

    with DefectMatcher(caminho_banco) as dm:
        while True:
            escolha = mostrar_menu()

            if escolha == '1':
                dm.iniciar_log('RELATORIO')
                dm.executar_consulta(tabela_mod, tabela_comp, 'relatorio')
                input("\nPressione Enter para continuar...")

            elif escolha == '2':
                confirmacao = input("Tem certeza que deseja atualizar os dados? (s/n): ").lower()
                if confirmacao == 's':
                    dm.iniciar_log('ATUALIZACAO')
                    dm.executar_consulta(tabela_mod, tabela_comp, 'atualizar')
                input("\nPressione Enter para continuar...")

            elif escolha == '3':
                print("\nRetornando ao menu do AnalystToolBox...")
                subprocess.Popen(['python', 'menu.py'], shell=True)
                sys.exit(0)

            else:
                print("\nOpção inválida!")
                input("Pressione Enter para continuar...")


if __name__ == "__main__":
    main()