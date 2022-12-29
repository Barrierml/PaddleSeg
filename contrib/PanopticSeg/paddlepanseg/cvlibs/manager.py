# Copyright (c) 2022 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import paddleseg.cvlibs.manager as manager
from paddleseg.cvlibs.manager import ComponentManager, BACKBONES, TRANSFORMS

# NOTE: Models, datasets, losses, and postprocessors are very different in the 
# panoptic segmentation task, compared with the semantic segmentation task,
# while most of the backbones and transforms can be reused.
MODELS = ComponentManager("models")
DATASETS = ComponentManager("datasets")
LOSSES = ComponentManager("losses")
POSTPROCESSORS = ComponentManager("postprocessors")

# HACK: Patch `paddleseg.cvlibs.manager`
# Since https://github.com/PaddlePaddle/PaddleSeg/pull/2806 PaddleSeg no longer 
# provides API to modify components used by `Config` in an elegant way.
manager.MODELS = MODELS
manager.DATASETS = DATASETS
manager.LOSSES = LOSSES
manager.POSTPROCESSORS = POSTPROCESSORS