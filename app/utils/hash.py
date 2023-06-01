import hashlib

class Hash:
    def __init__(self):
        pass

    @staticmethod
    def hash_string(string):
        # Create a SHA-256 hash object
        sha256_hash = hashlib.sha256()

        # Convert the string to bytes and update the hash object
        sha256_hash.update(string.encode('utf-8'))

        # Get the hashed value as a hexadecimal string
        hashed_string = sha256_hash.hexdigest()

        return hashed_string
