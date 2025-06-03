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

```bash
pip install PyMuPDF==1.23.2 pandas
