⸻

🧾 API - Extração de Pedidos de Compra (PDF → JSON)

API desenvolvida em Python que automatiza a leitura de arquivos PDF contendo pedidos de compra. Ela extrai as principais informações — como número do pedido, códigos dos produtos, quantidades e valores — e retorna os dados em formato JSON, prontos para serem integrados ao sistema da empresa.

⸻

🚀 Funcionalidades
	•	📁 Verifica automaticamente se há novos PDFs na pasta monitorada
	•	🧠 Extrai e padroniza os dados dos pedidos (número, produtos, quantidades, preços)
	•	🔄 Retorna os dados formatados em JSON para integração com sistemas internos
	•	🌐 Disponível via API com Flask
	•	🧪 Código de teste incluído usando requests para simular chamadas e salvar os JSONs em uma pasta - disponíveis na pasta “testes”

⸻

🛠 Tecnologias
	•	Python 3
	•	Flask
	•	pdfplumber (para extração de texto dos PDFs)
	•	Regex

⸻

⚠️ Observação

O projeto está configurado para funcionar com um modelo de pedido “teste” específico. Caso o layout do PDF seja diferente, será necessário ajustar a lógica de extração e padronização dos dados — esse ajuste deve ser feito no arquivo funcoes.py, dentro da função standardize_text.

⸻

▶️ Como usar

# Clonar o repositório
git clone https://github.com/felipemonsef10/order-extract-api/

# Entrar na pasta do projeto
cd order-extract-api

# (Opcional) Criar um ambiente virtual
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows

# Instalar as dependências
pip install -r requirements.txt

# Rodar a API
python app.py

Depois, basta acessar:

http://localhost:5000/pedidos?folder=caminho_da_pasta


⸻

## 👨‍💻 Felipe Gabriel Monsef

Desenvolvido por Felipe Monsef. 
