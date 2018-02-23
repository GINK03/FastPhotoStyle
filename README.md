## FastPhotoStyle

### 序
deep-photo-styletransferはMatlabなどが必要でセットアップがかなり面倒で、かつ、手順が複雑でしたが、nvidiaが公開したライブラリのFastPhotoStyleはpythonのみで完結し、nvidia謹製の機能群のみの依存ですむので、Matlab依存よりはマシで簡単でした。  

幾つかの例を載せつつ、簡単に実行してみたいと思います。  

### nvidiaからのフォークの変更点
- 不完全ながらpython3対応(nvidiaのpythonのモジュールの対応待ち)
- 自動で様々な組み合わせを試すスクリプトを追加

### 注意点
- nvidiaのcuda 9.0以降であること
- python2のライブラリでないとうまく動作しないことがある


### License
Copyright (C) 2018 NVIDIA Corporation.  All rights reserved.
Licensed under the CC BY-NC-SA 4.0 license (https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode).

### About

This code repository contains an implementation of our fast photorealistic style transfer algorithm. Given a content photo and a style photo, the code can transfer the style of the style photo to the content photo. The details of the algorithm behind the code is documented in our arxiv paper. Please cite the paper if this code repository is used in your publications.

[Yijun Li](https://sites.google.com/site/yijunlimaverick/), [Ming-Yu Liu](http://mingyuliu.net/), [Xueting Li](https://sunshineatnoon.github.io/), [Ming-Hsuan Yang](http://faculty.ucmerced.edu/mhyang/), [Jan Kautz](http://jankautz.com/) "[A Closed-form Solution to Photorealistic Image Stylization](https://arxiv.org/abs/1802.06474)" arXiv preprint arXiv:1802.06474

![](teaser.png)



### Code usage

Please check out the [user manual page](USAGE.md).



