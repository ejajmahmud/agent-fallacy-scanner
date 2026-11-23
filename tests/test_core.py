"""Tests for FallacyScanner."""
import unittest
from agent_fallacy_scanner.core import FallacyScanner

class TestFallacyScanner(unittest.TestCase):
    def test_detection(self):
        text = "You are either with us or against us in this vote."
        matches = FallacyScanner.scan(text)
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0].fallacy_type, "false_dilemma")
