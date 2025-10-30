# 🔗 PARTAGER LA BASE NOTION AVEC L'INTÉGRATION

## ⚠️ PROBLÈME ACTUEL

La base "Fiches Process PNX™" est restaurée MAIS pas encore partagée avec votre intégration.

L'intégration Notion ne peut accéder à AUCUNE base par défaut. Chaque base doit être **explicitement partagée**.

---

## ✅ SOLUTION SIMPLE (30 secondes)

### Étape 1 : Ouvrir votre base Notion

Cliquez sur ce lien pour ouvrir la base directement :

👉 **https://www.notion.so/2990a77e973480fcade1cc37ef1c24a4**

### Étape 2 : Trouver le bouton "Share"

En haut à droite de la page, vous devriez voir :

```
[Nom de la base]                    [Share] [⋯]
```

Cliquez sur le bouton **"Share"**

### Étape 3 : Ajouter l'intégration

Dans la fenêtre qui s'ouvre :

1. En bas, vous verrez **"Add connections"** ou un champ de recherche
2. Tapez le nom de votre intégration (probablement "ProNeXus" ou similaire)
3. Cliquez sur l'intégration dans les résultats
4. Elle devrait maintenant apparaître dans la liste

**Visuel :**
```
┌─────────────────────────────────────────┐
│  Share to web or invite people          │
│                                          │
│  🔍 Search for a person, email...       │
│                                          │
│  ────────────────────────────────────   │
│  🔗 Add connections                      │
│     ┌──────────────────────────────┐    │
│     │ 🤖 ProNeXus Bridge V2        │ ← Cliquez ici
│     └──────────────────────────────┘    │
└─────────────────────────────────────────┘
```

### Étape 4 : Confirmer

Une fois ajoutée, vous devriez voir l'intégration dans la liste des "Connections" avec une icône de robot 🤖.

---

## 🎯 MÉTHODE ALTERNATIVE (si "Share" n'est pas visible)

### Option A : Via le menu "⋯"

1. Cliquez sur **"⋯"** (trois points) en haut à droite
2. Descendez jusqu'à la section **"Connections"**
3. Cliquez sur **"+ Add connections"**
4. Sélectionnez votre intégration

### Option B : Via les paramètres de la base

1. Dans la base, cliquez sur l'icône de la base en haut à gauche
2. Allez dans les paramètres
3. Section "Connections"
4. Ajoutez votre intégration

---

## ✅ VÉRIFICATION

Une fois l'intégration ajoutée, vous devriez voir :

```
Connections
  🤖 ProNeXus Bridge V2 (ou le nom de votre intégration)
```

---

## 🚀 APRÈS LE PARTAGE

Une fois que vous avez partagé la base, exécutez dans le terminal :

```bash
export NOTION_API_KEY="secret_K28100913161JiojvrgismfGQZVDYtkv49qWUO3MOzw7rP"
export NOTION_DATABASE_ID="2990a77e973480fcade1cc37ef1c24a4"

# Test
python3 scripts/notion-deep-diagnostic.py
```

Vous devriez voir :
```
✅ Token valide ! L'intégration existe.
✅ Recherche réussie !
✅ Accès autorisé à la base !
```

Ensuite :
```bash
python3 scripts/publish-to-notion.py
```

Et les 5 fiches seront publiées ! 🎉

---

## 🆘 BESOIN D'AIDE ?

Si vous ne trouvez pas comment partager la base :

1. Faites une capture d'écran de votre base Notion (vue complète)
2. Je pourrai vous guider plus précisément

Ou partagez-moi le nom exact de votre intégration, je pourrai adapter les instructions.
