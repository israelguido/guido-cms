# Use uma imagem oficial do Python como base
FROM python:3.9-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copie os arquivos necessários para o container
COPY . /app

# Instale as dependências
RUN pip install --no-cache-dir -r app/requirements.txt

# Exponha a porta em que o Flask será executado
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["python", "main.py"]
