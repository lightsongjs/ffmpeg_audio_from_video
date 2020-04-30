
import os
from pathlib import Path
import subprocess


# os.chdir(file_path)
# print(os.getcwd())
files = os.listdir()
print(files)

filename = ''

for file in files:
    if file.endswith('.mkv') or file.endswith('.mp4') or file.endswith('.avi'):
        filename = file

print(f'Filmul este {filename}')

# Diferentierea intre film si extensie
film, extensie = os.path.splitext(filename)
# print(film)
# print(extensie)


subprocess.run(f'ffmpeg -i {filename} -q:a 0 -map a {film}.mp3')


# print(file_path.name)
# print(file_path.suffix)
# os.system(f'ffmpeg -i tangled.mp4 -q:a 0 -map a tangled.mp3
# ')


# cale = Path(folder)
# os.chdir(filename)
# print(os.getcwd())
# print(os.getcwd())
# os.system('cd..')
# print(os.getcwd())
