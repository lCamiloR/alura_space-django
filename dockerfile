FROM python:3.13.0a4-slim-bullseye
LABEL mantainer="https://github.com/lCamiloR"

# Essa variável de ambiente é usada para controlar se o Python deve 
# gravar arquivos de bytecode (.pyc) no disco. 1 = Não, 0 = Sim
ENV PYTHONDONTWRITEBYTECODE 1

# Define que a saída do Python será exibida imediatamente no console ou em 
# outros dispositivos de saída, sem ser armazenada em buffer.
# Em resumo, você verá os outputs do Python em tempo real.
ENV PYTHONUNBUFFERED 1

# Copia a pasta "alura-space" para dentro do container.
COPY alura-space /alura-space

# Entra na pasta alura-space no container
WORKDIR /alura-space

# A porta 8000 estará disponível para conexões externas ao container
# É a porta que vamos usar para o Django.
EXPOSE 8000

# RUN executa comandos em um shell dentro do container para construir a imagem. 
# O resultado da execução do comando é armazenado no sistema de arquivos da 
# imagem como uma nova camada.
# Agrupar os comandos em um único RUN pode reduzir a quantidade de camadas da 
# imagem e torná-la mais eficiente.
RUN apt-get update -y && \
  apt-get upgrade -y && \
  apt-get install python3-dev default-libmysqlclient-dev build-essential -y && \
  apt install pkg-config -y && \
  apt install libjpeg-dev zlib1g-dev -y && \
  python -m venv /venv && \
  /venv/bin/pip install --upgrade pip && \
  /venv/bin/pip install -r /alura-space/requirements.txt 

# Adiciona a pasta scripts e venv/bin 
# no $PATH do container.
ENV PATH="/venv/bin:$PATH"


# O docker file funcionou para a criação da imagem, mais ainda assim é preciso definir a porta de comunicação durante a execução do container
# docker run -it -p 8000:8000 custodian/alura-space:1.0 bash

# na hora de executar o django tbm é preciso definir uma rede diferente da localhost, pois isso faz o django conflitar com a maquina HOST
# python manage.py runserver 0.0.0.0:8000