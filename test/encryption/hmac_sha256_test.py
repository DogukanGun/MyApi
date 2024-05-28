from unittest import TestCase
from app.utils.encryption.hmac_sha256 import hmac_sha256

class HmacSha256Test(TestCase):
    def test_encryption_object(self):
        assert 'f4d850b1017eb4e20e0c58443919033c90cc9f4fe889b4d6b4572a4a0ec2d08a' == hmac_sha256("secret-key", "Hello, world!")

