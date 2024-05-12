
import os

for file in os.listdir('.'):
    if file == "all_in_one.py": continue
    os.system("python " + file)