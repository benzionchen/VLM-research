# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

# Base data folder
DATASET_DIR = "/Users/raiu/Desktop/Desktop/projects/data/MILS"

# Output dir
OUTPUT_DIR = f"{DATASET_DIR}/outputs"

# Image captioning
IMAGEC_COCO_ANNOTATIONS = f"{DATASET_DIR}/coco/annotations/captions_val2014.json"
IMAGEC_COCO_IMAGES = f"{DATASET_DIR}/coco/val2014_small"
IMAGEC_COCO_SPLITS      = f"{DATASET_DIR}/coco/coco_test_split.json" # replaced karpathy split with 5 sample images

# Video captioning
VIDEOC_MSRVTT_ANNOTATIONS = f"{DATASET_DIR}/msrvtt/test_videodatainfo.json"
VIDEOC_MSRVTT_VIDEOS = f"{DATASET_DIR}/msrvtt/TestVideo"

# Audio captioning
AUDIOC_CLOTHO_ANNOTATIONS = f"{DATASET_DIR}/clotho/clotho_captions_evaluation.csv"
AUDIOC_CLOTHO_FILES = f"{DATASET_DIR}/clotho/wav"

# Checkpoints
VICLIP_CKPT = f"{DATASET_DIR}/checkpoints/ViClip-InternVid-10M-FLT.pth"

# Image generation

# Style transfer