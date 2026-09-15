import unittest

from contextual_knowledge.review_state import can_transition, is_terminal_state, requires_human_decision


class ReviewStateTests(unittest.TestCase):
    def test_allows_linear_transition(self) -> None:
        # A source may advance one lifecycle step at a time after capture.
        self.assertTrue(can_transition("captured", "parsed"))

    def test_rejects_skip_transition(self) -> None:
        # A source cannot jump directly from capture to trusted approval;
        # parsing, proposal, review, and a human decision must occur first.
        self.assertFalse(can_transition("captured", "approved"))

    def test_terminal_state_detection(self) -> None:
        # Approved is a final disposition, while reviewed still awaits the
        # human's final decision.
        self.assertTrue(is_terminal_state("approved"))
        self.assertFalse(is_terminal_state("reviewed"))

    def test_human_decision_required_for_terminal_states(self) -> None:
        # Entering a final disposition requires human decision evidence;
        # an early candidate state does not.
        self.assertTrue(requires_human_decision("approved"))
        self.assertFalse(requires_human_decision("proposed"))


if __name__ == "__main__":
    unittest.main()
