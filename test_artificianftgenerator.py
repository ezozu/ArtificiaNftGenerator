# test_artificianftgenerator.py
"""
Tests for ArtificiaNftGenerator module.
"""

import unittest
from artificianftgenerator import ArtificiaNftGenerator

class TestArtificiaNftGenerator(unittest.TestCase):
    """Test cases for ArtificiaNftGenerator class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ArtificiaNftGenerator()
        self.assertIsInstance(instance, ArtificiaNftGenerator)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ArtificiaNftGenerator()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
