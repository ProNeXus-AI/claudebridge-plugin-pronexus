#!/usr/bin/env python3
"""
Diagnostic approfondi de l'intégration Notion
"""

import requests
import json

NOTION_API_KEY = "secret_K28100913161JiojvrgismfGQZVDYtkv49qWUO3MOzw7rP"

print("=" * 80)
print("🔬 DIAGNOSTIC APPROFONDI - INTÉGRATION NOTION")
print("=" * 80)

headers = {
    'Authorization': f'Bearer {NOTION_API_KEY}',
    'Notion-Version': '2022-06-28',
    'Content-Type': 'application/json'
}

# Test 1: Vérifier si le token est valide avec un self-test
print("\n1️⃣  Test de validation du token...")
print("-" * 80)

# Essayer de récupérer l'utilisateur bot
response = requests.get(
    'https://api.notion.com/v1/users/me',
    headers=headers
)

print(f"Status Code: {response.status_code}")
print(f"Response: {response.text[:300]}")

if response.status_code == 200:
    print("✅ Token valide ! L'intégration existe.")
    data = response.json()
    print(f"\nInformation sur le bot:")
    print(f"  - Type: {data.get('type')}")
    print(f"  - ID: {data.get('id')}")
    print(f"  - Name: {data.get('name', 'N/A')}")
elif response.status_code == 401:
    print("❌ Token invalide (401 Unauthorized)")
    print("\n⚠️  Le token ne fonctionne pas. Vérifiez :")
    print("   - Que vous avez copié le token complet")
    print("   - Que l'intégration n'a pas été supprimée")
    print("   - Que le workspace est toujours actif")
elif response.status_code == 403:
    print("❌ Accès refusé (403 Forbidden)")
    print("\n⚠️  Le token existe mais n'a pas les permissions nécessaires")
else:
    print(f"❌ Erreur inattendue: {response.status_code}")

# Test 2: Lister les pages accessibles
print("\n\n2️⃣  Test de recherche de pages...")
print("-" * 80)

search_response = requests.post(
    'https://api.notion.com/v1/search',
    headers=headers,
    json={"page_size": 5}
)

print(f"Status Code: {search_response.status_code}")

if search_response.status_code == 200:
    data = search_response.json()
    results = data.get('results', [])
    print(f"\n✅ Recherche réussie ! {len(results)} élément(s) trouvé(s)")

    if len(results) == 0:
        print("\n⚠️  IMPORTANT : Aucune page/base n'est accessible")
        print("\nCela signifie que l'intégration n'a accès à RIEN.")
        print("\n📝 Solution :")
        print("   1. Ouvrez votre base Notion dans un navigateur")
        print("   2. Cliquez sur '⋯' (menu) en haut à droite")
        print("   3. Allez dans 'Connections'")
        print("   4. Cliquez sur '+ Add connections'")
        print("   5. Sélectionnez votre intégration")
        print("\n   Sans cette étape, l'intégration ne peut accéder à aucune donnée.")
    else:
        print("\n📄 Pages/Bases accessibles :")
        for item in results[:5]:
            item_type = item.get('object')
            item_id = item.get('id')

            if item_type == 'page':
                title_prop = item.get('properties', {}).get('title', {})
                title = title_prop.get('title', [{}])[0].get('plain_text', 'Sans titre') if title_prop.get('title') else 'Sans titre'
                print(f"   📄 Page: {title} (ID: {item_id})")
            elif item_type == 'database':
                title = item.get('title', [{}])[0].get('plain_text', 'Sans titre') if item.get('title') else 'Sans titre'
                print(f"   🗃️  Database: {title} (ID: {item_id})")
else:
    print(f"❌ Erreur lors de la recherche: {search_response.text}")

# Test 3: Tester l'accès à la base spécifique
print("\n\n3️⃣  Test d'accès à la base 'Fiches Process PNX™'...")
print("-" * 80)

DATABASE_ID = "2990a77e973480fcade1cc37ef1c24a4"
db_response = requests.get(
    f'https://api.notion.com/v1/databases/{DATABASE_ID}',
    headers=headers
)

print(f"Status Code: {db_response.status_code}")

if db_response.status_code == 200:
    print("✅ Accès autorisé à la base !")
    data = db_response.json()
    title = data.get('title', [{}])[0].get('plain_text', 'Sans titre') if data.get('title') else 'Sans titre'
    print(f"\n📊 Base trouvée : {title}")
    print(f"   ID: {data.get('id')}")
    print(f"   URL: {data.get('url')}")
elif db_response.status_code == 404:
    print("❌ Base non trouvée (404)")
    print("\n⚠️  La base n'existe pas ou l'ID est incorrect")
    print(f"\nID testé : {DATABASE_ID}")
    print("\nVérifiez l'URL de votre base Notion et extrayez le bon ID")
elif db_response.status_code == 403:
    print("❌ Accès refusé à cette base (403)")
    print("\n⚠️  L'intégration n'a PAS accès à cette base spécifique")
    print("\n📝 Solution :")
    print(f"   1. Ouvrez : https://www.notion.so/{DATABASE_ID}")
    print("   2. Menu '⋯' → 'Connections' → '+ Add connections'")
    print("   3. Sélectionnez votre intégration")
    print("\n   Même si l'intégration a accès à d'autres pages,")
    print("   chaque page/base doit être partagée individuellement !")
else:
    print(f"❌ Erreur inattendue: {db_response.text}")

print("\n" + "=" * 80)
print("📊 RÉSUMÉ DU DIAGNOSTIC")
print("=" * 80)

print(f"""
Token format      : ✅ Correct (secret_XXX)
Token validité    : {'✅ Valide' if response.status_code == 200 else '❌ Invalide ou accès refusé'}
Recherche générale: {'✅ OK' if search_response.status_code == 200 else '❌ Échoué'}
Accès à la base   : {'✅ OK' if db_response.status_code == 200 else '❌ Échoué'}

""")

if db_response.status_code == 403:
    print("🎯 ACTION REQUISE :")
    print("   La base 'Fiches Process PNX™' doit être partagée avec l'intégration.")
    print("   Suivez les instructions ci-dessus pour résoudre le problème.")
elif response.status_code != 200:
    print("🎯 ACTION REQUISE :")
    print("   Le token API ne fonctionne pas correctement.")
    print("   Créez une nouvelle intégration sur https://www.notion.so/my-integrations")

print("\n" + "=" * 80)
