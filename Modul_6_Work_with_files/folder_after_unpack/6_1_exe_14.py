from pathlib import Path

message = Path('test_binary.bin')
message.write_bytes(b'First line 123')

print(message.read_bytes().decode())