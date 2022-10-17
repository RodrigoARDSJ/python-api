### Para rodar o projeto no Docker:

Na pasta do projeto em um terminal, você deve colocar os seguintes comandos:

```
sudo docker build -t python-api -f Dockerfile .
```

```
sudo docker run --name python-api -d -v /home/dev/logs:/home/dev/logs -p 5000:5000 python-api
```

Para acessar a documentação basta colocar a seguinte url no navegador:

```
http://localhost:5000/swagger/#/
```
