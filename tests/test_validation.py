import unittest

from contextual_knowledge.validation import (
    validate_knowledge_record,
    validate_retrieval_chunk,
    validate_source_artifact,
)


class ValidationTests(unittest.TestCase):
    def test_valid_source_artifact_has_no_errors(self) -> None:
        payload = {
            "source_id": "source_1",
            "origin": "notes.md",
            "content_type": "text/markdown",
            "captured_at": "2026-09-15T00:00:00Z",
            "content_hash": "abc",
            "license_note": "open",
            "trust_classification": "untrusted",
            "raw_reference": "data/samples/notes.md",
        }
        self.assertEqual(validate_source_artifact(payload), [])

    def test_missing_source_artifact_field_fails(self) -> None:
        payload = {
            "source_id": "source_1",
        }
        self.assertTrue(validate_source_artifact(payload))

    def test_terminal_knowledge_state_requires_human_evidence(self) -> None:
        payload = {
            "record_id": "record_1",
            "source_ids": ["source_1"],
            "title": "Title",
            "summary": "Summary",
            "concepts": [],
            "candidate_claims": [],
            "authority_class": "advisory",
            "relationships": [],
            "review_state": "approved",
            "decision_provenance": None,
        }
        errors = validate_knowledge_record(payload, from_state="reviewed")
        self.assertIn("human decision evidence required for review_state: approved", errors)

    def test_terminal_knowledge_state_accepts_payload_decision_provenance(self) -> None:
        payload = {
            "record_id": "record_1",
            "source_ids": ["source_1"],
            "title": "Title",
            "summary": "Summary",
            "concepts": [],
            "candidate_claims": [],
            "authority_class": "advisory",
            "relationships": [],
            "review_state": "approved",
            "decision_provenance": "REVIEWED: PR #2",
        }
        self.assertEqual(validate_knowledge_record(payload, from_state="reviewed"), [])

    def test_chunk_invalid_state_fails(self) -> None:
        payload = {
            "chunk_id": "chunk_1",
            "source_id": "source_1",
            "parent_section_id": "h1",
            "content": "text",
            "content_hash": "abc",
            "heading_path": ["h1"],
            "location": "1:1",
            "chunk_type": "paragraph",
            "review_state": "invalid",
        }
        errors = validate_retrieval_chunk(payload)
        self.assertIn("invalid review_state: invalid", errors)

    def test_knowledge_record_invalid_transition_fails(self) -> None:
        payload = {
            "record_id": "record_1",
            "source_ids": ["source_1"],
            "title": "Title",
            "summary": "Summary",
            "concepts": [],
            "candidate_claims": [],
            "authority_class": "advisory",
            "relationships": [],
            "review_state": "approved",
            "decision_provenance": "REVIEWED: PR #2",
        }
        errors = validate_knowledge_record(payload, from_state="captured")
        self.assertIn("invalid transition: captured -> approved", errors)

    def test_knowledge_record_noop_transition_is_allowed(self) -> None:
        payload = {
            "record_id": "record_1",
            "source_ids": ["source_1"],
            "title": "Title",
            "summary": "Summary",
            "concepts": [],
            "candidate_claims": [],
            "authority_class": "advisory",
            "relationships": [],
            "review_state": "reviewed",
            "decision_provenance": None,
        }
        self.assertEqual(validate_knowledge_record(payload, from_state="reviewed"), [])

    def test_terminal_state_explicit_empty_override_fails(self) -> None:
        payload = {
            "record_id": "record_1",
            "source_ids": ["source_1"],
            "title": "Title",
            "summary": "Summary",
            "concepts": [],
            "candidate_claims": [],
            "authority_class": "advisory",
            "relationships": [],
            "review_state": "approved",
            "decision_provenance": "REVIEWED: PR #2",
        }
        errors = validate_knowledge_record(
            payload,
            from_state="reviewed",
            human_decision_evidence="",
        )
        self.assertIn("human decision evidence required for review_state: approved", errors)


if __name__ == "__main__":
    unittest.main()
