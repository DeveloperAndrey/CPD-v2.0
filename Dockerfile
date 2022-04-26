FROM python:3.9

ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
ADD . /app


RUN pip install -r requirements.txt


RUN apt-get update
RUN apt-get -y install nodejs
RUN apt-get -y install npm

RUN npm init --yes  --prefix ./frontend
RUN npm install --prefix ./frontend webpack webpack-cli
CMD ["npm", "run", "--prefix", "./frontend", "dev"]