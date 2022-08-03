import base64

message = input("Please type a short message to encode: ")
message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')
print("encoded message: ", base64_message)

decoded = base64.b64decode(base64_bytes)
decoded_message = decoded.decode('ascii')
print("decoded message: ", decoded_message)
