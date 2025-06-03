# 🔍 Extrator de Chave de Acesso de NF-e (Nota Fiscal Eletrônica) via PDF

Este projeto em Python permite extrair automaticamente a **chave de acesso de 44 dígitos** de arquivos PDF de Notas Fiscais Eletrônicas (NF-e). Ideal para automatizar a leitura de chaves em grandes volumes de documentos.

## 📌 Funcionalidades

- Upload de múltiplos arquivos PDF diretamente via Google Colab.
- Extração da chave de acesso usando expressão regular.
- Exportação dos dados para um arquivo CSV formatado para Excel/WPS.
- Remoção automática dos arquivos PDF após a extração.

## 📁 Exemplo de saída (CSV)

| arquivo           | chave_acesso                   |
|-------------------|-------------------------------|
| nota1.pdf         | '12345678901234567890123456789012345678901234 |
| nota2.pdf         | '98765432109876543210987654321098765432109876 |

> O apóstrofo (`'`) inicial garante que o Excel/WPS interprete a chave como texto.

---

## ⚙️ Requisitos

- Python 3.7+
- Google Colab (ou ambiente Jupyter compatível)
- Bibliotecas:

      pip install PyMuPDF==1.23.2 pandas

============================================================================================
# 🔍 NF-e (Electronic Invoice) Access Key Extractor via PDF

This Python project automatically extracts the **44-digit access key** from PDF files of Brazilian Electronic Invoices (NF-e). Ideal for automating key reading from large volumes of documents.

## 📌 Features

- Upload multiple PDF files directly via Google Colab.
- Extract access keys using regular expressions.
- Export data to a CSV file formatted for Excel/WPS.
- Automatically delete PDF files after extraction.

## 📁 Output Example (CSV)

| file              | access_key                     |
|-------------------|-------------------------------|
| nota1.pdf         | '12345678901234567890123456789012345678901234 |
| nota2.pdf         | '98765432109876543210987654321098765432109876 |

> The initial apostrophe (`'`) ensures that Excel/WPS interprets the key as text.

---

## ⚙️ Requirements

- Python 3.7+
- Google Colab (or compatible Jupyter environment)
- Libraries:

```bash
pip install PyMuPDF==1.23.2 pandas
