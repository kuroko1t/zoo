#from PIL import Image
#from zoo import Facenet, MTCNN
#from torchvision import transforms
#from torchvision import datasets
#from torch.utils.data import DataLoader
# 
#import torch
# 
#dataset = datasets.ImageFolder('facenet-pytorch/data/test_images/')
# 
#dataset.idx_to_class = {i:c for c, i in dataset.class_to_idx.items()}
#loader = DataLoader(dataset, collate_fn=collate_fn, num_workers=workers)
# 
#facenet = Facenet(pretrained='casia-webface').eval()
#embeddings = facenet(img)
#dists = [[(e1 - e2).norm().item() for e2 in embeddings] for e1 in embeddings]
#print(dists)

