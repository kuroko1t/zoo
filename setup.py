from setuptools import setup, find_packages

def get_packages():
    packages = find_packages()
    packages += ['zoo.models.pytorch_yolov3.utils']
    packages += ['zoo.models.pytorch_yolov3']
    packages += ['zoo.models.facenet_pytorch.models']
    packages += ['zoo.models.facenet_pytorch.models.utils']
    packages += ['zoo.models.pytorch_deeplab']
    packages += ['zoo.models.pytorch_deeplab.utils']
    packages += ['zoo.models.pytorch_deeplab.dataloaders.datasets']
    packages += ['zoo.models.pytorch_deeplab.modeling']
    packages += ['zoo.models.pytorch_deeplab.modeling.sync_batchnorm']
    packages += ['zoo.models.pytorch_deeplab.modeling.backbone']
    return packages

def get_requires():
    requires = ["torch", 'torchvision', 'numpy']
    yolo = ['tqdm', 'matplotlib']
    deep_lab = ['pycocotools']
    requires += yolo
    requires += deep_lab
    return requires

setup(
    name='zoo',
    packages=get_packages(),
    install_requires=get_requires(),
    version='0.1'
)
