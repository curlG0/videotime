import urllib.request
import os
from os import path

dir_path = os.path.dirname(__file__)

urllib.request.urlretrieve("https://drive.google.com/uc?export=download&id=0B7fNdx_jAqhtSmdCNDVOVVdINWs",
                            path.join(dir_path, '../../.data/resnet101.pth'))

urllib.request.urlretrieve("https://drive.google.com/uc?export=download&id=0B7fNdx_jAqhtc2FaYzEwZUVSSW8",
                           path.join(dir_path, '../../.data/a2ia_model.pth'))

urllib.request.urlretrieve("https://drive.google.com/uc?export=download&id=0B7fNdx_jAqhtbzJtM1BVbWpDYkk",
                           path.join(dir_path, "../../.data/infos_a2ia.pkl"))
