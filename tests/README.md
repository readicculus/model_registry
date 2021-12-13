I've added tests to run the command line VIAME-JoBBS-Model pipelines.

In order to run test must have seal_tk and modify `sealtk_setup` in `tests/config.ini`

I don't think there is a good way to test the embedded pipelines in VIAME or Kamera as inputs require a python
embedded runner which I don't have but one could be made.

Since I had to remove LFS file from the repo, I've added a script `tests/download_test_files.py` to download the example imagery and copy model files to the correct locations
required to run the tests so if you plan to run the tests *first run this script*.

