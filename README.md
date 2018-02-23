## FastPhotoStyle

### 序
[deep-photo-styletransfer](https://github.com/luanfujun/deep-photo-styletransfer)はMatlabなどが必要でセットアップがかなり面倒で、かつ、手順が複雑でしたが、nvidiaが公開したライブラリのFastPhotoStyleはpythonのみで完結し、nvidia謹製の機能群のみの依存ですむので、Matlab依存よりはマシで簡単でした  

この実装系の優れたところは輪郭や、絵柄などを変化させず、色やコントラストを大きく変化させることに限定されているので、実際のアート領域と相性が良さそうな点があります（すごい）  

幾つかの例を載せつつ、簡単に実行してみたいと思います。  

[公式サイトのUsage](https://github.com/NVIDIA/FastPhotoStyle)を見ながらセットアップしてみてください。ハマリポイントは注意点に書きました  

### nvidiaからのフォークの変更点
- 不完全ながらpython3対応(nvidiaのpythonのモジュールの対応待ち)
- 自動で様々な組み合わせを試すスクリプトを追加

### 注意点
- nvidiaのcuda 9.0以降であること
- python2のライブラリでないとうまく動作しないことがある
- gcc, g++のversionが2018/2時点で5までの対応となっている
- cudaのtensorflowなどで普段参照しないcudaのlibを参照するのでLD_LIBRARY_PATHを確認する必要があるかもしれない  

**adhocな対応で動かす**  
```console
$ sudo rm /usr/bin/g++
$ sudo ln -s /usr/bin/g++-5 /usr/bin/g++
$ sudo rm /usr/bin/gcc
$ sudo ln -s /usr/bin/gcc-5 /usr/bin/gcc
```

### datasourceを集めたら総当りで、FastPhotoStyleを適応する  

このようなスクリプトを書くと早い  
```python
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
```

### Examples
<div align="center">
  <img width="100%" src="https://user-images.githubusercontent.com/4949982/36600303-3c88c564-18f5-11e8-81a6-a2aa74949cc5.png">
</div>
<div align="center">
  <img width="100%" src="https://user-images.githubusercontent.com/4949982/36600316-42e99a0a-18f5-11e8-94ff-8cd82f21b3f4.png">
</div>
<div align="center">
  <img width="100%" src="https://user-images.githubusercontent.com/4949982/36600325-48106310-18f5-11e8-8d21-21c7e6f39814.png">
</div>
<div align="center">
  <img width="100%" src="https://user-images.githubusercontent.com/4949982/36600333-4d8b370c-18f5-11e8-802e-444c981db8b8.png">
</div>
<div align="center">
  <img width="100%" src="https://user-images.githubusercontent.com/4949982/36600344-541f806e-18f5-11e8-9886-a1ed9086ae2b.png">
</div>
<div align="center">
  <img width="100%" src="https://user-images.githubusercontent.com/4949982/36600372-686a0576-18f5-11e8-9c76-341ffa32d06f.png">
</div>
<div align="center">
  <img width="100%" src="https://user-images.githubusercontent.com/4949982/36600379-70778d60-18f5-11e8-879f-65b2258bbeb0.png">
</div>
<div align="center">
  <img width="100%" src="https://user-images.githubusercontent.com/4949982/36600395-793808f8-18f5-11e8-8141-452621f263a9.png">
</div>

PyTorchとcudaだけでStyle Transferができるので便利ですね  

## 余談
約一年前に、DeepPhotoStyleTransferの方を苦労しながらやった感じでして、きれいな絵同士を使うとうまくいことがわかっています  
ただ、面倒な環境依存が多く、運用プロセスまで載せたくなかったのでサーベイで止まっていましたがこれは良さそうですね。 

https://github.com/GINK03/gink03.github.io/blob/master/_posts/posts/2017-04-07-deep-photo-style-transfer.md

### License
Copyright (C) 2018 NVIDIA Corporation.  All rights reserved.
Licensed under the CC BY-NC-SA 4.0 license (https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode).

### About

This code repository contains an implementation of our fast photorealistic style transfer algorithm. Given a content photo and a style photo, the code can transfer the style of the style photo to the content photo. The details of the algorithm behind the code is documented in our arxiv paper. Please cite the paper if this code repository is used in your publications.

[Yijun Li](https://sites.google.com/site/yijunlimaverick/), [Ming-Yu Liu](http://mingyuliu.net/), [Xueting Li](https://sunshineatnoon.github.io/), [Ming-Hsuan Yang](http://faculty.ucmerced.edu/mhyang/), [Jan Kautz](http://jankautz.com/) "[A Closed-form Solution to Photorealistic Image Stylization](https://arxiv.org/abs/1802.06474)" arXiv preprint arXiv:1802.06474

![](teaser.png)



### Code usage

Please check out the [user manual page](USAGE.md).



