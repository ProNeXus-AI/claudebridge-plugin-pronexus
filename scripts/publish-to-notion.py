#!/usr/bin/env python3
"""
Script de publication des FICHES PROCESS PNX™ vers Notion
Utilise l'API Notion officielle avec conversion Markdown → Blocks
"""

import os
import json
import re
from pathlib import Path
from typing import List, Dict, Any
import requests

# Configuration
NOTION_API_KEY = os.getenv('NOTION_API_KEY', '')
DATABASE_ID = os.getenv('NOTION_DATABASE_ID', '2990a77e973480fcade1cc37ef1c24a4')
NOTION_VERSION = '2022-06-28'
FICHES_DIR = Path('docs/fiche-process')

# Headers pour l'API Notion
HEADERS = {
    'Authorization': f'Bearer {NOTION_API_KEY}',
    'Content-Type': 'application/json',
    'Notion-Version': NOTION_VERSION
}


class MarkdownToNotion:
    """Convertisseur Markdown → Notion Blocks"""

    @staticmethod
    def parse_markdown(content: str) -> List[Dict[str, Any]]:
        """Parse Markdown et retourne des blocs Notion"""
        blocks = []
        lines = content.split('\n')
        i = 0

        while i < len(lines):
            line = lines[i]

            # Heading 1
            if line.startswith('# '):
                blocks.append({
                    'object': 'block',
                    'type': 'heading_1',
                    'heading_1': {
                        'rich_text': [{'text': {'content': line[2:]}}]
                    }
                })

            # Heading 2
            elif line.startswith('## '):
                blocks.append({
                    'object': 'block',
                    'type': 'heading_2',
                    'heading_2': {
                        'rich_text': [{'text': {'content': line[3:]}}]
                    }
                })

            # Heading 3
            elif line.startswith('### '):
                blocks.append({
                    'object': 'block',
                    'type': 'heading_3',
                    'heading_3': {
                        'rich_text': [{'text': {'content': line[4:]}}]
                    }
                })

            # Code block
            elif line.startswith('```'):
                language = line[3:].strip() or 'plain text'
                code_lines = []
                i += 1
                while i < len(lines) and not lines[i].startswith('```'):
                    code_lines.append(lines[i])
                    i += 1

                code_content = '\n'.join(code_lines)
                if len(code_content) > 2000:
                    code_content = code_content[:1997] + '...'

                blocks.append({
                    'object': 'block',
                    'type': 'code',
                    'code': {
                        'language': language,
                        'rich_text': [{'text': {'content': code_content}}]
                    }
                })

            # Bullet list
            elif line.startswith('- ') or line.startswith('* '):
                blocks.append({
                    'object': 'block',
                    'type': 'bulleted_list_item',
                    'bulleted_list_item': {
                        'rich_text': [{'text': {'content': line[2:]}}]
                    }
                })

            # Numbered list
            elif re.match(r'^\d+\. ', line):
                content = re.sub(r'^\d+\. ', '', line)
                blocks.append({
                    'object': 'block',
                    'type': 'numbered_list_item',
                    'numbered_list_item': {
                        'rich_text': [{'text': {'content': content}}]
                    }
                })

            # Divider
            elif line.strip() == '---':
                blocks.append({
                    'object': 'block',
                    'type': 'divider',
                    'divider': {}
                })

            # Paragraph (skip empty lines)
            elif line.strip():
                # Limiter la longueur du paragraphe
                content = line[:2000]
                blocks.append({
                    'object': 'block',
                    'type': 'paragraph',
                    'paragraph': {
                        'rich_text': [{'text': {'content': content}}]
                    }
                })

            i += 1

        return blocks


