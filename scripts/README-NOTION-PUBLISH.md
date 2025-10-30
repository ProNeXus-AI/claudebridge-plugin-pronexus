# 📤 Publication des Fiches vers Notion

Guide complet pour publier les **FICHES PROCESS PNX™ 06-10** vers votre base Notion.

---

## 🎯 Prérequis

### 1️⃣ Intégration Notion

Créez une intégration Notion :

1. Allez sur https://www.notion.so/my-integrations
2. Cliquez sur **"+ New integration"**
3. Nommez-la : `ProNeXus Claude Bridge`
4. Sélectionnez votre workspace
5. **Copiez le token** : `secret_xxxxxxxxxxxxx`

### 2️⃣ Partager la Base avec l'Intégration

1. Ouvrez votre base Notion "Fiches Process PNX™"
2. Cliquez sur `⋯` (menu) en haut à droite
3. Sélectionnez **"Connections"** ou **"Add connections"**
4. Recherchez et ajoutez votre intégration `ProNeXus Claude Bridge`

### 3️⃣ Récupérer l'ID de la Base

L'URL de votre base ressemble à :
```
https://www.notion.so/2990a77e973480fcade1cc37ef1c24a4?v=...
```

L'ID de la base est : `2990a77e973480fcade1cc37ef1c24a4`

---

## ⚙️ Configuration

### Option 1 : Variables d'environnement

```bash
# Ajouter à votre ~/.bashrc ou ~/.zshrc
export NOTION_API_KEY="secret_xxxxxxxxxxxxx"
export NOTION_DATABASE_ID="2990a77e973480fcade1cc37ef1c24a4"

# Recharger le shell
source ~/.bashrc  # ou source ~/.zshrc
```

### Option 2 : Fichier .env

Créez un fichier `.env` à la racine du projet :

```bash
# .env
NOTION_API_KEY=secret_xxxxxxxxxxxxx
NOTION_DATABASE_ID=2990a77e973480fcade1cc37ef1c24a4
```

Puis chargez-le avant d'exécuter le script :
```bash
source .env
```

---

## 🚀 Utilisation

### Méthode 1 : Script Python (Recommandé)

Le script Python offre une conversion complète Markdown → Notion avec gestion des blocs.

**Installation des dépendances :**
```bash
pip install requests
```

**Exécution :**
```bash
cd /home/user/claudebridge-plugin-pronexus
python3 scripts/publish-to-notion.py
```

**Sortie attendue :**
```
🚀 Publication des FICHES PROCESS PNX™ vers Notion
============================================================

📄 5 fiche(s) trouvée(s)

📝 Publication : 06.md... ✅
   🔗 https://notion.so/FICHE-06-...
📝 Publication : 07.md... ✅
   🔗 https://notion.so/FICHE-07-...
📝 Publication : 08.md... ✅
   🔗 https://notion.so/FICHE-08-...
📝 Publication : 09.md... ✅
   🔗 https://notion.so/FICHE-09-...
📝 Publication : 10.md... ✅
   🔗 https://notion.so/FICHE-10-...

============================================================
✅ Publication terminée
   Succès : 5 / 5
   Échecs : 0

🎉 Toutes les fiches ont été publiées avec succès !

🔗 Base Notion : https://www.notion.so/2990a77e973480fcade1cc37ef1c24a4
```

### Méthode 2 : Script Bash (Template)

Le script bash est un template à adapter selon votre implémentation MCP.

```bash
chmod +x scripts/publish-fiches-to-notion.sh
./scripts/publish-fiches-to-notion.sh
```

---

## 📋 Structure de la Base Notion

Assurez-vous que votre base Notion contient les **propriétés suivantes** :

| Propriété | Type | Valeurs possibles |
|-----------|------|-------------------|
| **Nom du Process** | Title | (texte libre) |
| **Description** | Text | (texte libre) |
| **Statut** | Select | Public, Draft |
| **Niveau** | Select | Débutant, Intermédiaire, Avancé, Expert |
| **Lien** | URL | (optionnel) |

Le script créera automatiquement les pages avec ces propriétés.

---

## 🔍 Vérification

Après l'exécution, vérifiez dans Notion :

1. **Pages créées** : 5 nouvelles pages (FICHE 06 à 10)
2. **Propriétés remplies** :
   - Titre : `FICHE XX — Nom du Process`
   - Description : Première phrase du contexte
   - Statut : `Public`
   - Niveau : `Avancé`
3. **Contenu formaté** :
   - Headings (H1, H2, H3)
   - Paragraphes
   - Blocs de code avec syntaxe
   - Listes (bullet et numbered)
   - Dividers

---

## 🐛 Résolution des Erreurs

### Erreur : "NOTION_API_KEY non définie"

**Solution :**
```bash
export NOTION_API_KEY="secret_xxxxxxxxxxxxx"
```

### Erreur : "Could not find database"

**Causes possibles :**
1. ID de base incorrecte
2. Intégration non partagée avec la base

**Solution :**
- Vérifiez l'ID dans l'URL de la base
- Partagez la base avec votre intégration (voir Prérequis § 2)

### Erreur : "Unauthorized" (401)

**Cause :** Token API invalide

**Solution :**
- Régénérez un token sur https://www.notion.so/my-integrations
- Mettez à jour `NOTION_API_KEY`

### Erreur : "Invalid request" (400)

**Cause :** Propriétés de la base ne correspondent pas

**Solution :**
- Vérifiez que votre base contient les propriétés exactes :
  - `Nom du Process` (Title)
  - `Description` (Text)
  - `Statut` (Select avec option "Public")
  - `Niveau` (Select avec option "Avancé")

### Erreur : "Rate limited" (429)

**Cause :** Trop de requêtes simultanées

**Solution :**
- Attendez 1 minute
- Le script Python gère automatiquement le rate limiting

---

## 📚 Fichiers Créés

| Fichier | Description |
|---------|-------------|
| `publish-to-notion.py` | Script Python complet avec conversion MD → Notion |
| `publish-fiches-to-notion.sh` | Script Bash (template) |
| `README-NOTION-PUBLISH.md` | Cette documentation |

---

## 🔗 Ressources

- **API Notion Documentation** : https://developers.notion.com
- **Base Fiches Process PNX™** : https://www.notion.so/2990a77e973480fcade1cc37ef1c24a4
- **Intégrations Notion** : https://www.notion.so/my-integrations

---

## ✅ Checklist de Publication

- [ ] Intégration Notion créée
- [ ] Token API copié
- [ ] Base Notion partagée avec l'intégration
- [ ] Variables d'environnement configurées
- [ ] Script Python exécuté avec succès
- [ ] 5 fiches visibles dans Notion
- [ ] Formatage vérifié (headings, code blocks, listes)

---

> **Guide validé — prêt pour publication automatique vers Notion**

*GalaXLytique™ Process Documentation • ProNeXus AI Division • v1.0.0*
