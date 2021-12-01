import configparser
import logging
import os
import shutil
import unittest
import pathlib as pl

TEST_DIR = os.path.dirname(__file__)
PROJECT_ROOT = os.path.dirname(TEST_DIR)
OBJECT_DETECTION_DIR = os.path.join(PROJECT_ROOT, 'packages/VIAME-JoBBS-Models/examples/object_detection')

test_config = os.path.join(TEST_DIR, 'config.ini')
config = configparser.ConfigParser()
config.read(test_config)

def get_sealtk_dir():
    return config['TestConfig'].get('sealtk_setup')

def get_image_list_path(fn):
    return os.path.join(OBJECT_DETECTION_DIR, fn)

class TestCaseBase(unittest.TestCase):
    log = None
    temp_dir = os.path.join(TEST_DIR, 'tmp')

    def get_output_fp(self, fn):
        return os.path.join(self.temp_dir, fn)

    def assertIsFile(self, path):
        if not pl.Path(path).resolve().is_file():
            raise AssertionError("File does not exist: %s" % str(path))

    def assertIsDir(self, path):
        if not pl.Path(path).resolve().is_dir():
            raise AssertionError("Directory does not exist: %s" % str(path))

    def _setup(self):
        self.log = logging.getLogger(self.id())
        self.print('Test Started', logging.DEBUG)


    # print to test log
    def print(self, message, loglevel=logging.INFO):
        if not self.log:
            self._setup()

        self.log.log(level=loglevel, msg=message)

    def setUp(self) -> None:
        self._setup()

    def tearDown(self) -> None:
        try:
            if self._outcome.success:
                self.print('Test Succeeded', logging.DEBUG)
            else:
                self.print('Test Failed', logging.ERROR)
        except:
            pass

    @classmethod
    def setUpClass(cls) -> None:
        if os.path.isdir(cls.temp_dir):
            shutil.rmtree(cls.temp_dir)

        os.makedirs(cls.temp_dir, exist_ok=True)

    # @classmethod
    # def tearDownClass(cls) -> None:
    #     shutil.rmtree(cls.temp_dir)
