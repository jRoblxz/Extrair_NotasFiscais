# 🛠️ Como Usar o Extrator de Chave de Acesso de NF-e

## 🚀 Passo a Passo para Executar

1. Acesse o [Google Colab](https://colab.research.google.com/).
2. Copie e cole o código Python do projeto.
3. Execute a célula de instalação da biblioteca:
   ```python
   !pip install PyMuPDF==1.23.2
   
   #Observação: A função files.upload() e files.download() são específicas do Google Colab.
4. Faça upload dos arquivos PDF de NF-e.
5. O script irá extrair a chave e gerar um arquivo chaves_acesso_nfe.csv para download.
6. Após a extração, os PDFs enviados serão removidos automaticamente do ambiente.

## 🧠 Como Funciona

O script:
   - Abre o PDF com a biblioteca PyMuPDF (fitz).
   - Extrai o texto de todas as páginas do PDF.
   - Usa uma expressão regular para localizar qualquer número com exatamente 44 dígitos (formato da chave de acesso da NF-e).
   - Salva os resultados em um DataFrame e exporta como CSV.
### 🗒️ Exemplo de Expressão Regular Usada 
      r'\b\d{44}\b'
Essa expressão busca qualquer número com exatamente 44 dígitos, separado por espaços ou pontuações.
### 🧼 Limpeza automática
Após gerar o CSV, o script remove todos os arquivos .pdf do ambiente para evitar armazenamento desnecessário.

## 🙋‍♂️ Autor / Contatos
Desenvolvido por [João Roblez](https://github.com/jRoblxz). <br>
E-mail: [João Roblez](mailto:joaoroblez76@gmail.com)   <br>
GitHub: [João Roblez](https://github.com/jRoblxz).  <br>
LinkedIn: [João Roblez](https://www.linkedin.com/in/joaoroblez).

