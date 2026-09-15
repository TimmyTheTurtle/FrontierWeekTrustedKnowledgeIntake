# Stage 0 architecture diagrams

These diagrams make the repository foundation and the intended Trusted Knowledge
Intake boundary easier to review. They are architecture documentation, not
runtime behavior or a commitment to a particular service, vendor, or deployment.

## Reading the diagrams

- **Implemented Stage 0** means a repository artifact exists today.
- **Planned** means a later roadmap stage may implement that responsibility; it
  is not present in the codebase.
- Solid entity relationships describe provenance and approval boundaries, not a
  database schema.

## 1. System boundary and staged flow

The foundation now defines the contract. The path from source capture through
human approval is intentionally shown as planned work so the later stages do not
blur the implemented boundary.

```mermaid
flowchart LR
    subgraph foundation[Implemented Stage 0 — repository foundation]
        direction TB
        Docs[Canonical docs and ADRs]
        Models[Separate domain models]
        Rules[Deterministic IDs, validation, review-state rules]
        Tests[Focused unit tests and CI]
        Docs --> Models
        Models --> Rules
        Rules --> Tests
    end

    subgraph intake[Planned Trusted Knowledge Intake]
        direction LR
        Submit[Submit source] --> Artifact[Preserve Source Artifact]
        Artifact --> Parse[Deterministic structural parsing]
        Parse --> Chunks[Source-faithful Retrieval Chunks]
        Chunks --> Analyst[Intake Analyst proposal]
        Analyst --> Candidate[Candidate Knowledge Record]
        Candidate --> Steward[Knowledge Steward comparison]
        Steward --> Package[Human review package]
        Package --> Human{Human decision}
        Human -->|approve| Trusted[Eligible for trusted retrieval]
        Human -->|revise, quarantine, or reject| Held[Not trusted]
    end

    foundation -. establishes constraints for .-> intake
```

## 2. Domain class diagram

This is a UML-style view of the three separate entities and the review-state
rules that already exist as minimal models and validation helpers. It does not
claim that persistence or parsing is implemented.

```mermaid
classDiagram
    class SourceArtifact {
        +source_id: str
        +origin: str
        +content_type: str
        +captured_at: str
        +content_hash: str
        +license_note: str
        +trust_classification: str
        +raw_reference: str
    }

    class KnowledgeRecord {
        +record_id: str
        +source_ids: tuple[str]
        +title: str
        +summary: str
        +concepts: tuple[str]
        +candidate_claims: tuple[str]
        +authority_class: str
        +review_state: str
        +decision_provenance: str?
    }

    class RetrievalChunk {
        +chunk_id: str
        +source_id: str
        +record_id: str?
        +parent_section_id: str
        +content: str
        +content_hash: str
        +heading_path: tuple[str]
        +location: str
        +chunk_type: str
        +review_state: str
    }

    class KnowledgeRelationship {
        +relation_type: str
        +target_id: str
        +note: str?
    }

    class ReviewStateRules {
        +can_transition(from, to): bool
        +requires_human_decision(state): bool
        +is_terminal_state(state): bool
    }

    KnowledgeRecord "1" --> "1..*" SourceArtifact : derived from
    RetrievalChunk "*" --> "1" SourceArtifact : source-faithful part of
    RetrievalChunk "*" --> "0..1" KnowledgeRecord : optionally associated with
    KnowledgeRecord "1" *-- "0..*" KnowledgeRelationship
    KnowledgeRecord ..> ReviewStateRules : validated by
    RetrievalChunk ..> ReviewStateRules : state checked by
```

## 3. Intended deterministic-ingestion sequence

This sequence is the bounded target for Stage 1. The only actor-side result is a
preserved artifact and validated chunks; it deliberately stops before any agent
proposal or trusted retrieval.

