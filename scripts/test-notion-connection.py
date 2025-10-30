#!/usr/bin/env python3
"""Test de connexion à l'API Notion"""

import requests
import json

NOTION_API_KEY = "ntn_K28100913161JiojvrgismfGQZVDYtkv49qWUO3MOzw7rP"
DATABASE_ID = "2990a77e973480fcade1cc37ef1c24a4"

# Test 1: Vérifier le token en listant les bases accessibles
print("🔍 Test de connexion à l'API Notion...")
print("=" * 60)

headers = {
    'Authorization': f'Bearer {NOTION_API_KEY}',
    'Notion-Version': '2022-06-28',
    'Content-Type': 'application/json'
}

# Test d'accès à la base
print(f"\n📊 Test d'accès à la base : {DATABASE_ID}")
response = requests.get(
    f'https://api.notion.com/v1/databases/{DATABASE_ID}',
    headers=headers
)

print(f"Status: {response.status_code}")
print(f"Response: {response.text[:500]}")

if response.status_code == 200:
    print("\n✅ Accès autorisé ! La base est accessible.")
    data = response.json()
    print(f"Titre de la base : {data.get('title', [{}])[0].get('plain_text', 'N/A')}")
elif response.status_code == 404:
    print("\n❌ Base non trouvée (404)")
    print("Vérifiez l'ID de la base dans l'URL Notion")
elif response.status_code == 401:
    print("\n❌ Token invalide (401)")
    print("Vérifiez que le token API est correct")
else:
    print(f"\n❌ Erreur {response.status_code}")

# Test 2: Lister les bases de recherche
print("\n\n🔎 Test de recherche des bases accessibles...")
search_response = requests.post(
    'https://api.notion.com/v1/search',
    headers=headers,
    json={
        "filter": {
            "property": "object",
            "value": "database"
        },
        "page_size": 10
    }
)

print(f"Status: {search_response.status_code}")

if search_response.status_code == 200:
    data = search_response.json()
    results = data.get('results', [])
    print(f"\n✅ {len(results)} base(s) accessible(s) avec cette intégration:")
    for db in results:
        title = db.get('title', [{}])[0].get('plain_text', 'Sans titre') if db.get('title') else 'Sans titre'
        db_id = db.get('id', 'N/A')
        print(f"   - {title} (ID: {db_id})")

    if len(results) == 0:
        print("\n⚠️  Aucune base n'est partagée avec cette intégration !")
        print("\n📝 Pour partager une base avec votre intégration :")
        print("   1. Ouvrez votre base Notion 'Fiches Process PNX™'")
        print("   2. Cliquez sur '⋯' (menu) en haut à droite")
        print("   3. Sélectionnez 'Connections' ou 'Add connections'")
        print("   4. Recherchez et ajoutez votre intégration")
else:
    print(f"❌ Erreur lors de la recherche: {search_response.text}")
