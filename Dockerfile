# Wybierz obraz bazowy
FROM python:3.9

# Ustaw katalog roboczy
WORKDIR /app

# Skopiuj pliki z aktualnego katalogu do kontenera
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Otwórz port
EXPOSE 5000

# Uruchom aplikację
CMD ["python", "main.py"]
