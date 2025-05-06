FROM python:3.13-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5002

CMD ["gunicorn", "-b", "0.0.0.0:5002", "pokeneas.app:app"]
