# ZOO

zoo pytorch models

# models

class name list

### Image Semantic
* [DeepLab](https://github.com/jfzhang95/pytorch-deeplab-xception)

### Object Detection
* [Darknet](https://github.com/eriklindernoren/PyTorch-YOLOv3)(YOLOv3)

### Face Recognition
* [Facenet](https://github.com/timesler/facenet-pytorch)

### Image Classification

* [resnet18](https://pytorch.org/docs/stable/torchvision/models.html)
* [resnet101](https://pytorch.org/docs/stable/torchvision/models.html)
* [vgg16](https://pytorch.org/docs/stable/torchvision/models.html)
* [densenet161](https://pytorch.org/docs/stable/torchvision/models.html)
* [inception](https://pytorch.org/docs/stable/torchvision/models.html)


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
