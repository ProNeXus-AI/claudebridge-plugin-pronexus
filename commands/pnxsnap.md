---
description: Create a ProNeXus snapshot - capture current project state, generate DVF analysis, and optionally publish to Notion
argument-hint: [target-path] [--publish]
allowed-tools: Read, Glob, Grep, TodoWrite
model: sonnet
---

# ProNeXus Snapshot Command

Create a comprehensive snapshot of the current project or specified path, including:
- Project structure overview
- Key files and documentation
- Current status and progress
- Optional DVF analysis for pending features
- Optional publishing to Notion

## Usage

```
/pnxsnap                          # Snapshot current directory
/pnxsnap ./src                    # Snapshot specific path
/pnxsnap . --publish              # Snapshot and publish to Notion
```

## Instructions

1. **Analyze Structure**: Examine the project at the specified path (default: current directory)
   - Identify key directories and files
   - Look for README, package.json, or other project metadata
   - Note any TODO files or task lists

2. **Generate Overview**: Create a structured summary including:
   - **Project Name**: From package.json or directory name
   - **Purpose**: From README or inferred from structure
   - **Structure**: Key directories and their purpose
   - **Recent Changes**: If git available, check recent commits
   - **Open Tasks**: From TODO files or todo lists

3. **Optional DVF Analysis**: If there are pending features or proposals:
   - Identify feature candidates from issues or TODO comments
   - Provide quick DVF scores for top 3-5 items
   - Recommend prioritization

4. **Format Output**: Present as a well-structured markdown document with:
   - Executive summary
   - Detailed sections for each component
   - Actionable insights and recommendations

5. **Optional Publishing**: If `--publish` flag is present:
   - Ask user for Notion database/page target
   - Format snapshot for Notion
   - Publish using Notion MCP or notion-publish Skill
   - Return link to published snapshot

## Output Template

```markdown
# Project Snapshot: [Project Name]
*Captured: [Date/Time]*

## Executive Summary
[2-3 sentence overview]

## Project Structure
- `directory/` - [purpose]
- `file.ext` - [description]

## Current Status
- [Key metrics or progress indicators]

## Pending Work
- [ ] Task 1
- [ ] Task 2

## DVF Analysis (if applicable)
| Feature | D | V | F | Overall | Priority |
|---------|---|---|---|---------|----------|
| Feature 1 | 8 | 7 | 6 | 7.0 | High |

## Recommendations
1. [Actionable recommendation]
2. [Next steps]
```

## Notes

- Respects .gitignore and only analyzes accessible files
- Sensitive files (.env, credentials) are noted but not included in output
- For large projects, focuses on most relevant/changed files
