# claudebridge-plugin-pronexus
Plugin Claude Code officiel ProNeXus™ (skills, subagents, slash, MCP)

## Configuration

### Notion Setup

To use the Notion publishing features, you need to configure your Notion API credentials:

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Get your Notion API key from [Notion Integrations](https://www.notion.so/my-integrations)

3. Add your credentials to `.env`:
   ```
   NOTION_API_KEY="your_notion_api_key"
   NOTION_DATABASE_ID="your_database_id"
   ```

4. Make sure your Notion integration has access to the target database

**Note:** The `.env` file is git-ignored to keep your credentials secure.
