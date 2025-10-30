#!/usr/bin/env python3
"""
Guide interactif pour configurer l'intégration Notion
"""

print("""
╔════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║       🔧 GUIDE DE CONFIGURATION NOTION - FICHES PROCESS PNX™              ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝

❌ PROBLÈME DÉTECTÉ : Erreur 403 (Access denied)

Votre token actuel : ntn_K28100913161JiojvrgismfGQZVDYtkv49qWUO3MOzw7rP

⚠️  Ce token ne fonctionne pas avec l'API Notion.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 ÉTAPES POUR RÉSOUDRE LE PROBLÈME :

┌────────────────────────────────────────────────────────────────────────────┐
│ ÉTAPE 1 : Créer une Intégration Notion                                    │
└────────────────────────────────────────────────────────────────────────────┘

1. Ouvrez ce lien dans votre navigateur :
   👉 https://www.notion.so/my-integrations

2. Cliquez sur le bouton "+ New integration"

3. Remplissez le formulaire :
   • Name: ProNeXus Claude Bridge
   • Associated workspace: [Sélectionnez votre workspace]
   • Type: Internal integration (par défaut)

4. Dans "Capabilities", cochez :
   ✅ Read content
   ✅ Update content
   ✅ Insert content

5. Cliquez sur "Submit"

6. ⭐ IMPORTANT : Copiez le "Internal Integration Secret"
   Format attendu : secret_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

   ⚠️  Ne partagez JAMAIS ce token publiquement !

┌────────────────────────────────────────────────────────────────────────────┐
│ ÉTAPE 2 : Partager votre Base Notion avec l'Intégration                   │
└────────────────────────────────────────────────────────────────────────────┘

1. Ouvrez votre base "Fiches Process PNX™" :
   👉 https://www.notion.so/2990a77e973480fcade1cc37ef1c24a4

2. En haut à droite de la page, cliquez sur le menu "⋯" (trois points)

3. Descendez jusqu'à la section "Connections"

4. Cliquez sur "Add connections"

5. Recherchez et sélectionnez "ProNeXus Claude Bridge"

6. L'intégration devrait maintenant apparaître dans la liste des connections

┌────────────────────────────────────────────────────────────────────────────┐
│ ÉTAPE 3 : Tester la Configuration                                         │
└────────────────────────────────────────────────────────────────────────────┘

Dans votre terminal, exécutez :

export NOTION_API_KEY="secret_VOTRE_TOKEN_ICI"
export NOTION_DATABASE_ID="2990a77e973480fcade1cc37ef1c24a4"

python3 scripts/test-notion-connection.py

Si vous voyez "✅ Accès autorisé !", passez à l'étape 4.
Sinon, revérifiez les étapes 1 et 2.

┌────────────────────────────────────────────────────────────────────────────┐
│ ÉTAPE 4 : Publier les Fiches                                              │
└────────────────────────────────────────────────────────────────────────────┘

Une fois le test réussi :

python3 scripts/publish-to-notion.py

Les 5 fiches (06-10) seront automatiquement publiées dans votre base Notion !

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔍 DIAGNOSTIC DU TOKEN ACTUEL :

Token fourni : ntn_K28100913161JiojvrgismfGQZVDYtkv49qWUO3MOzw7rP
Format      : ntn_XXXXXXXXX

❌ Format incorrect pour une intégration Notion.

Le format attendu pour une intégration est :
✅ secret_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Votre token commence par "ntn_" ce qui peut indiquer :
- Un token d'API utilisateur (deprecated)
- Un token expiré
- Un token invalide

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 BESOIN D'AIDE ?

Si vous rencontrez des difficultés :

1. Vérifiez que vous avez les permissions d'administrateur dans le workspace
2. Assurez-vous que la base et l'intégration sont dans le même workspace
3. Attendez 1-2 minutes après avoir partagé la base (synchronisation)
4. Essayez de supprimer et recréer l'intégration

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 DOCUMENTATION COMPLÈTE :

Consultez scripts/README-NOTION-PUBLISH.md pour plus de détails.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
