# Full-Markdown structure discovery report

**Status:** exploratory, non-authoritative design evidence
**Date:** 2026-09-16
**Scope:** LLM-assisted inspection of two full Markdown extracts. This is not a parser specification, an evaluation result, or a promotion of source claims to trusted knowledge.

## Purpose and boundary

This discovery exercise asks a downstream question: given a Markdown document, which source structures should a future deterministic Markdown reader preserve and represent? It does not decide how PDFs are converted into Markdown. The source text was treated as untrusted data throughout; no instruction or claim inside either paper was acted upon.

The report separates direct observations from candidate follow-up work. A human must decide whether a candidate becomes a requirement, a model change, or a deterministic test.

## Corpus and reproducibility anchors

| Document | Immutable PDF SHA-256 | Full-extract Markdown SHA-256 | Current parser result |
| --- | --- | --- | --- |
| `agentic-agile-v-2605.20456v1` | `21bf735feda38da23fe4d4308d063dfe9cbb2f9b125c1a1b6eeb215c5961c513` | `48eeb553b7450f6fa0fc1a83594ae37a3dc0344eafc1afdd11562d8c9eb3c013` | 7 page chunks; repeatable and schema-valid |
| `agile-v-2602.20684v1` | `232a601ae097250ebf5781ba8399ce557690e2df1b75d2be807b68d0ac8b8dd1` | `12b2df8a06a43b889d1e9e1e72b519e93646cc27b6e41a90dcbac4130efb5338` | 9 page chunks; repeatable and schema-valid |

The extracts retain `# Extracted page N` anchors. Those are added Markdown provenance anchors; apart from those anchors, the body text is `pypdf` per-page extraction. See `data/README.md` for the extraction boundary.

## Method

1. Run the current deterministic parser over each full extract and record its chunks, locations, repeatability, and schema validation.
2. Have an LLM inspect the Markdown as untrusted content for structural phenomena that are preserved, flattened, ambiguous, or absent from the current representation.
3. Cite concrete extract locations for every discovery observation.
4. Record findings as candidates only. The LLM output is intentionally non-deterministic and is not itself an acceptance criterion.

The interactive discovery run did not use a dedicated evaluation runner, so no model-version or verbatim prompt record exists. The corpus hashes above, this report's scope, and the raw extracts are the available evidence. Any later repeatable evaluation should capture prompt, model/version, parameters, raw response, and human disposition separately.

## Deterministic baseline

The current parser recognizes only ATX headings outside fenced code. Therefore, the added page anchors are the only recognized headings in either extract. Their source-native headings, such as `I. INTRODUCTION`, `A. ...`, `TABLE I`, and `REFERENCES`, remain content inside the page chunks.

| Behavior | Agentic Agile-V | Agile-V |
| --- | ---: | ---: |
| Full-extract pages | 7 | 9 |
| Output chunks | 7 | 9 |
| Structural heading paths | `Extracted page 1` through `Extracted page 7` | `Extracted page 1` through `Extracted page 9` |
| Stable repeated ingestion | yes | yes |
| Current source/chunk schema validation | yes | yes |

This is correct for the narrow implementation: it preserves content and gives page-level provenance. It does not yet model the document's native structure.

## LLM-assisted discovery observations

### 1. Section hierarchy is present but opaque

Both documents contain Roman-numeral top-level headings and lettered subsections. Examples include Agentic Agile-V `I. INTRODUCTION` at line 41, `II. BACKGROUND ANDEVIDENCEBASE` at line 108, and `V. THEAGENTICAGILE-V FRAMEWORK` at line 281. Agile-V contains `II. RELATEDWORK` at line 105 and `III. THEAGILEV FRAMEWORK` at line 176.

**Candidate:** conservatively represent heading-like syntax and hierarchy without mistaking arbitrary prose for a heading. Retain the original line even when classification is uncertain.

### 2. Lists are neither Markdown lists nor plain paragraphs

The extracts use Unicode bullet glyphs and inline formatting remnants, for example Agentic Agile-V lines 241-245 and 479-485, and Agile-V lines 422-427. Numbered procedural steps also appear inside section body text.

