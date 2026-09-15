import unittest

from contextual_knowledge.models import KnowledgeRecord, KnowledgeRelationship


class ModelImmutabilityTests(unittest.TestCase):
    def test_relationship_entries_are_immutable(self) -> None:
        # This relationship is one possible graph edge. Because it lives inside
        # record_1, its source is implicit: record_1 --supports--> record_2.
        # Stage 0 does not yet build a graph-wide record dictionary, index, or
        # traversal API; it only protects the value object that a later graph
        # layer can use.
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

        # Changing an existing edge would silently rewrite derived knowledge.
        # The model is frozen, so a change must instead create a deliberate new
        # record/relationship value with its own review and provenance context.
        with self.assertRaises(AttributeError):
            record.relationships[0].target_id = "record_3"


if __name__ == "__main__":
    unittest.main()
