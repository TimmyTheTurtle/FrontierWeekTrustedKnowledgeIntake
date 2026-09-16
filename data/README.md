# Test source artifacts

This directory separates immutable raw source artifacts from Markdown fixtures
derived for deterministic-ingestion tests. The fixtures are not the canonical
source and must not replace it.

## Agentic Agile-V

- **Canonical raw artifact:** `sources/agentic-agile-v-2605.20456v1.pdf`
- **Title:** *Agentic Agile-V: From Vibe Coding to Verified Engineering in
  Software and Hardware Development*
- **Author:** Christopher Koch
- **Version:** arXiv:2605.20456v1, submitted May 19, 2026
- **Canonical URL:** <https://arxiv.org/pdf/2605.20456v1>
- **License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- **SHA-256:**
  `21bf735feda38da23fe4d4308d063dfe9cbb2f9b125c1a1b6eeb215c5961c513`
- **Retrieved:** September 15, 2026

The raw PDF is retained unchanged. It is not an input format supported by the
first deterministic-ingestion slice.

### Derived test fixtures

- `samples/agentic-agile-v-overview.md` selects and reformats portions of the
  title, abstract, and introduction as Markdown. Line breaks were normalized;
  no claims were added.
- `samples/agentic-agile-v-contributions.md` selects and reformats the paper's
  stated contributions and central principle as Markdown. The numbered list and
  quotation formatting are test-fixture structure, not new source claims.

Both files are CC BY 4.0 derivatives. Attribute Christopher Koch and link to
the canonical URL and license whenever either fixture is redistributed.

- `samples/agentic-agile-v-paper-components.md` is a compact, CC BY 4.0
  derivative that exercises common research-paper components: front matter,
  author text, abstract, nested sections, a numbered list, bullets, a quote,
  an inline citation, and references.
- `samples/agentic-agile-v-artifact-components.md` is a synthetic companion
  fixture for a Markdown table, image reference, caption, and fenced example.
  It contains no claims from the paper.
