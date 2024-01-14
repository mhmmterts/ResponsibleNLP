#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

import argparse

from holistic_bias.src.sentences import HolisticBiasSentenceGenerator
DEFAULT_DATASET_VERSION = "v1.1"
# Default to the original v1.0 version for compatibility.

RANDOM_SEED = 17

# Template building constants
NONE_STRING = "(none)"  # Use when an attribute is not present
NO_PREFERENCE_DATA_STRING = "no_data"
# Use when it is not known whether a descriptor is preferred


if __name__ == "__main__":



    print(
        f"Instantiating the HolisticBias sentence generator and saving output files to 'xxx'."
    )
    generator = HolisticBiasSentenceGenerator(
        save_folder='D:\Repos\Github Projects\ResponsibleNLP\holistic_bias\dataset',
        dataset_version=DEFAULT_DATASET_VERSION
    )
    print(f"\nSample sentences:")
    for _ in range(5):
        sentence_with_metadata = generator.get_sentence()
        print("\t" + sentence_with_metadata["text"])
