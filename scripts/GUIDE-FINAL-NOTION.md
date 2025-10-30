# 🎯 GUIDE FINAL - CONFIGURATION NOTION (2 MINUTES)

## ❌ PROBLÈME : Token retourne 403 partout

Cela signifie que l'intégration "MCP ProNeXus" n'a **PAS les bonnes permissions**.

---

## ✅ SOLUTION EN 2 ÉTAPES

### ÉTAPE 1 : Activer les Capabilities (1 minute)

**a) Ouvrez :** https://www.notion.so/my-integrations

**b) Cliquez sur "MCP ProNeXus"**

**c) Vérifiez la section "Capabilities"**

Vous DEVEZ voir ces 3 cases **COCHÉES** :

```
Content Capabilities
  ☑️  Read content          ← DOIT ÊTRE COCHÉ
  ☑️  Update content        ← DOIT ÊTRE COCHÉ
  ☑️  Insert content        ← DOIT ÊTRE COCHÉ
```

**d) Si elles ne sont PAS cochées :**
1. Cochez les 3 cases
2. Cliquez sur **"Submit"** en bas de la page
3. **IMPORTANT :** Copiez le nouveau token qui apparaît (il peut avoir changé)

---

### ÉTAPE 2 : Partager la Base avec l'Intégration (30 secondes)

**a) Ouvrez votre base :**
https://www.notion.so/2990a77e973480fcade1cc37ef1c24a4

**b) En haut à droite, cliquez sur "Share"**

**c) Dans le champ de recherche, tapez : `MCP ProNeXus`**

**d) Cliquez sur `🤖 MCP ProNeXus` dans les résultats**

**e) Vérifiez qu'elle apparaît maintenant dans "Connected to :"**

---

## 🧪 TESTER

Dans le terminal :

```bash
# Utilisez le token APRÈS avoir activé les Capabilities
export NOTION_API_KEY="secret_VOTRE_TOKEN"
export NOTION_DATABASE_ID="2990a77e973480fcade1cc37ef1c24a4"

python3 scripts/notion-deep-diagnostic.py
```

**Vous DEVEZ voir :**
```
✅ Token valide ! L'intégration existe.
✅ Recherche réussie !
✅ Accès autorisé à la base !
```

---

## 🚀 PUBLIER LES FICHES

Si les 3 tests sont **✅ verts** :

```bash
python3 scripts/publish-to-notion.py
```

**Résultat :**
```
📝 Publication : 06.md... ✅
📝 Publication : 07.md... ✅
📝 Publication : 08.md... ✅
📝 Publication : 09.md... ✅
📝 Publication : 10.md... ✅

🎉 5 fiches publiées avec succès !
```

---

## 🆘 SI ÇA NE FONCTIONNE TOUJOURS PAS

**Créez une NOUVELLE intégration :**

1. Sur https://www.notion.so/my-integrations
2. Cliquez **"+ New integration"**
3. Name : `ProNeXus Publish`
4. **AVANT de créer, cochez bien :**
   - ✅ Read content
   - ✅ Update content
   - ✅ Insert content
5. Cliquez "Submit"
6. Copiez le token
7. Partagez la base avec "ProNeXus Publish"
8. Testez avec le nouveau token

---

**Une fois configuré, donnez-moi le token et je lance immédiatement la publication ! 🚀**
