FROM python:3-alpine

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000

ENTRYPOINT []
CMD [ "python3", "-m", "flask", "--app", "app.py", "--debug", "run", "--host", "0.0.0.0" ]
