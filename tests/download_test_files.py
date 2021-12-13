import configparser
import glob
import os
import shutil

import requests

from tests.util import TEST_DIR, VIAME_JOBSS_DIR, PROJECT_ROOT



test_config = os.path.join(TEST_DIR, 'config.ini')
config = configparser.ConfigParser()
config.read(test_config)

def download_example_imagery():
    extract_fn = 'examples.tar.gz'
    if not os.path.isfile(extract_fn):
        response = requests.get(config['TestConfig'].get('example_imagery_url'), stream=True)
        print('Downloading %s' % config['TestConfig'].get('example_imagery_url'))
        if response.status_code == 200:
            with open(extract_fn, 'wb') as f:
                f.write(response.raw.read())

    shutil.unpack_archive(extract_fn, VIAME_JOBSS_DIR)

def copy_model_files():
    model_files = glob.glob(os.path.join(PROJECT_ROOT, 'models/*/model/*'))
    destination_path = os.path.join(PROJECT_ROOT, 'packages/VIAME-JoBBS-Models/configs/pipelines/models/')
    for f in model_files:
        shutil.copy(f, destination_path)
download_example_imagery()
copy_model_files()
