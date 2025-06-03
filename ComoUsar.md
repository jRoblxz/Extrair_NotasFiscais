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

# 🛠️ How to Use the NF-e Access Key Extractor

## 🚀 Step-by-Step Guide to Run

1. Access [Google Colab](https://colab.research.google.com/).
2. Copy and paste the project's Python code.
3. Run the cell to install the library:
   ```python
   !pip install PyMuPDF==1.23.2

   #Note: The functions files.upload() and files.download() are specific to Google Colab.
4. Upload the NF-e PDF files.
5. The script will extract the keys and generate a file named chaves_acesso_nfe.csv for download.
6. After extraction, the uploaded PDFs will be automatically removed from the environment.

## 🧠 How It Works

The script:
   - Opens the PDF using the PyMuPDF (fitz) library.
   - Extracts text from all PDF pages.
   - Uses a regular expression to locate any number with exactly 44 digits (NF-e access key format).
   - Saves the results in a DataFrame and exports it as a CSV file.
### 🗒️ Example of Regular Expression Used
      r'\b\d{44}\b'
This expression searches for any number with exactly 44 digits, separated by spaces or punctuation.
### 🧼 Automatic Cleanup
After generating the CSV, the script removes all .pdf files from the environment to avoid unnecessary storage.

## 🙋‍♂️ Author / Contact
Developed by [João Roblez](https://github.com/jRoblxz). <br>
Email: [João Roblez](mailto:joaoroblez76@gmail.com)   <br>
GitHub: [João Roblez](https://github.com/jRoblxz).  <br>
LinkedIn: [João Roblez](https://www.linkedin.com/in/joaoroblez).
