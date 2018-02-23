import os

from pathlib import Path

import random

import shutil
names = [name for name in Path('./kaga/nvme0n1/pixabay-scraper/imgs').glob('*')]

PWD = os.environ['PWD']
for i in range(5000):
  style, content = [str(x) for x in random.sample(names, 2)]
  print(style, content)
  out = f'{PWD}/images/{i:09d}_output.jpg'
  to_style = f'{PWD}/images/{i:09d}_style.jpg'
  to_content = f'{PWD}/images/{i:09d}_content.jpg'
  shutil.copy(style, to_style)
  shutil.copy(content, to_content)
  os.system(f'python ../demo.py --content_image_path={content} --style_image_path={style} --output_image_path={out}')  
  print(to_style)
