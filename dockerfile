FROM python:3.11-slim

WORKDIR /

# Copier uniquement requirements.txt à la racine
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Commande par défaut
CMD ["bash"]
