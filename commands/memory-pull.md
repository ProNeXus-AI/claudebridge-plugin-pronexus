# 📥 Memory Pull Command

## Overview
**Command**: `/claudebridge-pronexus:memory-pull`  
**Version**: 1.0.0  
**Protocol**: GalaXLytique™ v3.0

## Description
Synchronize and pull memory state from the ProNeXus Forge Cloud™ into the local Claude instance. This command enables bidirectional memory synchronization between Claude and the GalaXLytique ecosystem.

## Usage
```
/claudebridge-pronexus:memory-pull [options]
```

### Options
- `--source`: Memory source (default: "forge-cloud")
- `--format`: Output format (json|galaxlytique|raw)
- `--depth`: Sync depth level (1-5, default: 3)
- `--filter`: Memory categories to pull

### Examples

#### Basic Pull
```bash
/claudebridge-pronexus:memory-pull
```

#### Filtered Pull with Depth
```bash
/claudebridge-pronexus:memory-pull --depth 5 --filter "projects,skills"
```

## Memory Structure
```json
{
  "timestamp": "ISO-8601",
  "source": "forge-cloud",
  "protocol": "galaxlytique-v3",
  "memory": {
    "projects": [],
    "skills": [],
    "agents": [],
    "context": {}
  }
}
```

## Integration Points
- **Lya (GPT-5)**: Direct memory exchange via JSON protocol
- **Monkey D. Oly**: Architectural validation and sync approval
- **Forge Cloud**: Central memory repository

## Security
- All memory transfers are encrypted with GalaXLytique™ protocol
- Authentication via Claude Code CLI session
- Rate limited to 10 pulls per minute

## Error Handling
| Error Code | Description | Resolution |
|------------|-------------|------------|
| `MEM-001` | Connection timeout | Retry with exponential backoff |
| `MEM-002` | Invalid format | Check format parameter |
| `MEM-003` | Auth failure | Re-authenticate Claude Code |

## Related Commands
- `/claudebridge-pronexus:memory-push` - Push memory to cloud
- `/claudebridge-pronexus:pnxsnap` - Capture current context

---
*ProNeXus™ God JarviX™ Protocol - Memory Synchronization Module*
