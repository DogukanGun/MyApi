import hashlib
import hmac


def hmac_sha256(key, message):
    """
    Generate a HMAC SHA256 hash of the message using the provided key.

    :param key: The secret key for the HMAC algorithm
    :param message: The message to be hashed
    :return: Hexadecimal string of the HMAC SHA256 hash
    """
    # Encode the key and message to bytes if they are not already
    if isinstance(key, str):
        key = key.encode()
    if isinstance(message, str):
        message = message.encode()

    # Create a new HMAC object using the key and SHA256 hash algorithm
    hmac_obj = hmac.new(key, message, hashlib.sha256)

    # Return the HMAC object's hexadecimal digest
    return hmac_obj.hexdigest()

