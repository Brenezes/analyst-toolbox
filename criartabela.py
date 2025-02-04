import sqlite3
from typing import Optional


class GerenciadorTabelasAnomalias:

    @staticmethod
    def gerar_sql_tabela(nome_tabela: str) -> str:
        """Gera o SQL para criação da tabela de anomalias"""
        return f"""
        CREATE TABLE IF NOT EXISTS {nome_tabela} (
            classe INTEGER NOT NULL,
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nometab CHAR NOT NULL,
            nometabanom CHAR,
            tsf CHAR NOT NULL,
            posAxi INTEGER NOT NULL,
            posAng DECIMAL(10,2) NOT NULL,
            tipo CHAR,
            compr INTEGER,
            larg INTEGER,
            prof INTEGER,
            profMM DECIMAL(10,2),
            profPerc DECIMAL(10,2),
            ie CHAR,
            comentario CHAR,
            numAnom INTEGER,
            numElementosAnom INTEGER,
            numCanaisAnom INTEGER,
            numCanaisFerramenta INTEGER,
            passo DECIMAL(10,2),
            posAxiIni INTEGER,
            posAxiFim INTEGER,
            canalIni INTEGER,
            canalFim INTEGER,
            canalMax INTEGER,
            oriMax DECIMAL(10,2),
            distSldAnt INTEGER,
            distSldPost INTEGER,
            distSldProx INTEGER,
            idSldAnt INTEGER,
            prB31G DECIMAL(10,2),
            prB31GMod DECIMAL(10,2),
            prRPA DECIMAL(10,2),
            prKastner DECIMAL(10,2),
            prDNV DECIMAL(10,2) DEFAULT 0,
            prSegura DECIMAL(10,2),
            erf DECIMAL(10,2),
            diamTubo DECIMAL(10,2),
            espTubo DECIMAL(10,2),
            dimPOF INTEGER,
            posGeografica CHAR,
            dimAuto INTEGER NOT NULL DEFAULT 0,
            idAnomOrig CHAR
        );
        """

    @classmethod
    def criar_tabela(cls, caminho_banco: str, nome_tabela: str) -> bool:
        """
        Cria uma nova tabela de anomalias no banco de dados

        Args:
            caminho_banco (str): Caminho para o arquivo do banco de dados
            nome_tabela (str): Nome da tabela a ser criada

        Returns:
            bool: True se a tabela foi criada com sucesso, False caso contrário
        """
        try:
            with sqlite3.connect(caminho_banco) as conn:
                cursor = conn.cursor()

                # Gera o SQL específico para a tabela
                sql = cls.gerar_sql_tabela(nome_tabela)

                # Executa o comando SQL
                cursor.execute(sql)
                print(f"Tabela {nome_tabela} criada com sucesso!")
                return True

        except sqlite3.Error as error:
            print(f"Erro ao criar tabela: {error}")
            return False


if __name__ == "__main__":
    # Configurações
    BANCO_DADOS = "meu_banco.prdb"
    NOME_TABELA = "anom_create"  # Altere para o nome desejado

    # Cria a tabela
    sucesso = GerenciadorTabelasAnomalias.criar_tabela(
        caminho_banco=BANCO_DADOS,
        nome_tabela=NOME_TABELA
    )

    if sucesso:
        print("Operação concluída com sucesso!")
    else:
        print("Falha na criação da tabela!")