FROM python:3.11-slim

# Copier les scripts et requirements
COPY ./scripts/requirements.txt /app/requirements.txt

# Installer les dépendances pendant le build
RUN pip install --no-cache-dir -r /app/requirements.txt

# Commande par défaut à l'exécution
CMD ["bash"]
