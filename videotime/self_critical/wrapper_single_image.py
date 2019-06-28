import os
from os import path

import torch
import videotime.self_critical.misc.utils as utils
from six.moves import cPickle
from videotime.self_critical import eval_utils
from videotime.self_critical import models
from videotime.self_critical.singleloader import SingleLoader

dir_path = os.path.dirname(os.path.realpath(__file__))


class Opt:
    batch_size = 10
    seq_per_img = 1
    input_json = 'data/coco.json'
    coco_json = ''
    cnn_model = 'resnet101'
    caption_model = 'show_tell'
    model = path.join(dir_path, '../../.data/a2ia_model.pth')
    infos_path = path.join(dir_path, '../../.data/infos_a2ia.pkl')
    input_encoding_size = 512
    rnn_type = 'lstm'
    rnn_size = 512
    num_layers = 1
    drop_prob_lm = 0.5
    seq_length = 0
    fc_feat_size = 2048
    cnn_model_dir = path.join(dir_path, '../../.data/')


def analyze_image(img_path: str):
    opt = Opt()
    with open(opt.infos_path, 'rb') as f:
        infos = cPickle.load(f, encoding='latin1')
        # Setup the model
    ignore = ["id", "batch_size", "beam_size", "start_from", "language_eval"]
    for k in vars(infos['opt']).keys():
        if k not in ignore:
            if k in vars(opt):
                assert vars(opt)[k] == vars(infos['opt'])[k], k + ' option not consistent'
            else:
                vars(opt).update({k: vars(infos['opt'])[k]})  # copy over options from model

    loader = SingleLoader({'image_path': img_path,
                           'coco_json': opt.coco_json,
                           'batch_size': opt.batch_size,
                           'cnn_model': opt.cnn_model,
                           'cnn_model_dir': opt.cnn_model_dir})

    loader.ix_to_word = infos['vocab']
    crit = utils.LanguageModelCriterion()
    model = models.setup(opt)
    model.load_state_dict(torch.load(opt.model, map_location=lambda storage, loc: storage))
    model.eval()
    # Set sample options
    loss, split_predictions, lang_stats = eval_utils.eval_split(model, crit, loader,
                                                                vars(opt))
    return split_predictions[0]['caption']
