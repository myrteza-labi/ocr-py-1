# Instructions d'exécution

## Prérequis

Assurez-vous d'avoir Python installé sur votre système.

## Étapes pour exécuter le code avec succès

**Environnement virtuel**

Pour exécuter ce code, vous devez d'abord configurer un environnement virtuel pour isoler les dépendances. Suivez ces étapes :

- Créer l'environnement virtuel :
  - Ouvrez une fenêtre de terminal.
  - Naviguez vers le répertoire du projet.
  - Exécutez la commande suivante pour installer les dépendances :

```
python -m venv venv
```

- Activer l'environnement virtuel :

Sur Windows :

```
.\venv\Scripts\activate
```

Sur Linux/macOS :

```
source venv/bin/activate
```

1. **Installation des dépendances**

   - Toujours sur le repertoire du projet
   - Exécutez la commande suivante pour installer les dépendances :

     ```
     pip install -r requirements.txt
     ```

2. **Exécution du script**

   - Assurez-vous d'être toujours dans le répertoire du projet via le terminal.
   - Exécutez le script `app.py` en utilisant la commande suivante :
     ```
     python3 app.py
     ```

3. **Résultats**

   - Le script va récupérer les informations des livres dans la catégorie de mystère depuis le site "https://books.toscrape.com/".
   - Les informations seront sauvegardées dans le fichier `generated_datas/book_info.txt`.
   - Les images des livres seront téléchargées et sauvegardées dans le dossier `fetched_images`.
   - Les fichiers CSV seront générés dans le dossier `CSVs`.

4. **Notes**
   - Si les dossiers `generated_datas`, `fetched_images`, ou `CSVs` n'existent pas, le script les créeras automatiquement.

## Structure du projet

- `app.py`: Le script principal qui effectue le scraping et la sauvegarde des informations.
- `requirements.txt`: Fichier spécifiant les dépendances du projet.

## Dépendances

Les dépendances nécessaires sont répertoriées dans le fichier `requirements.txt` et seront installées lors de l'étape 1.

---

Ce script utilise BeautifulSoup pour le scraping web et requests pour effectuer les requêtes HTTP. Les informations des livres et les images sont sauvegardées localement dans le dossier `generated_datas` et `fetched_images` respectivement.
