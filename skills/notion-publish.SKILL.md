---
name: notion-publish
description: Publish content to Notion databases or pages, useful when users want to save analysis, documentation, or structured data to their Notion workspace
---

# Notion Publish Skill

## Overview

This Skill enables publishing content to Notion databases and pages. It's useful for:
- Saving analysis results and reports
- Creating documentation
- Populating databases with structured data
- Archiving conversation outputs

## When to Use

Activate this Skill when:
- User asks to "save this to Notion"
- Creating meeting notes or project documentation
- Exporting structured data or tables
- Publishing reports or analysis results

## Prerequisites

- Notion MCP server must be configured and running
- User must have Notion integration authorized
- Target database or page ID should be available

## Instructions

1. **Confirm Intent**: Verify the user wants to publish to Notion
2. **Identify Target**: Determine if publishing to:
   - Existing page (update)
   - New page in workspace
   - Database entry (with properties)
3. **Format Content**: Structure the content appropriately:
   - Use Notion blocks (headings, paragraphs, lists, code blocks)
   - Map structured data to database properties
   - Include relevant metadata (tags, dates, status)
4. **Execute Publish**: Use the Notion MCP tools to create/update content
5. **Confirm Success**: Provide the user with a link to the published content

## Content Formatting

### For Pages
- Use clear hierarchy with headings
- Include table of contents for long documents
- Add callouts for important information
- Link related pages when relevant

### For Database Entries
- Map fields correctly (text, number, select, date, etc.)
- Set appropriate status/tags
- Fill required properties
- Link to related entries

## Examples

### Example 1: Save Analysis Results

**User**: "Can you save this DVF analysis to Notion?"

**Actions**:
1. Format the DVF scores as a structured Notion page
2. Create new page in "Product Analysis" database
3. Set properties: Title, Score, Date, Status
4. Return link to created page

### Example 2: Create Meeting Notes

**User**: "Create meeting notes in Notion for our standup"

**Actions**:
1. Structure content with date, attendees, topics, action items
2. Create page in "Meeting Notes" database
3. Set meeting type, date, and tag relevant team
4. Return link for sharing

## Error Handling

- If Notion MCP not configured: Guide user to set up integration
- If database not found: Ask user for database ID or name
- If permissions error: Verify integration has necessary access
- Always provide clear error messages and next steps
