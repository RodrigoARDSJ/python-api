FROM python:3.8-slim-buster

WORKDIR /app
RUN apt-get update && apt-get install -y python3-pip python-dev
RUN pip3 install flask flask_swagger_ui
COPY . .
#CMD ["python3", "app.py", "--host=127.0.0.1"]
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]