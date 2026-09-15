import unittest

from contextual_knowledge.ids import stable_content_hash, stable_id


class StableIdTests(unittest.TestCase):
    def test_hash_is_order_insensitive_for_dicts(self) -> None:
        # The same logical source metadata must hash the same way even when
        # its dictionary keys were written in a different order.
        left = {"b": 2, "a": 1}
        right = {"a": 1, "b": 2}
        self.assertEqual(stable_content_hash(left), stable_content_hash(right))

    def test_stable_id_is_deterministic(self) -> None:
        # Reprocessing identical input must produce the identical source ID,
        # rather than inventing a new identity for the same source.
        payload = {"origin": "example.md", "captured_at": "2026-09-15T00:00:00Z"}
        self.assertEqual(stable_id("source", payload), stable_id("source", payload))

    def test_stable_id_changes_when_namespace_changes(self) -> None:
        # The namespace keeps identifiers for different entity types separate:
        # the same data cannot be both a source ID and a record ID.
        payload = {"origin": "example.md"}
        self.assertNotEqual(stable_id("source", payload), stable_id("record", payload))

    def test_stable_id_has_expected_format_and_length(self) -> None:
        # A stable ID is intentionally recognizable and compact: its entity
        # type prefix is followed by the first 16 hash characters.
        identifier = stable_id("source", {"origin": "example.md"})
        self.assertTrue(identifier.startswith("source_"))
        self.assertEqual(len(identifier), len("source_") + 16)


if __name__ == "__main__":
    unittest.main()
