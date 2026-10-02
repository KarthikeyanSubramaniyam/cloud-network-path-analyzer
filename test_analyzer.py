import unittest
from analyzer import analyze

class Cases(unittest.TestCase):
    def test_security_behavior(self):
        self.assertEqual(analyze({"assets":[{"id":"x","public_ip":None}]}), [])
        self.assertEqual(analyze({"assets":[{"id":"x","public_ip":"203.0.113.1","routes":[{"cidr":"0.0.0.0/0","gateway":"nat-x"}],"ingress":[{"cidr":"0.0.0.0/0"}]}]}), [])

if __name__ == "__main__":
    unittest.main()

