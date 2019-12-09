from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from .ctdet import CtdetTrainer
from .exdet import ExdetTrainer

train_factory = {
  'exdet': ExdetTrainer,
  'ctdet': CtdetTrainer,
}
