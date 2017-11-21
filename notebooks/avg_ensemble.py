#!/usr/bin/env python3

import sys
import os
LOCAL_FAST_AI = '/Users/krishnakalyan3/Educational/FastAI/fastai/'
AWS_FAST_AI = '/home/ubuntu/fastai'
sys.path.append(LOCAL_FAST_AI)
from fastai.imports import *
from fastai.conv_learner import *
from fastai.model import *
from fastai.dataset import *
from fastai.sgdr import *
from fastai.plots import *
from sklearn.metrics import accuracy_score


lr = np.array([1e-3, 1e-2, 1e-1])


def get_models(model):
    arch = eval(model)
    lr = lr_dict[model]
    sz = 550
    bs = 64
    tfms = tfms_from_model(arch, bs, aug_tfms=transforms_side_on, max_zoom=1.1)
    data = ImageClassifierData.from_csv(path=PATH, folder='train', csv_fname=label_csv, test_name='test',
                                        bs=bs, tfms=tfms, val_idxs=val_idxs, suffix='.jpg')
    learn = ConvLearner.pretrained(arch, data=data, precompute=True)
    learn.unfreeze()
    learn.fit(lr, 3, cycle_len=1, cycle_mult=2)
    return learn


def train_accuracy(learn, model):
    log_preds, y = learn.TTA()
    y_pred = np.exp(log_preds)
    preds = np.argmax(log_preds, axis=1)
    acc= accuracy_score(y, preds)
    print('{} has {} accuracy'.format(model, learn))
    return acc


def find_lr(model):
    PATH = '/home/ubuntu/kaggle/dogbreeds/'
    label_csv = f'{PATH}labels.csv'
    n = len(list(open(label_csv)))-1
    val_idxs = get_cv_idxs(n)
    arch = eval(model)
    lr = lr_dict[model]
    sz = 550
    bs = 64
    tfms = tfms_from_model(arch, bs, aug_tfms=transforms_side_on, max_zoom=1.1)
    data = ImageClassifierData.from_csv(path=PATH, folder='train', csv_fname=label_csv, test_name='test',
                                        bs=bs, tfms=tfms, val_idxs=val_idxs, suffix='.jpg')
    learn = ConvLearner.pretrained(arch, data=data, precompute=True)
    learn.lr_find()
    learn.sched.plot()
    return learn


if __name__ == '__main__':
    model_dict = ['resnext101_64','inception_4']
    for key, value in enumerate(model_dict):
        model = get_models(value)
        acc = train_accuracy(model, value)
