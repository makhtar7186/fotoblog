# Étape 1 : choisir une image de base Python
FROM python:3.11-slim

# Étape 2 : définir le répertoire de travail dans le conteneur
WORKDIR /app

# Étape 3 : éviter la mise en cache des fichiers .pyc et forcer un buffer stdout/stderr immédiat
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Étape 4 : installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Étape 5 : copier les fichiers de dépendances (requirements.txt)
COPY requirements.txt /app/

# Étape 6 : installer les dépendances Python
RUN pip install --upgrade pip && pip install -r requirements.txt

# Étape 7 : copier le reste du code du projet
COPY . /app/

# Étape 8 : exposer le port 8000 (par défaut pour Django)
EXPOSE 8000

# Étape 9 : définir la commande de démarrage
# (tu peux adapter selon ton besoin : runserver, gunicorn, etc.)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
