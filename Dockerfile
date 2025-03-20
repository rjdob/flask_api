# Utiliser une image Python de base
FROM python:3.12.7

# Définir le répertoire de travail
WORKDIR /

# Copier le fichier requirements.txt dans l'image
COPY requirements.txt /

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste de l'application dans l'image
COPY . /

# Exécuter les tests avant de démarrer l'application
RUN pytest test_app.py

# Exposer le port sur lequel l'app sera disponible + le port des métriques
EXPOSE 5000 8000

# Définir la commande pour lancer l'application Flask
CMD ["python", "app.py"]