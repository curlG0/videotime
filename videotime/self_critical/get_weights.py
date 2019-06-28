import urllib.request
import os
from os import path

dir_path = os.path.dirname(__file__)


data_dir = path.join(dir_path, '../../.data')

os.mkdir(data_dir)

urllib.request.urlretrieve("https://drive.google.com/uc?export=download&id=0B7fNdx_jAqhtSmdCNDVOVVdINWs",
                            path.join(data_dir, 'resnet101.pth'))

urllib.request.urlretrieve("https://drive.google.com/uc?export=download&id=0B7fNdx_jAqhtc2FaYzEwZUVSSW8",
                           path.join(data_dir, 'a2ia_model.pth'))

urllib.request.urlretrieve("https://drive.google.com/uc?export=download&id=0B7fNdx_jAqhtbzJtM1BVbWpDYkk",
                           path.join(data_dir, "infos_a2ia.pkl"))
