from pathlib import Path

message = Path('test_file_copy.txt')
message.write_text('First line')
message.write_text('Second line')

message.write_text('First line\nSecond line')
print(message.read_text())