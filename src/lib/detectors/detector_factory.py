from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from .exdet import ExdetDetector
from .ctdet import CtdetDetector

detector_factory = {
  'exdet': ExdetDetector,
  'ctdet': CtdetDetector,
}
