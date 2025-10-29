---
name: dvf-score
description: Calculate DVF (Desirability, Viability, Feasibility) scores for ideas, features, or projects to help prioritize and evaluate opportunities
---

# DVF Scoring Skill

## Overview

This Skill helps evaluate ideas, features, products, or projects using the DVF framework:
- **Desirability**: How much do users want this?
- **Viability**: Is it economically sustainable?
- **Feasibility**: Can we build it with our resources?

## When to Use

Use this Skill when:
- Evaluating feature requests or product ideas
- Prioritizing a backlog
- Making go/no-go decisions
- Comparing multiple opportunities

## Instructions

1. **Gather Context**: Ask the user for relevant details about what they're evaluating
2. **Score Each Dimension** (1-10 scale):
   - **Desirability**: User demand, market need, problem severity
   - **Viability**: Business model, revenue potential, strategic fit
   - **Feasibility**: Technical complexity, resource availability, time required
3. **Calculate Composite Score**: Average or weighted average of the three dimensions
4. **Provide Recommendation**: Explain the scores and suggest next steps

## Output Format

```
DVF Analysis for: [Thing Being Evaluated]

Desirability: X/10
- [Key factors]

Viability: X/10
- [Key factors]

Feasibility: X/10
- [Key factors]

Overall DVF Score: X.X/10
Recommendation: [Go/No-Go/Conditional with explanation]
```

## Examples

### Example 1: Feature Request

**Input**: "Should we add dark mode to our app?"

**Analysis**:
- Desirability: 8/10 - Frequently requested by users
- Viability: 7/10 - Increases user satisfaction, minimal cost
- Feasibility: 6/10 - Requires CSS refactoring, 2-week effort

**Overall**: 7/10 - Recommend prioritizing after current sprint

### Example 2: New Product

**Input**: "Should we launch a mobile app?"

**Analysis**:
- Desirability: 9/10 - Strong market demand
- Viability: 5/10 - High development/maintenance costs
- Feasibility: 4/10 - Requires hiring mobile developers

**Overall**: 6/10 - Consider phased approach or PWA first
