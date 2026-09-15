import unittest

from contextual_knowledge.ids import stable_content_hash, stable_id


class StableIdTests(unittest.TestCase):
    def test_hash_is_order_insensitive_for_dicts(self) -> None:
        left = {"b": 2, "a": 1}
        right = {"a": 1, "b": 2}
        self.assertEqual(stable_content_hash(left), stable_content_hash(right))

    def test_stable_id_is_deterministic(self) -> None:
        payload = {"origin": "example.md", "captured_at": "2026-09-15T00:00:00Z"}
        self.assertEqual(stable_id("source", payload), stable_id("source", payload))

    def test_stable_id_changes_when_namespace_changes(self) -> None:
        payload = {"origin": "example.md"}
        self.assertNotEqual(stable_id("source", payload), stable_id("record", payload))


if __name__ == "__main__":
    unittest.main()
