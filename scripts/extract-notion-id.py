#!/usr/bin/env python3
"""Extraction de l'ID depuis une URL Notion"""

import re

url = "https://www.notion.so/Rejoindre-la-Meute-WOLPH-GENESIS-2990a77e973481c4b8d3c6bbd008747a?source=copy_link"

# Extraire l'ID (32 caractères hexadécimaux à la fin de l'URL)
match = re.search(r'([a-f0-9]{32})', url)

if match:
    notion_id = match.group(1)
    print(f"✅ ID extrait : {notion_id}")

    # Comparer avec l'ancien ID
    old_id = "2990a77e973480fcade1cc37ef1c24a4"
    print(f"\n🔍 Comparaison :")
    print(f"   Ancien ID : {old_id}")
    print(f"   Nouvel ID : {notion_id}")

    if notion_id != old_id:
        print(f"\n⚠️  Les IDs sont DIFFÉRENTS !")
        print(f"\n💡 Cela explique pourquoi ça ne fonctionnait pas.")
        print(f"   Nous utilisions le mauvais ID de base !")
    else:
        print(f"\n✅ Les IDs sont identiques")
else:
    print("❌ Impossible d'extraire l'ID")
