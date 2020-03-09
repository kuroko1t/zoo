# ZOO

zoo pytorch models

# models

### Image Semantic
* class DeepLab ref:[DeepLabV3](https://github.com/jfzhang95/pytorch-deeplab-xception)

### Object Detection
* class Darknet res:[YOLOv3](https://github.com/eriklindernoren/PyTorch-YOLOv3)

### Face Recognition
* class Facenet res:[facenet](https://github.com/timesler/facenet-pytorch)

### Image Classification

* def resnet18
* def resnet101
* def vgg16
* def densenet161
* def inception

[ref](https://pytorch.org/docs/stable/torchvision/models.html)

# Install

```
git clone https://github.com/kuroko1t/zoo
git submodule init
git submodule update
python setup.py install
```

# Usage

Please refer to each project for details of usage.

```python3
from zoo import Darknet, Facenet, DeepLab
from zoo import resnet18, resnet101, vgg16

yolo_model = Darknet('zoo/models/pytorch_yolov3/config/yolov3-tiny.cfg')
facenet_model = Facenet(pretrained='vggface2').eval()
resnet18_model = resnet18()
```

# LICENSE
MIT
