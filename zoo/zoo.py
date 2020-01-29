import sys, os

# import facenet
facenet_path = 'models/facenet_pytorch'
sys.path.append(os.path.join(os.path.dirname(__file__), facenet_path))
from zoo.models.facenet_pytorch.models.inception_resnet_v1 import InceptionResnetV1
from zoo.models.facenet_pytorch.models.mtcnn import MTCNN as TorchMTCNN
sys.path.remove(os.path.join(os.path.dirname(__file__), facenet_path))

# import yolo
yolo_path = 'models/pytorch_yolov3'
sys.path.append(os.path.join(os.path.dirname(__file__), yolo_path))
from zoo.models.pytorch_yolov3.models import Darknet as darknet
sys.path.remove(os.path.join(os.path.dirname(__file__), yolo_path))

# import deeplab
deeplab_path = 'models/pytorch_deeplab'
sys.path.append(os.path.join(os.path.dirname(__file__), deeplab_path))
from zoo.models.pytorch_deeplab.modeling.deeplab import DeepLab as TorchDeeplab
sys.path.remove(os.path.join(os.path.dirname(__file__), deeplab_path))

import torchvision.models as torch_models

class Facenet(InceptionResnetV1):
    def __init__(self, pretrained=None, classify=False, num_classes=None, dropout_prob=0.6, device=None):
        super(Facenet, self).__init__(pretrained, classify, num_classes, dropout_prob, device)

class MTCNN(TorchMTCNN):
    def __init__(self, image_size=160, margin=0, min_face_size=20,
                 thresholds=[0.6, 0.7, 0.7], factor=0.709, post_process=True,
                 select_largest=True, keep_all=False, device=None):
        super(MTCNN, self).__init__(image_size, margin, min_face_size,
                                    thresholds, factor, post_process,
                                    select_largest, keep_all, device)
        
class Darknet(darknet):
    def __init__(self, config_path, img_size=416):
        super(darknet, self).__init__(config_path, img_size)
                
### DeepLab ###
class DeepLab(TorchDeeplab):
    def __init__(self, backbone='resnet', output_stride=16, num_classes=21,
                 sync_bn=True, freeze_bn=False):
        super(DeepLab, self).__init__(backbone, output_stride, num_classes,
                                      sync_bn, freeze_bn)

def resnet18(pretrained=False, progress=True, **kwargs):
    return torch_models.resnet18(pretrained, progress, **kwargs)

def resnet101(pretrained=False, progress=True, **kwargs):
    return torch_models.resnet101(pretrained, progress, **kwargs)

def vgg16(pretrained=False, progress=True, **kwargs):
    return torch_models.vgg16(pretrained, progress, **kwargs)
