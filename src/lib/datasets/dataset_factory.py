from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from .sample.exdet import EXDetDataset
from .sample.ctdet import CTDetDataset

from .dataset.coco import COCO
from .dataset.pascal import PascalVOC
from .dataset.XinTong import XinTong

dataset_factory = {
  'coco': COCO,
  'pascal': PascalVOC,
  'XinTong': XinTong
}

_sample_factory = {
  'exdet': EXDetDataset,
  'ctdet': CTDetDataset,
}


def get_dataset(dataset, task):
  class Dataset(dataset_factory[dataset], _sample_factory[task]):
    pass
  return Dataset
  
