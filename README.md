# Instructions d'exécution

## Prérequis

Assurez-vous d'avoir Python installé sur votre système.

## Étapes pour exécuter le code avec succès

1. **Installation des dépendances**

   - Ouvrez une fenêtre de terminal.
   - Naviguez vers le répertoire du projet.
   - Exécutez la commande suivante pour installer les dépendances :

     ```
     pip install -r requirements.txt
     ```

     ```activer l'environnement de developpement avec la commande
     source venv/bin/activate
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

4. **Notes**
   - Si le dossier `generated_datas` n'existe pas, le script le créera automatiquement.

## Structure du projet

- `app.py`: Le script principal qui effectue le scraping et la sauvegarde des informations.
- `requirements.txt`: Fichier spécifiant les dépendances du projet.

## Dépendances

Les dépendances nécessaires sont répertoriées dans le fichier `requirements.txt` et seront installées lors de l'étape 1.

---

Ce script utilise BeautifulSoup pour le scraping web et requests pour effectuer les requêtes HTTP. Les informations des livres et les images sont sauvegardées localement dans le dossier `generated_datas` et `fetched_images` respectivement.
