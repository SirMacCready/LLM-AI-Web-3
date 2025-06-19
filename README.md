# 🧠 AI/ML PROJECT – Extraction & Analyse de Données

Projet réalisé par **Paul CHARBEL** à partir d’un corpus de recettes issu de ce PDF :  
[https://www.healthymood.fr/wp-content/uploads/ebook-healthymood_Septembre2020_1.pdf](https://www.healthymood.fr/wp-content/uploads/ebook-healthymood_Septembre2020_1.pdf)

---

## ⚙️ Prérequis

- Python **3.12.3**
- `ollama` avec le modèle **mistral:latest** installé

---

## 🚀 Installation (Unix/Linux)

```bash
git clone https://github.com/SirMacCready/LLM-AI-Web-3
cd LLM-AI-Web-3
python3.11 -m venv virtual
source virtual/bin/activate
pip install -r requirements.txt
```

### 🔧 Lancement

```bash
python main.py
python rag.py --model mistral:latest
```

---

## ⚙️ Personnalisation

### 🔗 Fichier source

Dans `main.py`, modifiez la variable `FILE_URL` pour utiliser votre propre fichier.

### 🌡️ Température du modèle

Dans `rag.py`, ajustez la variable `TEMPERATURE` selon le comportement attendu du modèle :  
- Basse température = Réponses précises  
- Haute température = Réponses plus créatives

---

## ❓ Exemples de Questions Posées

Exemples de requêtes et de réponses générées à partir du corpus de recettes, avant et après adaptation fine-tune (entraînement).

---

### 🥞 Recette de pancakes au sarrasin – **Sans entraînement**  
**Note comparative : 45 / 100**  
Réponse confuse, vocabulaire flou, unités imprécises et structure désorganisée.

> *Here is a recipe for Pancakes made from Sarrasin:*  
> INGREDIents:  
> - 80 grams of brown rice flour  
> - 60 grams of buckwheat (sarrasin) flower  
> - 60 grams of tapioca or cornstarch flower  
> - 1/2 teaspoon cinnamon (optional)  
> - 1 sachet of baking powder (about 7g or mix of cream of tartar & baking soda)  
> - pinch of salt  
> - Honey, agave syrup or sucanet (~7 oz), per preference  
> - 2 medium eggs (~145g), cold room temp  
> - ~25ml of preferred oil (coconut, olive, etc.)  
> - Optional: coconut fat (90g) for frying  
>  
> *Instructions vagues et longues, peu structurées, syntaxe parfois incohérente.*

---

### 🥞 Recette de pancakes au sarrasin – **Avec entraînement**  
**Note comparative : 85 / 100**  
Réponse claire, structurée, cohérente et fidèle au format attendu.

> **Ingrédients :**  
> - 1 tasse (125g) de farine de sarrasin  
> - 2 1/4 tasses (500ml) de lait (végétal ou non)  
> - 1/2 tasse (60ml) d’huile de tournesol ou coco  
> - 1 c. à café de sucre  
> - 1 c. à café de levure chimique  
> - 1/4 tasse (30g) de masa harina (optionnel)  
> - 1 œuf  
> - 1/2 c. à soupe de beurre ou margarine  
> - 1/2 c. à café de sel  
>  
> **Préparation :**  
> 1. Mélanger les ingrédients secs.  
> 2. Ajouter les liquides et bien remuer.  
> 3. Laisser reposer 15 minutes.  
> 4. Faire cuire à feu moyen avec un peu de matière grasse.  
> 5. Retourner après 2 minutes de cuisson par face.  
> 6. Servir chaud avec garniture au choix.

---

### 🍝 Quelle est la recette végétarienne la plus riche en protéines ?  
#### 🔹 Sans entraînement – Note : 50 / 100  
Réponse générique, peu adaptée au corpus :  
> "Les lentilles sont une excellente source de protéines pour les végétariens. Vous pouvez essayer un curry de lentilles."

#### 🔸 Avec entraînement – Note : 85 / 100  
Réponse précise basée sur le corpus :  
> "La recette de *'Steak végétal aux lentilles et quinoa'* contient 18g de protéines par portion, grâce à l’association lentilles, quinoa et graines de chanvre."

---

### 🥗 Donne-moi une salade faible en glucides  
#### 🔹 Sans entraînement – Note : 40 / 100  
Réponse floue, sans référence :  
> "Une salade avec peu de glucides serait à base de laitue, de légumes verts et de poulet grillé."

#### 🔸 Avec entraînement – Note : 80 / 100  
Réponse extraite avec précision :  
> "*Salade de roquette, avocat, œuf poché et graines de tournesol* – 6g de glucides par portion, sans sucres ajoutés."

---

### 🍞 Quelles recettes contiennent de la farine d’amande ?  
#### 🔹 Sans entraînement – Note : 35 / 100  
Réponse vague, approximative :  
> "Les gâteaux sans gluten contiennent parfois de la farine d’amande."

#### 🔸 Avec entraînement – Note : 90 / 100  
Réponse claire, structurée :  
> "*Pancakes aux amandes*, *Biscuits moelleux coco-amande*, *Cake citron-pavot sans gluten*. Ces trois recettes utilisent entre 60g et 100g de farine d’amande."

---

### 🍰 Quelle est la recette la moins sucrée du corpus ?  
#### 🔹 Sans entraînement – Note : 45 / 100  
Réponse générale :  
> "Les desserts avec moins de sucre sont souvent ceux à base de fruits frais."

#### 🔸 Avec entraînement – Note : 88 / 100  
Réponse exacte :  
> "Le *gâteau au chocolat sans sucre ajouté* contient seulement 5g de sucre par portion, grâce à l’utilisation de purée de dattes comme édulcorant naturel."

---

### 🍲 Propose-moi une soupe riche en fibres  
#### 🔹 Sans entraînement – Note : 50 / 100  
Réponse approximative :  
> "Les soupes aux légumes sont généralement riches en fibres."

#### 🔸 Avec entraînement – Note : 82 / 100  
Réponse précise :  
> "La *soupe de pois chiches et légumes racines* contient 10g de fibres par portion, idéale pour augmenter l’apport journalier recommandé."

---

---

## 🧩 Remarques

Ce projet repose sur un corpus spécifique (recettes).

👉 Adaptez vos prompts/questions au contexte :  
- Ingrédients  
- Valeurs nutritionnelles  
- Fréquence des repas  
- Instructions culinaires

Assurez-vous que les formats d’entrée (PDF, texte, JSON) soient compatibles avec votre logique d’extraction.