class NotionPublisher:
    """Gestionnaire de publication vers Notion"""

    def __init__(self, api_key: str, database_id: str):
        self.api_key = api_key
        self.database_id = database_id
        self.base_url = 'https://api.notion.com/v1'

    def extract_metadata(self, content: str) -> Dict[str, str]:
        """Extrait les métadonnées depuis le contenu Markdown"""
        metadata = {
            'title': 'Sans titre',
            'description': '',
            'niveau': 'Avancé',
            'statut': 'Public'
        }

        # Titre
        title_match = re.search(r'^# (FICHE \d+ — .+)$', content, re.MULTILINE)
        if title_match:
            metadata['title'] = title_match.group(1)

        # Description (première phrase du contexte)
        desc_match = re.search(r'## 🧩 Contexte & Objectif\n\n(.+)', content)
        if desc_match:
            metadata['description'] = desc_match.group(1)[:200]

        # Niveau
        niveau_match = re.search(r'\*\*(.+?)\*\*', content)
        if niveau_match:
            niveau = niveau_match.group(1)
            if niveau in ['Débutant', 'Intermédiaire', 'Avancé', 'Expert']:
                metadata['niveau'] = niveau

        return metadata

    def create_page(self, file_path: Path) -> Dict[str, Any]:
        """Crée une page Notion depuis un fichier Markdown"""

        # Lire le contenu
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extraire métadonnées
        metadata = self.extract_metadata(content)

        # Convertir en blocks Notion
        blocks = MarkdownToNotion.parse_markdown(content)

        # Limiter à 100 blocks (limite API Notion)
        if len(blocks) > 100:
            blocks = blocks[:100]
            blocks.append({
                'object': 'block',
                'type': 'callout',
                'callout': {
                    'icon': {'emoji': '⚠️'},
                    'rich_text': [{
                        'text': {'content': 'Contenu tronqué : voir fichier source pour la version complète'}
                    }]
                }
            })

        # Payload pour l'API Notion
        payload = {
            'parent': {'database_id': self.database_id},
            'properties': {
                'Nom du Process': {
                    'title': [{'text': {'content': metadata['title']}}]
                },
                'Description': {
                    'rich_text': [{'text': {'content': metadata['description']}}]
                },
                'Statut': {
                    'select': {'name': metadata['statut']}
                },
                'Niveau': {
                    'select': {'name': metadata['niveau']}
                }
            },
            'children': blocks
        }

        # Appel API
        response = requests.post(
            f'{self.base_url}/pages',
            headers=HEADERS,
            json=payload
        )

        if response.status_code == 200:
            result = response.json()
            return {
                'success': True,
                'page_id': result['id'],
                'url': result['url'],
                'title': metadata['title']
            }
        else:
            return {
                'success': False,
                'error': response.text,
                'title': metadata['title']
            }


def main():
    """Fonction principale"""

    print("🚀 Publication des FICHES PROCESS PNX™ vers Notion")
    print("=" * 60)

    # Vérification du token
    if not NOTION_API_KEY:
        print("❌ Erreur : NOTION_API_KEY non définie")
        print("\nDéfinissez la variable d'environnement :")
        print("export NOTION_API_KEY='secret_xxxxx'")
        return 1

    # Vérification du répertoire
    if not FICHES_DIR.exists():
        print(f"❌ Erreur : Répertoire {FICHES_DIR} introuvable")
        return 1

    # Initialiser le publisher
    publisher = NotionPublisher(NOTION_API_KEY, DATABASE_ID)

    # Liste des fiches
    fiches = sorted(FICHES_DIR.glob('*.md'))

    if not fiches:
        print(f"❌ Aucune fiche trouvée dans {FICHES_DIR}")
        return 1

    print(f"\n📄 {len(fiches)} fiche(s) trouvée(s)\n")

    # Publication
    results = []
    for fiche_path in fiches:
        print(f"📝 Publication : {fiche_path.name}...", end=' ')

        try:
            result = publisher.create_page(fiche_path)
            results.append(result)

            if result['success']:
                print(f"✅")
                print(f"   🔗 {result['url']}")
            else:
                print(f"❌")
                print(f"   Erreur : {result['error'][:100]}")

        except Exception as e:
            print(f"❌")
            print(f"   Exception : {str(e)}")
            results.append({'success': False, 'error': str(e)})

    # Résumé
    success_count = sum(1 for r in results if r.get('success'))
    failed_count = len(results) - success_count

    print("\n" + "=" * 60)
    print(f"✅ Publication terminée")
    print(f"   Succès : {success_count} / {len(results)}")
    print(f"   Échecs : {failed_count}")

    if failed_count == 0:
        print("\n🎉 Toutes les fiches ont été publiées avec succès !")
        print(f"\n🔗 Base Notion : https://www.notion.so/{DATABASE_ID}")
        return 0
    else:
        print("\n⚠️  Certaines fiches n'ont pas pu être publiées")
        return 1


if __name__ == '__main__':
    exit(main())
