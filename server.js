#!/usr/bin/env node

import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
  ListResourcesRequestSchema,
  ReadResourceRequestSchema,
} from '@modelcontextprotocol/sdk/types.js';
import fs from 'fs/promises';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Helper function to read markdown files
async function readMarkdownFile(filePath) {
  try {
    const content = await fs.readFile(filePath, 'utf-8');
    return content;
  } catch (error) {
    console.error(`Error reading file ${filePath}:`, error);
    return null;
  }
}

// Helper function to parse frontmatter
function parseFrontmatter(content) {
  const frontmatterRegex = /^---\n([\s\S]*?)\n---\n([\s\S]*)$/;
  const match = content.match(frontmatterRegex);

  if (!match) {
    return { metadata: {}, body: content };
  }

  const metadata = {};
  const frontmatter = match[1];
  const body = match[2];

  frontmatter.split('\n').forEach(line => {
    const [key, ...valueParts] = line.split(':');
    if (key && valueParts.length > 0) {
      metadata[key.trim()] = valueParts.join(':').trim();
    }
  });

  return { metadata, body };
}

// Helper function to discover resources
async function discoverResources() {
  const resources = [];
  const directories = ['skills', 'commands', 'agents'];

  for (const dir of directories) {
    const dirPath = path.join(__dirname, dir);
    try {
      const files = await fs.readdir(dirPath);
      for (const file of files) {
        if (file.endsWith('.md') || file.endsWith('.SKILL.md')) {
          const filePath = path.join(dirPath, file);
          const content = await readMarkdownFile(filePath);
          if (content) {
            const { metadata } = parseFrontmatter(content);
            resources.push({
              uri: `pronexus://${dir}/${file}`,
              name: metadata.name || file.replace(/\.(SKILL\.)?md$/, ''),
              description: metadata.description || `Resource from ${dir}/${file}`,
              mimeType: 'text/markdown',
              filePath,
            });
          }
        }
      }
    } catch (error) {
      console.error(`Error reading directory ${dir}:`, error);
    }
  }

  return resources;
}

// Create MCP server
const server = new Server(
  {
    name: 'claudebridge-pronexus',
    version: '1.0.0',
  },
  {
    capabilities: {
      tools: {},
      resources: {},
    },
  }
);

// Store discovered resources
let cachedResources = null;

// List tools handler
server.setRequestHandler(ListToolsRequestSchema, async () => {
  const resources = cachedResources || await discoverResources();

  const tools = resources
    .filter(r => r.uri.includes('/skills/'))
    .map(resource => ({
      name: resource.name,
      description: resource.description,
      inputSchema: {
        type: 'object',
        properties: {
          input: {
            type: 'string',
            description: 'Input data or context for the skill',
          },
        },
        required: [],
      },
    }));

  return { tools };
});

// Call tool handler
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  const resources = cachedResources || await discoverResources();
  const skill = resources.find(r => r.name === name && r.uri.includes('/skills/'));

  if (!skill) {
    throw new Error(`Tool ${name} not found`);
  }

  const content = await readMarkdownFile(skill.filePath);
  const { body } = parseFrontmatter(content);

  return {
    content: [
      {
        type: 'text',
        text: `Executing skill: ${name}\n\nSkill Instructions:\n${body}\n\nInput: ${JSON.stringify(args, null, 2)}`,
      },
    ],
  };
});

// List resources handler
server.setRequestHandler(ListResourcesRequestSchema, async () => {
  if (!cachedResources) {
    cachedResources = await discoverResources();
  }

  return {
    resources: cachedResources.map(r => ({
      uri: r.uri,
      name: r.name,
      description: r.description,
      mimeType: r.mimeType,
    })),
  };
});

// Read resource handler
server.setRequestHandler(ReadResourceRequestSchema, async (request) => {
  const { uri } = request.params;

  const resources = cachedResources || await discoverResources();
  const resource = resources.find(r => r.uri === uri);

  if (!resource) {
    throw new Error(`Resource ${uri} not found`);
  }

  const content = await readMarkdownFile(resource.filePath);

  return {
    contents: [
      {
        uri: resource.uri,
        mimeType: resource.mimeType,
        text: content,
      },
    ],
  };
});

// Start server
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error('ClaudeBridge ProNeXus MCP Server running on stdio');
}

main().catch((error) => {
  console.error('Server error:', error);
  process.exit(1);
});
