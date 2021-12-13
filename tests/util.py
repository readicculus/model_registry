import configparser
import logging
import os
import shutil
import unittest
import pathlib as pl

TEST_DIR = os.path.dirname(__file__)
PROJECT_ROOT = os.path.dirname(TEST_DIR)
OBJECT_DETECTION_DIR = os.path.join(PROJECT_ROOT, 'packages/VIAME-JoBBS-Models/examples/object_detection')
EXAMPLE_IMAGE_DIR = os.path.join(PROJECT_ROOT, 'packages/VIAME-JoBBS-Models/examples/example_imagery/arctic_seal_example_set1')
VIAME_JOBSS_DIR = os.path.join(PROJECT_ROOT, 'packages/VIAME-JoBBS-Models/')

test_config = os.path.join(TEST_DIR, 'config.ini')
config = configparser.ConfigParser()
config.read(test_config)

logging.basicConfig(format='%(asctime)s [%(levelname)s][%(name)s] - %(message)s', level=logging.DEBUG)
global_logger = logging.getLogger(f'')

def get_sealtk_dir():
    return config['TestConfig'].get('sealtk_setup')

def get_image_list_path(fn):
    return os.path.join(EXAMPLE_IMAGE_DIR, fn)


class TestCaseBase(unittest.TestCase):
    log = None
    temp_dir = os.path.join(TEST_DIR, 'tmp')

    def get_output_fp(self, fn):
        return os.path.join(self.temp_dir, self._testMethodName + '_' + fn)

    def get_kwiver_log_file(self):
        return os.path.join(self.temp_dir, self._testMethodName + '.log')

    def assertIsFile(self, path):
        if not pl.Path(path).resolve().is_file():
            raise AssertionError("File does not exist: %s" % str(path))

    def assertIsDir(self, path):
        if not pl.Path(path).resolve().is_dir():
            raise AssertionError("Directory does not exist: %s" % str(path))


    def print(self, message, loglevel=logging.INFO):
        self.log.log(level=loglevel, msg=message)

    def setUp(self) -> None:
        self.log = logging.getLogger(self.id())
        # if os.path.isdir(self.temp_dir):
        #     shutil.rmtree(self.temp_dir)
        os.makedirs(self.temp_dir, exist_ok=True)

    def tearDown(self) -> None:
        try:
            if self._outcome.success:
                self.print('Test Succeeded', logging.INFO)
                # if os.path.isdir(self.temp_dir):
                #     shutil.rmtree(self.temp_dir)
            else:
                self.print('Test Failed', logging.ERROR)
        except:
            pass


    # @classmethod
    # def setUpClass(cls) -> None:
    #     if os.path.isdir(cls.temp_dir):
    #         shutil.rmtree(cls.temp_dir)
    #
    #     os.makedirs(cls.temp_dir, exist_ok=True)

    @classmethod
    def tearDownClass(cls) -> None:
        if os.path.isdir(cls.temp_dir):
            shutil.rmtree(cls.temp_dir)
