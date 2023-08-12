import base64

message = 'Hello world!'
message_bytes = message.encode('utf-8')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('utf-8')

print(f'{message = }',\                 # 'Hello world!'
      f'{message_bytes = }',\           # b'Hello world!''
      f'{base64_bytes = }',\            # b'SGVsbG8gd29ybGQh'
      f'{base64_message = }', sep='\n') # 'SGVsbG8gd29ybGQh'