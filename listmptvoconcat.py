import os
import sys
import subprocess
from pathlib import Path
import datetime


def concatenar_arquivos():
    while True:
        print("\n" + "=" * 60)
        print("LISTMPTVO CONCAT".center(60))
        print("=" * 60)
        print("1 - Escolher extensão e concatenar")
        print("2 - Concatenar todas as extensões disponíveis")
        print("3 - Sair")

        opcao = input("\nDigite sua opção: ")

        if opcao == "1":
            processar_extensao()
        elif opcao == "2":
            todas_extensoes()
        elif opcao == "3":
            print("\nRetornando ao menu do AnalystToolBox...")
            subprocess.Popen(['python', 'menu.py'], shell=True)
            sys.exit(0)
        else:
            print("\nOpção inválida! Tente novamente.")


def processar_extensao():
    ext = input("\nDigite a extensão dos arquivos (ex: mag, txt, csv): ").strip().lower()

    if not ext.startswith("."):
        ext = f".{ext}"

    diretorio = Path(input("Digite o caminho do diretório: ").strip())
    arquivos = list(diretorio.glob(f"*{ext}"))

    if not arquivos:
        print(f"\nNenhum arquivo {ext} encontrado no diretório!")
        return

    arquivos_ordenados = sorted(
        arquivos,
        key=lambda x: os.path.getctime(x),
        reverse=False
    )

    print(f"\nArquivos encontrados ({len(arquivos)}):")
    for i, arq in enumerate(arquivos_ordenados, 1):
        # Obtem a data de criação formatada #
        timestamp_criacao = os.path.getctime(arq)
        data_criacao = datetime.datetime.fromtimestamp(timestamp_criacao)
        data_formatada = data_criacao.strftime('%d/%m/%Y %H:%M:%S')

        # Obtem tamanho formatado #
        tamanho = arq.stat().st_size

        print(f"{i:02d} - {data_formatada} | {arq.name} | {tamanho:,} bytes".replace(",", "."))

    confirmar = input("\nConcatenar estes arquivos? (s/n): ").lower()
    if confirmar != 's':
        return

    saida = input("Digite o nome do arquivo de saída: ").strip()
    if not saida:
        saida = f"concatenado{ext}"

    try:
        with open(diretorio / saida, 'w', encoding='utf-8') as arquivo_saida:
            for arquivo in arquivos_ordenados:
                with open(arquivo, 'r', encoding='utf-8') as f:
                    arquivo_saida.write(
                        f"--- Arquivo original: {arquivo.name} | Criado em: {datetime.datetime.fromtimestamp(os.path.getctime(arquivo)).strftime('%d/%m/%Y %H:%M:%S')} ---\n")
                    arquivo_saida.write(f.read())
                    arquivo_saida.write("\n\n")

        print(f"\n✓ Concatenação concluída! Arquivo salvo como: {saida}")
        print(f"Caminho completo: {diretorio / saida}")

    except Exception as e:
        print(f"\nErro durante a concatenação: {str(e)}")

def todas_extensoes():
    diretorio = Path(input("Digite o caminho do diretório: ").strip())

    DIRETORIO_TRABALHO = diretorio
    EXTENSOES_ALVO = ['.btr', '.vel', '.ori', '.mag', '.dia', '.mil']
    PREFIXO_SAIDA = "CONCATENADO"

    # Criar diretório de trabalho se não existir
    DIRETORIO_TRABALHO.mkdir(parents=True, exist_ok=True)

    # Processar cada extensão #
    for extensao in EXTENSOES_ALVO:
        # Buscar e ordenar arquivos por tempo #
        arquivos = sorted(
            DIRETORIO_TRABALHO.glob(f'*{extensao}'),
            key=lambda x: os.path.getctime(x)
        )

        if not arquivos:
            print(f"Nenhum arquivo {extensao} encontrado. Pulando...")
            continue

        # Criar nome do arquivo de saída #
        mais_antigo = arquivos[0].stem
        nome_saida = f"{PREFIXO_SAIDA}_{mais_antigo}{extensao}"

        # Executar concatenação
        try:
            with open(DIRETORIO_TRABALHO / nome_saida, 'w', encoding='utf-8') as saida:
                for arquivo in arquivos:
                    with open(arquivo, 'r', encoding='utf-8') as entrada:
                            saida.write(entrada.read())

            print(f"✓ {extensao.upper()}: {len(arquivos)} arquivos -> {nome_saida}")

        except Exception as e:
            print(f"Erro ao processar {extensao}: {str(e)}")

    print("\nProcesso de concatenação concluído!")

if __name__ == "__main__":
    concatenar_arquivos()