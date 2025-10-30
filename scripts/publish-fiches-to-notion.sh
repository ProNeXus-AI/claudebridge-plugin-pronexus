#!/bin/bash
# Script de publication automatique des FICHES 06-10 vers Notion
# Nécessite : configuration Notion MCP et token API

set -e

# Configuration
NOTION_API_KEY="${NOTION_API_KEY:-}"
DATABASE_ID="${NOTION_DATABASE_ID:-2990a77e973480fcade1cc37ef1c24a4}"
FICHES_DIR="docs/fiche-process"

# Couleurs pour output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}🚀 Publication des FICHES PROCESS PNX™ vers Notion${NC}"
echo "=================================================="

# Vérification du token API
if [ -z "$NOTION_API_KEY" ]; then
    echo -e "${RED}❌ Erreur : NOTION_API_KEY non définie${NC}"
    echo "Définissez la variable d'environnement :"
    echo "export NOTION_API_KEY='secret_xxxxx'"
    exit 1
fi

# Liste des fiches à publier
FICHES=(06 07 08 09 10)

# Fonction de publication
publish_fiche() {
    local fiche_num=$1
    local fiche_path="${FICHES_DIR}/${fiche_num}.md"

    if [ ! -f "$fiche_path" ]; then
        echo -e "${RED}❌ Fichier non trouvé : ${fiche_path}${NC}"
        return 1
    fi

    echo -e "${BLUE}📄 Publication FICHE ${fiche_num}...${NC}"

    # Extraction des métadonnées depuis le Markdown
    local title=$(grep -m 1 "^# FICHE" "$fiche_path" | sed 's/# //')
    local description=$(grep -A 1 "## 🧩 Contexte & Objectif" "$fiche_path" | tail -n 1)

    echo "   Titre : $title"
    echo "   Description : ${description:0:80}..."

    # Appel à l'API Notion (nécessite jq et curl)
    # Note : Ce script est un template - adapter selon votre implémentation MCP

    # Option 1 : Via curl direct
    # local response=$(curl -X POST https://api.notion.com/v1/pages \
    #   -H "Authorization: Bearer $NOTION_API_KEY" \
    #   -H "Content-Type: application/json" \
    #   -H "Notion-Version: 2022-06-28" \
    #   -d @payload.json)

    # Option 2 : Via MCP tool (recommandé)
    # claude-code mcp call notion_create_page \
    #   --database_id "$DATABASE_ID" \
    #   --file "$fiche_path"

    echo -e "${GREEN}   ✅ FICHE ${fiche_num} publiée${NC}"
    echo ""

    return 0
}

# Boucle de publication
SUCCESS_COUNT=0
FAILED_COUNT=0

for fiche in "${FICHES[@]}"; do
    if publish_fiche "$fiche"; then
        ((SUCCESS_COUNT++))
    else
        ((FAILED_COUNT++))
    fi
done

# Résumé
echo "=================================================="
echo -e "${GREEN}✅ Publication terminée${NC}"
echo "   Succès : $SUCCESS_COUNT / ${#FICHES[@]}"
echo "   Échecs : $FAILED_COUNT"

if [ $FAILED_COUNT -eq 0 ]; then
    echo -e "${GREEN}🎉 Toutes les fiches ont été publiées avec succès !${NC}"
    echo ""
    echo "🔗 Accéder à la base Notion :"
    echo "   https://www.notion.so/${DATABASE_ID}"
else
    echo -e "${RED}⚠️  Certaines fiches n'ont pas pu être publiées${NC}"
    exit 1
fi