**Candidate:** tolerate source forms beyond `-`, `*`, and `1.` while preserving source order, nesting ambiguity, and parent context.

### 3. Tables carry evidence but have lost native cell boundaries

Agentic Agile-V contains `TABLE I` at line 417 and `TABLE II` at line 444. Agile-V contains `TABLE I` at line 385, then Tables II-V at lines 442, 503, 532, and 619. Their rows appear as successive text lines rather than native Markdown table syntax.

**Candidate:** retain a typed `table_candidate` block containing raw lines and confidence/provenance, instead of fabricating row and cell boundaries. Keep the label, caption, and following body associated.

### 4. Figures survive only as nearby labels and captions

Agentic Agile-V has `Fig. 1. High-level Agentic Agile-V model.` at line 271. Agile-V has figure captions at lines 212 and 299. The diagrams themselves are not in the Markdown text.

**Candidate:** represent a figure reference or caption only when it is present; never invent visual content. Preserve its relation to adjacent prose and any available Markdown asset link.

### 5. Citations and bibliography are separate structural regions

Inline bracketed citations occur throughout both documents, while their reference sections begin at Agentic Agile-V line 584 and Agile-V line 756.

**Candidate:** preserve citation markers, bibliography entries, and unresolved status. Any citation resolution should be a later deterministic process, not an LLM inference.

### 6. Cross-page continuity conflicts with page-only chunking

The parser currently emits a page as a chunk. Native sections cross those boundaries, so current chunks can divide a single semantic unit. The observed tables are page-local; this corpus does not demonstrate a table crossing a page anchor. Locations are derived-Markdown line ranges, not native section identities.

**Candidate:** drive future chunks from recognized source structure, retaining page anchors as secondary provenance. Associate multi-page continuation without joining unrelated neighboring material.

### 7. Extraction artifacts need a non-destructive posture

Examples include concatenated heading words such as `RELATEDWORK` (Agile-V line 105), `THEAGILEV` (line 176), and `ANDEVIDENCEBASE` (Agentic Agile-V line 108), plus symbols such as `≈`, `≤`, and `→`.

**Candidate:** preserve raw content and never silently repair it. Emit reviewable extraction-quality observations, with evidence, when patterns suggest collapsed spacing, line-wrap hyphenation, or another ambiguity.

### 8. Document roles are visible but untyped

The extracts expose title/author material, abstracts, body sections, tables, figures, references, and appendix-like procedural material, but the current `RetrievalChunk` emits only `chunk_type="section"`.

**Candidate:** typed, still-untrusted block roles are a more useful direction than treating every heading body as the same kind of section.

## Candidate deterministic follow-up cases

These are proposed test cases, not approved work:

1. Recognize a documented heading grammar while retaining unrecognized heading-like lines as content.
2. Preserve Unicode-bullet and ordered-list blocks as source-faithful units.
3. Detect table labels/captions and retain their raw body as an ordered table candidate without fabricating cells.
4. Preserve figure labels/captions and associate a Markdown image/link when supplied; report a caption-only figure honestly.
5. Preserve inline citation markers and bibliography entries without resolving them at parse time.
6. Test a section that spans page anchors. Add a separate table-spanning-page test only after a source or synthetic fixture demonstrates that case.
7. Emit deterministic extraction-quality findings for selected, documented patterns, never an automatic text repair.
8. Verify that all derived blocks retain original Markdown ranges, heading context where known, source ID, and content hash.

## Non-goals and human decisions still needed

- This report does not choose a heading grammar or a table-reconstruction algorithm.
- It does not change the current parser or data model.
- It does not make a claim about the factual correctness of either paper.
- It does not decide whether all candidate block roles belong in Stage 1.
- A human must prioritize the candidates and approve any resulting patch.

## Suggested next smallest action

Review this report and choose one narrowly bounded structure family for the next deterministic parser increment. Heading hierarchy plus list preservation is the smallest coherent starting point; tables, figures, citations, and extraction-quality diagnostics can remain separate follow-on decisions.
