#!/Users/khannay/miniconda3/bin/python

import jupyter_to_medium as jtm

jtm.publish('./nbs/00_training.ipynb',
            integration_token=None,
            pub_name="",
            title="Differential Equations as a Pytorch Neural Network Layer",
            tags=["python", "machine learning", "pytorch", "differential equations", "deep learning"],
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome',
            gistify=True,
            gist_threshold=2,
            ) 