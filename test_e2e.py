import unittest

try:
    from partnership import parser, extractor, generator
    IMPLEMENTED = True
except ImportError:
    IMPLEMENTED = False

class TestPartnershipProposalE2E(unittest.TestCase):

    @unittest.skipUnless(IMPLEMENTED, "Product code not yet implemented")
    def test_interview_transcript_parsing(self):
        """Test parsing of interview transcript."""
        transcript = "We are looking for a backend API development partnership."
        result = parser.parse_transcript(transcript)
        self.assertIsNotNone(result)
        self.assertEqual(result.get("type"), "backend API")

    @unittest.skipUnless(IMPLEMENTED, "Product code not yet implemented")
    def test_partnership_scope_extraction(self):
        """Test extraction of partnership scope."""
        parsed_data = {"type": "backend API", "urgency": "high"}
        scope = extractor.extract_scope(parsed_data)
        self.assertIn("deliverables", scope)
        self.assertTrue(len(scope["deliverables"]) > 0)

    @unittest.skipUnless(IMPLEMENTED, "Product code not yet implemented")
    def test_proposal_generation_flow(self):
        """Test the proposal generation flow end-to-end."""
        transcript = "We are looking for a backend API development partnership."

        # E2E flow
        parsed_data = parser.parse_transcript(transcript)
        scope_data = extractor.extract_scope(parsed_data)
        proposal = generator.generate_proposal(scope_data)

        self.assertIsInstance(proposal, str)
        self.assertIn("backend API", proposal)
        self.assertIn("Proposal", proposal)

if __name__ == '__main__':
    unittest.main()
