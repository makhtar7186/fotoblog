# Étape 1 : image de base
FROM python:3.11-slim

# Étape 2 : répertoire de travail
WORKDIR /app

# Étape 3 : variables d’environnement
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Étape 4 : installation des dépendances système
# Pillow a besoin de ces paquets pour compiler correctement
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libjpeg-dev \
    zlib1g-dev \
    libfreetype6-dev \
    liblcms2-dev \
    libopenjp2-7-dev \
    libtiff5-dev \
    tk-dev \
    tcl-dev \
    python3-tk \
    && rm -rf /var/lib/apt/lists/*

# Étape 5 : installation des dépendances Python
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Étape 6 : copier le code du projet
COPY . /app/

# Étape 7 : exposer le port
EXPOSE 8000

# Étape 8 : lancer le serveur
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
