# ZOO

zoo pytorch models

# models

### Image Semantic
* [DeepLabV3](https://github.com/jfzhang95/pytorch-deeplab-xception)

### Object Detection
* [YOLOv3](https://github.com/eriklindernoren/PyTorch-YOLOv3)

### Face Recognition
* [facenet](https://github.com/timesler/facenet-pytorch)

### Image Classification

https://pytorch.org/docs/stable/torchvision/models.html

# Usage

Please refer to each project for details of usage.

```python3
from zoo import Darknet, Facenet, DeepLab
from zoo import resnet18, resnet101, vgg16

yolo_model = Darknet('config')
facenet_model = Facenet(pretrained='vggface2').eval()
resnet18_model = resnet18()
```

# MIT
