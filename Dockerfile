# Använd en officiell Python-bild
FROM python:3.9

# Sätt arbetskatalogen i containern
WORKDIR /app

# Kopiera projektfiler till containern
COPY . .

# Installera beroenden
RUN pip install --no-cache-dir -r requirements.txt

# Starta appen med Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "app:app"]

