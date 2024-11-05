import os
import base64

# Provided base64-encoded string
provided_base64_string = "47v1npCi7PL4fIynUvRDWrXMSsZUwpTNvBgvsNOmCfpWfVDMMU83vWI7IEeVNq7u3KdssLQHiEfODRFHuSlBRja04OBDVHWPtEM4hvUyQA2TIhvaxi8BMdtcnfH5FUOhn2ti6hYF33PRV+J8znJAI2Cmcw3/DejQIGPmpbPbNZc="

# Decode base64 to get binary data
binary_data = base64.b64decode(provided_base64_string)

# Generate a new random key with the same length
new_random_key = os.urandom(len(binary_data))

# Encode the new key to base64
new_base64_key = base64.b64encode(new_random_key).decode('utf-8')

print(new_base64_key)
