import unittest

from contextual_knowledge.review_state import can_transition, is_terminal_state, requires_human_decision


class ReviewStateTests(unittest.TestCase):
    def test_allows_linear_transition(self) -> None:
        self.assertTrue(can_transition("captured", "parsed"))

    def test_rejects_skip_transition(self) -> None:
        self.assertFalse(can_transition("captured", "approved"))

    def test_terminal_state_detection(self) -> None:
        self.assertTrue(is_terminal_state("approved"))
        self.assertFalse(is_terminal_state("reviewed"))

    def test_human_decision_required_for_terminal_states(self) -> None:
        self.assertTrue(requires_human_decision("approved"))
        self.assertFalse(requires_human_decision("proposed"))


if __name__ == "__main__":
    unittest.main()
