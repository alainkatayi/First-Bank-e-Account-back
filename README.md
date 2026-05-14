# 🏦 Bank Self-Boarding API (Backend)

Ce projet est la partie Backend d'une application bancaire permettant aux clients de soumettre leurs informations pour une ouverture de compte (self-boarding). Il inclut une interface de gestion pour les agents et un système d'audit pour les administrateurs.

## 📌 Fonctionnalités Clés
*   **Self-Boarding Public :** Soumission de formulaire et documents par les prospects.
*   **Gestion des Décisions :** Système de validation/rejet avec motivation obligatoire.
*   **Audit Trail :** Traçabilité complète des actions (quel agent a validé quel dossier).
*   **Soft Delete :** Suppression sécurisée des données sans perte définitive.
*   **Relations Complexes :** Liaison One-to-One entre les demandes et les décisions finales.

---

## 🛠️ Stack Technique
*   **Langage :** Python 3.10+
*   **Framework :** Django 5.x
*   **API :** Django REST Framework (DRF)
*   **Base de Données :** MySQL (ou PostgreSQL)
*   **Auth :** SimpleJWT (JSON Web Tokens)

---

## 🚀 Installation & Configuration rapide

### 1. Cloner le dépôt

* git clone <url-du-repo>
* cd bank-boarding-backend

## Configurer l'environnement virtuel
*pip install -r requirements.txt

## Base de données

* python manage.py makemigrations
* python manage.py migrate

## Endpoints API Principaux
* POST : accounts/register: creer un utilisateur data: [username, password]
* GET : accounts/index: lister tous les utilisateurs
* POST : api/token/: se connecter [username, password]
* POST : request/store : creer une request
* GET : request/index: lister toute les demandes
* GET: request/id: recuperer une demande
* POST : request/id/decision: prendre une decision
* GET : request/decision: lister toute les decision

#Pour connaitre les données a envoyer dans une requete POST, veuillez voir le fichier serializers.py de chaque application
