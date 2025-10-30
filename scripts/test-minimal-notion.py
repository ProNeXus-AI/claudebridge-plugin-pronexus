#!/usr/bin/env python3
"""
Test ultra-simple pour identifier le problème exact
"""

import requests

NOTION_API_KEY = "secret_K28100913161JiojvrgismfGQZVDYtkv49qWUO3MOzw7rP"

print("=" * 80)
print("🔍 TEST MINIMAL - INTÉGRATION NOTION")
print("=" * 80)

headers = {
    'Authorization': f'Bearer {NOTION_API_KEY}',
    'Notion-Version': '2022-06-28'
}

print("\n1️⃣  Test du token lui-même...")
print(f"Token utilisé : {NOTION_API_KEY[:20]}...{NOTION_API_KEY[-10:]}")
print(f"Longueur : {len(NOTION_API_KEY)} caractères")

# Test le plus basique possible
print("\n2️⃣  Appel API minimal (search vide)...")
response = requests.post(
    'https://api.notion.com/v1/search',
    headers=headers,
    json={}
)

print(f"\nStatus Code: {response.status_code}")
print(f"Response: {response.text}")

if response.status_code == 403:
    print("\n" + "=" * 80)
    print("❌ PROBLÈME CONFIRMÉ : INTÉGRATION INVALIDE")
    print("=" * 80)
    print("""
Le token retourne 403 Forbidden sur l'appel le plus basique.

Cela signifie une seule chose : L'intégration "MCP ProNeXus" a un problème
de configuration ou le token est incorrect/expiré.

🎯 SOLUTIONS POSSIBLES :

Option A - Vérifier l'intégration existante
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Allez sur https://www.notion.so/my-integrations
2. Trouvez "MCP ProNeXus"
3. Vérifiez que les Capabilities sont activées :
   ☑️ Read content
   ☑️ Update content
   ☑️ Insert content
4. Si elles ne le sont pas, activez-les et récupérez le NOUVEAU token
5. IMPORTANT : Le token change quand on modifie les Capabilities !

Option B - Créer une nouvelle intégration (RECOMMANDÉ)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Sur https://www.notion.so/my-integrations
2. "+ New integration"
3. Name: "ProNeXus Publisher" (nouveau nom)
4. Workspace: [Votre workspace]
5. AVANT de créer, COCHEZ :
   ☑️ Read content
   ☑️ Update content
   ☑️ Insert content
6. Submit
7. Copiez le token COMPLET
8. Partagez la base avec "ProNeXus Publisher"

Option C - Vérifier l'intégration dans Notion
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Si l'intégration n'apparaît plus dans la liste :
→ Elle a peut-être été supprimée
→ Créez-en une nouvelle (Option B)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 APRÈS CORRECTION :

export NOTION_API_KEY="secret_NOUVEAU_TOKEN"
export NOTION_DATABASE_ID="2990a77e973480fcade1cc37ef1c24a4"

python3 scripts/publish-to-notion.py
""")
elif response.status_code == 200:
    print("\n✅ TOKEN VALIDE !")
    print("Le problème n'est pas le token mais autre chose.")
    data = response.json()
    print(f"\nNombre de résultats : {len(data.get('results', []))}")
else:
    print(f"\n❌ Erreur inattendue : {response.status_code}")

print("\n" + "=" * 80)
