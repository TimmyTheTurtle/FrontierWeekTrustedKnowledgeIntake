import unittest

from contextual_knowledge.models import KnowledgeRecord, KnowledgeRelationship


class ModelImmutabilityTests(unittest.TestCase):
    def test_relationship_entries_are_immutable(self) -> None:
        relationship = KnowledgeRelationship("supports", "record_2", None)
        record = KnowledgeRecord(
            record_id="record_1",
            source_ids=("source_1",),
            title="Title",
            summary="Summary",
            concepts=("c1",),
            candidate_claims=("claim",),
            authority_class="advisory",
            relationships=(relationship,),
            review_state="proposed",
            decision_provenance=None,
        )

        with self.assertRaises(AttributeError):
            record.relationships[0].target_id = "record_3"


if __name__ == "__main__":
    unittest.main()
