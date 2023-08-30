# Copyright (c) OpenMMLab. All rights reserved.
from functools import partial

from datasets import load_dataset

from xtuner.dataset import process_hf_dataset
from xtuner.dataset.collate_fns import default_collate_fn
from xtuner.dataset.map_fns import sql_map_fn, template_map_fn_factory
from xtuner.utils import PROMPT_TEMPLATE


def sql_dataset(tokenizer,
                path='b-mc2/sql-create-context',
                max_length=2048,
                remove_unused_columns=True,
                pack_to_max_length=True):
    template_map_fn = template_map_fn_factory(template=PROMPT_TEMPLATE.sql)
    dataset_org = load_dataset(path)
    dataset = process_hf_dataset(
        dataset=dataset_org,
        tokenizer=tokenizer,
        max_length=max_length,
        dataset_map_fn=sql_map_fn,
        template_map_fn=template_map_fn,
        remove_unused_columns=remove_unused_columns,
        shuffle_before_pack=True,
        pack_to_max_length=pack_to_max_length)

    return dataset


def sql_data_collator(return_hf_format=False):
    return partial(default_collate_fn, return_hf_format=return_hf_format)
