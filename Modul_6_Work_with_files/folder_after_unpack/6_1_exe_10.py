from pathlib import Path

old_dir = Path('tes!t.txt')
new_dir = Path('temp/tes_t.txt')

old_dir.rename(new_dir)