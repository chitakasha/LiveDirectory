import unittest

from core.autogen import golden_ratio_autogen


class TestGoldenRatioAutogen(unittest.TestCase):
    """Tests for the golden ratio autogeneration module."""

    def test_generate_text(self):
        """Tests the generate_text() function."""
        prompts = [
            "What is the meaning of life?",
            "How can we achieve world peace?",
            "What are the principles of quantum mechanics?",
        ]
        current_state = {}
        generated_text = golden_ratio_autogen.generate_text(prompts, current_state)
        self.assertIsNotNone(generated_text)
        self.assertGreater(len(generated_text), 0)


if __name__ == "__main__":
    unittest.main()

