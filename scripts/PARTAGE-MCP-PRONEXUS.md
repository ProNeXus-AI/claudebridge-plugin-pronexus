# 🚀 PARTAGER LA BASE AVEC "MCP ProNeXus"

## 📍 Votre intégration : **MCP ProNeXus**

---

## ✅ ÉTAPES EXACTES (30 secondes)

### 1️⃣ Ouvrir votre base

Cliquez ici pour ouvrir directement :
👉 **https://www.notion.so/2990a77e973480fcade1cc37ef1c24a4**

### 2️⃣ Cliquer sur "Share" ou "⋯"

En haut à droite de la page Notion, cherchez l'un de ces boutons :
- **[Share]** (bouton bleu)
- **[⋯]** (trois points)

### 3️⃣ Ajouter la connexion

**Dans la fenêtre qui s'ouvre :**

```
┌───────────────────────────────────────────┐
│  Share "Fiches Process PNX™"              │
│                                           │
│  🔍 Add people, emails, or connections   │
│      ↓ Tapez ici ↓                       │
│  ┌─────────────────────────────────────┐ │
│  │ MCP ProNeXus                        │ │ ← Tapez ce nom
│  └─────────────────────────────────────┘ │
│                                           │
│  Résultats :                              │
│  ┌─────────────────────────────────────┐ │
│  │ 🤖 MCP ProNeXus                     │ │ ← Cliquez ici !
│  │    Integration                       │ │
│  └─────────────────────────────────────┘ │
└───────────────────────────────────────────┘
```

### 4️⃣ Confirmer

Après avoir cliqué, vous devriez voir :

```
Connected to:
  🤖 MCP ProNeXus
```

✅ **C'est tout ! La base est maintenant accessible à votre intégration.**

---

## 🧪 TESTER LA CONNEXION

Dans votre terminal, lancez :

```bash
export NOTION_API_KEY="secret_K28100913161JiojvrgismfGQZVDYtkv49qWUO3MOzw7rP"
export NOTION_DATABASE_ID="2990a77e973480fcade1cc37ef1c24a4"

python3 scripts/notion-deep-diagnostic.py
```

**Résultat attendu :**

```
✅ Token valide ! L'intégration existe.
✅ Recherche réussie ! X élément(s) trouvé(s)
✅ Accès autorisé à la base !
   📊 Base trouvée : Fiches Process PNX™
```

---

## 🚀 PUBLIER LES FICHES

Si le test est **entièrement vert**, lancez :

```bash
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
```

---

## 🆘 SI VOUS NE TROUVEZ PAS "MCP ProNeXus"

1. Vérifiez que l'intégration existe : https://www.notion.so/my-integrations
2. Si elle n'existe pas, créez-la avec exactement ce nom : **MCP ProNeXus**
3. Configurez les Capabilities : ✅ Read, ✅ Update, ✅ Insert

---

Dites-moi dès que vous avez partagé la base avec "MCP ProNeXus" et je lancerai immédiatement les tests ! 🚀
