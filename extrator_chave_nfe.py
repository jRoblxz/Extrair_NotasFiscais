
import fitz  # PyMuPDF
import re
import os
import glob
import pandas as pd

# Este bloco só funcionará no Google Colab
try:
    from google.colab import files
    uploaded = files.upload()  # Fazer upload de arquivos (PDF)
except ImportError:
    print("Este script foi feito para ser executado no Google Colab.")

def extrair_chave_acesso(pdf_path):
    with fitz.open(pdf_path) as doc:
        texto = ""
        for page in doc:
            texto += page.get_text()
        # Regex para 44 dígitos
        chave = re.search(r'\b\d{44}\b', texto)
        return chave.group(0) if chave else "Chave não encontrada"

# Lista para armazenar os resultados
dados = []

try:
    for nome_arquivo in uploaded.keys():
        chave = extrair_chave_acesso(nome_arquivo)
        dados.append({
            'arquivo': nome_arquivo,
            'chave_acesso': chave
        })

    # Criar DataFrame e salvar como CSV com separador ; e formato de texto
    df = pd.DataFrame(dados)

    # Adiciona apóstrofo antes da chave (força texto no Excel/WPS)
    df['chave_acesso'] = df['chave_acesso'].apply(lambda x: f"'{x}")

    # Salvar CSV
    df.to_csv("chaves_acesso_nfe.csv", index=False, sep=';')

    # Download do CSV
    files.download("chaves_acesso_nfe.csv")

    # Excluir arquivos PDF
    for pdf_file in glob.glob("*.pdf"):
        os.remove(pdf_file)
except:
    pass
