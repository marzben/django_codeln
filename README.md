# django_codeln

Ce projet contient des tests unitaires pour un système de badges d'utilisateur. Les tests sont écrits en utilisant le framework de test Django et sont destinés à vérifier le fonctionnement des badges "Star", "Collector" et "Pioneer".

## Configuration initiale

Avant d'exécuter les tests, assurez-vous d'avoir configuré correctement votre environnement Django et votre base de données. Assurez-vous également d'avoir les dépendances nécessaires installées.

## Tests unitaires

### `setUp`

La méthode `setUp` initialise un environnement de test en créant un utilisateur, en ajoutant plusieurs modèles 3D et en configurant un client API.

### `test_star_badge`

Ce test vérifie le fonctionnement du badge "Star" en se basant sur le nombre de vues des modèles 3D de l'utilisateur.

- Vérifie que l'utilisateur n'a pas déjà le badge "Star" au début du test.
- Vérifie que l'utilisateur n'obtient pas le badge "Star" s'il a moins de 1000 vues.
- Vérifie que l'utilisateur obtient le badge "Star" s'il a exactement 1000 vues.
- Vérifie que l'utilisateur obtient toujours le badge "Star" s'il a plus de 1000 vues.

### `test_collector_badge`

Ce test vérifie le fonctionnement du badge "Collector" en se basant sur le nombre de modèles 3D de l'utilisateur.

- Vérifie que l'utilisateur n'obtient pas le badge "Collector" s'il a moins de 5 modèles 3D.
- Vérifie que l'utilisateur obtient le badge "Collector" s'il a au moins 5 modèles 3D.

### `test_pioneer_badge`

Ce test vérifie le fonctionnement du badge "Pioneer" en se basant sur la date d'inscription de l'utilisateur.

- Vérifie que l'utilisateur n'obtient pas le badge "Pioneer" s'il s'est inscrit il y a moins d'un an.
- Vérifie que l'utilisateur obtient le badge "Pioneer" s'il s'est inscrit il y a exactement un an.
- Vérifie que l'utilisateur obtient toujours le badge "Pioneer" s'il s'est inscrit il y a plus d'un an.

## Exécution des tests

Pour exécuter les tests, vous pouvez utiliser la commande Django `python manage.py test`. Assurez-vous d'avoir configuré votre environnement de test approprié.

## Remarques

- Les lignes de code commentées dans les tests `test_star_badge` et `test_collector_badge` expliquent comment gérer le cas où l'utilisateur a déjà obtenu le badge. Vous pouvez décommenter ces lignes pour effectuer cette vérification si nécessaire.

- Assurez-vous que les dépendances requises sont installées avant d'exécuter les tests.

---

N'oubliez pas d'adapter ce README à votre projet en ajoutant des informations spécifiques, comme les dépendances requises, les étapes d'installation, etc. Bonne chance avec vos tests unitaires !

# Application de Badges avec Django

Ce dépôt contient une application web Django qui met en œuvre un système de badges pour les utilisateurs en fonction de leurs actions sur le site. Les badges sont attribués en fonction du nombre de vues des modèles 3D, du nombre de modèles téléchargés, et de la durée de l'inscription de l'utilisateur sur le site.

## Installation
Pour exécuter cette application localement, suivez ces étapes :

1. Clonez ce dépôt sur votre machine locale :

   ```bash
   git clone  https://github.com/marzben/django_codeln.git


- Accédez au répertoire du projet :
  cd django_codeln


- Créez un environnement virtuel(précisez la version de python, Ex: python3.11):
  ```bash
   python -m venv venv

- Activez l'environnement virtuel :
  - Sur Windows :
   venv\Scripts\activate
  - Sur macOS et Linux :
    source venv/bin/activate

- Installez les dépendances Python :
  ```bash
   pip install -r requirements.txt

- Appliquez les migrations de base de données :

   ```bash
    python manage.py migrate

- Exécutez le serveur de développement :
   ```bash
    python manage.py runserver

Accédez à l'application dans votre navigateur à l'adresse 
http://localhost:8000/

Structure du Code
* models.py : Définition des modèles de données Django, y compris le modèle Model3d, Badge, et UserBadge.
* views.py : Implémentation de l'API pour accéder aux badges des utilisateurs.
* utils.py : Fonctions utilitaires pour attribuer des badges aux utilisateurs.
* tests.py : Tests unitaires pour vérifier le bon fonctionnement de l'attribution des badges.

Tests Unitaires
Nous avons inclus des tests unitaires pour chaque badge afin de garantir que les badges sont attribués correctement en fonction des actions de l'utilisateur. Vous pouvez exécuter les tests en utilisant la commande suivante :

   ```bash
    python manage.py test



API

Ce projet contient une API view appelée `UserBadgeAPIView` qui permet de récupérer la liste des badges associés à un utilisateur spécifique.

## Fonctionnalités

La classe `UserBadgeAPIView` offre une seule méthode HTTP GET pour obtenir la liste des badges d'un utilisateur donné.

### Endpoint

- `GET /api/userbadges/<int:user_id>/`

### Paramètres de requête

- `user_id` (int) : L'ID de l'utilisateur pour lequel vous souhaitez récupérer les badges.

### Réponse

L'API renvoie une réponse JSON contenant la liste des noms de badges associés à l'utilisateur spécifié.

Exemple de réponse JSON :

```json
["Badge1", "Badge2", "Badge3"]


- Exemple d'utilisation avec curl :
    ```bash
      curl -X GET http://votre-domaine.com/api/userbadges/123/

Remplacez votre-domaine.com par l'URL de votre application et 123 par l'ID de l'utilisateur que vous souhaitez interroger.
