```mermaid
sequenceDiagram
    actor Submitter
    participant Intake as Deterministic intake (planned Stage 1)
    participant Artifact as Source Artifact
    participant Parser as Structural parser
    participant Chunks as Retrieval Chunks

    Submitter->>Intake: submit Markdown or plain text with provenance
    Intake->>Artifact: preserve immutable raw content
    Intake->>Artifact: calculate stable hash and ID
    Intake->>Parser: parse native document structure
    Parser-->>Intake: sections and structural locations
    Intake->>Chunks: create source-faithful chunks with provenance
    Intake->>Intake: validate entities and review state
    Intake-->>Submitter: report captured / parsed output
    Note over Intake,Chunks: No agent, approval, or retrieval occurs in Stage 1.
```

## 4. Intended human-approval sequence

Human authority is the essential control point. Agent recommendations remain
candidate information until a human makes and records a decision.

```mermaid
sequenceDiagram
    participant Analyst as Intake Analyst (planned Stage 2)
    participant Steward as Knowledge Steward (planned Stage 3)
    participant Review as Review package
    actor Human as Human reviewer
    participant Trusted as Approved corpus (planned Stage 5)

    Analyst->>Review: propose record, claims, and source evidence
    Steward->>Review: propose relationships and disposition evidence
    Note over Analyst,Steward: Neither agent can approve or promote knowledge.
    Review->>Human: present candidate and provenance
    Human->>Review: explicit decision with decision provenance

    alt approved
        Review->>Trusted: make approved material eligible for retrieval
    else not approved
        Review-->>Human: retain a non-trusted review decision
    end
```

## 5. Collaboration map

Mermaid does not provide a native UML communication-diagram notation. This
collaboration map serves the same review purpose: it shows which participant can
exchange which kind of information and makes the human authority boundary
visible.

```mermaid
flowchart TB
    Source[Source submitter] -->|untrusted source and provenance| Intake[Deterministic intake]
    Intake -->|immutable artifact and chunks| Analyst[Intake Analyst]
    Analyst -->|candidate record and evidence| Steward[Knowledge Steward]
    Steward -->|relationship and disposition recommendations| Review[Review package]
    Review -->|decision request| Human[Human reviewer]
    Human -->|explicit approval decision and provenance| Review
    Review -->|approved material only| Corpus[Trusted corpus]

    Intake -. no authority to approve .-> Corpus
    Analyst -. no authority to approve .-> Corpus
    Steward -. no authority to approve .-> Corpus
```

## Design constraints preserved

- Ingested content is data, never an instruction to the system or its agents.
- Source artifacts, knowledge records, and retrieval chunks cannot substitute
  for one another.
- Deterministic code owns parsing, hashing, validation, and state transitions.
- Human approval is an explicit transition; no agent output is trusted by
  default.

## 6. Product stages and competition capability gates

Product delivery stages and course/competition capability gates are related but
not interchangeable. This planning map shows where a product stage is expected
to create evidence for one or more gates. An arrow does **not** mean a gate is
satisfied, and the official competition requirements must be verified before
claiming any gate.

```mermaid
flowchart LR
    subgraph product[Product stages]
        direction TB
        P0[Stage 0: repository foundation]
        P1[Stage 1: deterministic ingestion]
        P2[Stage 2: Intake Analyst]
        P3[Stage 3: Knowledge Steward and human review]
        P4[Stage 4: operational evidence]
        P5[Stage 5: optional retrieval and deployment]
    end

    subgraph gates[Competition or course capability gates]
        direction TB
        Setup[Setup]
        Build[Build]
        Workflow[Workflow]
        Monitor[Monitor]
        Evaluate[Evaluate]
        Deploy[Deploy: separately verified requirements]
    end

    P0 --> Setup
    P1 --> Build
    P2 --> Build
    P3 --> Build
    P3 --> Workflow
    P4 --> Workflow
    P4 --> Monitor
    P4 --> Evaluate
    P5 -. only if deployment is adopted .-> Deploy
```

The immediate next product milestone remains Stage 1. It should demonstrate
deterministic ingestion; it must not be expanded just to check unrelated
competition boxes.
