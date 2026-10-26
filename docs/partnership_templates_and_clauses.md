# Partnership Agreement Templates and Clause Definitions

This document defines the guidelines and specifications for creating and managing standard partnership templates, parameter substitution rules, and clause schema guidelines in the Freedom Platform.

## Standard Partnership Templates

Partnership templates serve as the foundation for collaboration proposals. They provide a structured format for outlining the problem, scope, deliverables, and terms of a partnership.

### Template Structure

A standard partnership template should include the following sections:

1.  **Title and Objective:** A clear, concise title for the partnership and a brief statement of the main goal.
2.  **Problem Statement:** A description of the current situation, challenges, and who is affected.
3.  **Scope and Resources:** A list of available resources, time commitments, known constraints, and what is explicitly excluded from the current phase.
4.  **Minimal Viable Deliverable (MVD):** A defined, small-scale output to validate the partnership's value.
5.  **Deliverables and Timeline:** A clear list of expected outcomes and their deadlines.
6.  **Next Steps and Feedback:** The process for reviewing the work, providing feedback, and determining subsequent actions.

## Parameter Substitution Rules

Templates utilize parameters to allow for customization without altering the core structure. These parameters should follow a specific syntax for easy identification and replacement.

### Syntax

Parameters are enclosed in double curly braces: `{{PARAMETER_NAME}}`.

### Standard Parameters

*   `{{PARTNER_A_NAME}}`: The name of the first party involved.
*   `{{PARTNER_B_NAME}}`: The name of the second party involved.
*   `{{PROJECT_TITLE}}`: The name of the proposed project.
*   `{{START_DATE}}`: The agreed-upon commencement date.
*   `{{END_DATE}}`: The anticipated completion date.
*   `{{DELIVERABLE_DESCRIPTION}}`: A brief explanation of the expected output.
*   `{{PAYMENT_TERMS}}`: Details regarding compensation, if applicable.

### Substitution Process

When generating a specific proposal from a template, all instances of `{{PARAMETER_NAME}}` must be replaced with the appropriate values. If a parameter is not applicable, it should be removed or replaced with "N/A" rather than left blank.

## Clause Schema Guidelines

Clauses represent specific, reusable terms or conditions within an agreement. Standardizing their schema ensures consistency and allows for automated processing or validation.

### Schema Definition

Each clause should be defined as a JSON object with the following properties:

*   `id` (string, required): A unique identifier for the clause (e.g., `clause_confidentiality_v1`).
*   `title` (string, required): A human-readable name for the clause.
*   `description` (string, optional): A brief explanation of the clause's purpose.
*   `content` (string, required): The actual text of the clause. This may contain substitution parameters.
*   `type` (string, required): The category of the clause (e.g., `liability`, `confidentiality`, `payment`, `deliverables`).
*   `version` (string, required): Semantic versioning (e.g., `1.0.0`) to track updates.
*   `required` (boolean, default: false): Indicates if the clause is mandatory for all agreements of a certain type.

### Example Clause Schema

```json
{
  "id": "clause_confidentiality_basic",
  "title": "Basic Confidentiality",
  "description": "Standard non-disclosure agreement for project discussions.",
  "content": "Both parties agree to keep all shared information related to {{PROJECT_TITLE}} confidential and not disclose it to third parties without prior written consent.",
  "type": "confidentiality",
  "version": "1.0.0",
  "required": true
}
```

### Usage Guidelines

1.  **Reusability:** Design clauses to be as generic and reusable as possible, relying on parameters for specific details.
2.  **Clarity:** Ensure the language within the clause is clear, concise, and unambiguous.
3.  **Versioning:** When modifying an existing clause, create a new version and update the `version` field. Do not overwrite existing versions if they are still in use.
