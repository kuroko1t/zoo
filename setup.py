from setuptools import setup, find_packages

def get_packages():
    packages = find_packages()
    packages += ['zoo.models.pytorch_yolov3.utils']
    packages += ['zoo.models.facenet_pytorch.models.utils']
    packages += ['zoo.models.pytorch_deeplab.modeling']
    return packages

def get_requires():
    requires = ["torch", 'torchvision', 'numpy']
    yolo = ['tqdm', 'matplotlib']
    requires += yolo
    return requires

setup(
    name='zoo',
    packages=get_packages(),
    install_requires=get_requires(),
    version='0.1'
)
