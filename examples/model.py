from zoo import Facenet, Darknet, DeepLab
from zoo import resnet18, resnet101, vgg16

facenet_model = Facenet(pretrained='vggface2')
yolo_model = Darknet('zoo/models/pytorch_yolov3/config/yolov3-tiny.cfg')
deeplab_model = DeepLab()
resnet_model = resnet18()


