# CLAUDE CONTEXT LINK — WOLPH LAB GENESIS (MCP Full Sync)

## 🌌 Project Purpose & Objective

**Claude Forge Bridge** is an advanced MCP (Model Context Protocol) Full Sync integration system designed to create seamless, automated workflows between Claude AI interactions and the ProNeXus ecosystem. This system enables real-time synchronization of conversations, context, and artifacts across multiple platforms.

**Core Objective**: Establish a bidirectional bridge that captures Claude interactions, enriches them with structured metadata, and distributes them across Notion databases, GitHub repositories, Discord channels, and archival systems—all while maintaining perfect context coherence and traceability.

---

## 🔄 Step-by-Step Workflow

### 1. 📤 **Upload Phase**
- User initiates conversation with Claude via ProNeXus Bridge Plugin
- Conversation context, files, and metadata are captured in real-time
- System generates unique session IDs and timestamps
- Initial context tags are applied (project, domain, intent)

### 2. 🔗 **Sync Phase**
- MCP Full Sync protocol activates upon conversation milestones
- `transcript.md` is generated with full conversation history
- `links.yaml` extracts and structures all referenced URLs, files, and resources
- Context verification ensures all dependencies are captured
- Session metadata is enriched with GalaXLytique™ taxonomies

### 3. 📊 **Notion Integration**
- Structured data flows into Notion databases via API
- `template_fiche_galaxlytique.md` provides schema for Notion pages
- Key fields populated:
  - **Session ID** (unique identifier)
  - **Project Context** (linked entities)
  - **Artifacts** (generated files, code, documents)
  - **Status** (active, archived, review)
  - **Tags** (domain, technology, priority)
- Bidirectional sync maintains data consistency

### 4. 🐙 **GitHub Repository Push**
- Conversation artifacts committed to designated repository branch
- Branch naming convention: `claude/<task-description>-<session-id>`
- Commit messages follow conventional commits standard
- Files pushed:
  - `transcript.md` — Full conversation log
  - `CLAUDE.md` — Context link file
  - Generated code, configs, documentation
  - `links.yaml` — Resource reference map

### 5. 💬 **Discord Notification**
- Webhook triggers post to designated Discord channel
- Message includes:
  - 🎯 Session summary
  - 🔗 Links to Notion page and GitHub branch
  - 📋 Quick stats (duration, artifacts count, status)
  - 🏷️ Tag preview for discoverability
- Enables team awareness and collaboration triggers

### 6. 🗄️ **Archive Phase**
- Long-term storage in structured archive system
- Indexed by: date, project, session ID, tags
- Searchable via metadata fields
- Retention policies applied per project requirements
- Integration with backup systems

---

## 📁 Key Files & Components

### Core Files
- **`transcript.md`** — Complete conversation history with timestamps
- **`links.yaml`** — Structured reference map of all URLs, files, and external resources
- **`template_fiche_galaxlytique.md`** — Notion page schema template
- **`CLAUDE.md`** — Context link file (this file) for project-level instructions
- **`metadata.json`** — Session metadata (IDs, timestamps, tags, status)

### Configuration Files
- **`plugin.json`** — ProNeXus plugin configuration
- **`marketplace.json`** — Plugin marketplace metadata
- **`.github/workflows/`** — CI/CD automation for sync operations
- **`notion_config.yaml`** — Notion API settings and database IDs
- **`discord_webhooks.yaml`** — Discord integration endpoints

### Generated Artifacts
- Source code files (`.js`, `.ts`, `.py`, etc.)
- Documentation (`.md`, `.txt`)
- Configuration files (`.json`, `.yaml`, `.toml`)
- Data files (`.csv`, `.xlsx`, `.sql`)

---

## 🤖 Claude Forge Bridge Prompt Definition

When working with Claude Forge Bridge, use this prompt framework:

```markdown
### Context Initialization
- **Project**: [ProNeXus/WolphLab/GalaXLytique™/Other]
- **Domain**: [Development/Research/Documentation/Analysis]
- **Intent**: [Build/Debug/Refactor/Learn/Archive]
- **Session ID**: [Auto-generated or manual]

### Task Description
[Clear, specific description of what needs to be accomplished]

### Success Criteria
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

### Context Links
- Related Notion pages: [URLs]
- Related GitHub issues/PRs: [URLs]
- Previous sessions: [Session IDs]
- External resources: [URLs]

### Output Requirements
- Generate transcript.md: [Yes/No]
- Push to GitHub: [Yes/No]
- Sync to Notion: [Yes/No]
- Notify Discord: [Yes/No]
```

---

## ✅ Context Linking & Verification

### Context Verification Checklist
- ✓ **Session ID Assigned**: Unique identifier generated and tracked
- ✓ **Project Context Linked**: Properly tagged and associated with parent project
- ✓ **Dependencies Captured**: All referenced files, URLs, and resources documented
- ✓ **Metadata Complete**: All required fields populated (date, author, status, tags)
- ✓ **Sync Status Confirmed**: Successful push to Notion, GitHub, Discord verified
- ✓ **Archive Status**: Long-term storage confirmed with retention policy applied

### Context Link Verification
Every session must include:
```yaml
context:
  linked_to_project: true
  project_name: "claudebridge-plugin-pronexus"
  session_id: "unique-session-identifier"
  sync_status: "completed"
  verification_timestamp: "YYYY-MM-DD HH:MM:SS UTC"
  platforms:
    - notion: "synced"
    - github: "pushed"
    - discord: "notified"
    - archive: "stored"
```

---

## 🎨 GalaXLytique™ Style Guidelines

### Emoji Markers
- 🌌 Vision & Strategy
- 🔄 Workflows & Processes
- 📤 Input/Upload Operations
- 📥 Output/Download Operations
- 🔗 Integrations & Connections
- 📊 Data & Analytics
- 🐙 GitHub Operations
- 💬 Communication & Notifications
- 🗄️ Storage & Archives
- 🤖 AI & Automation
- ✅ Verification & Validation
- 🎯 Goals & Objectives
- 🏷️ Tags & Metadata
- 📁 Files & Documents
- 🎨 Design & Style

### Heading Structure
```markdown
# 🌌 Level 1: Major Sections
## 🔄 Level 2: Subsections
### 📊 Level 3: Components
#### 🔗 Level 4: Details
```

---

## 🔐 Security & Privacy Notes

- All sensitive data (API keys, tokens, credentials) stored in environment variables
- Never commit secrets to version control
- Use `.env.local` for local development
- GitHub secrets for CI/CD pipelines
- Notion API tokens rotated regularly
- Discord webhook URLs kept private

---

## 📚 Additional Resources

- [ProNeXus Documentation](https://pronexus.ai/docs)
- [MCP Protocol Specification](https://github.com/anthropics/mcp)
- [Notion API Reference](https://developers.notion.com)
- [Discord Webhooks Guide](https://discord.com/developers/docs/resources/webhook)
- [GalaXLytique™ Framework](https://galaxlytique.wolph.lab)

---

**Last Updated**: 2025-10-30
**Version**: 1.0.0
**Maintained By**: Wolph Lab Genesis Team
**Status**: 🟢 Active Development
