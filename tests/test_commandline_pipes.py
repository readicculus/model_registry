import os

from subprocess_runner import KwiverRunner
from util import PROJECT_ROOT, get_sealtk_dir, get_image_list_path, TestCaseBase, OBJECT_DETECTION_DIR


# check if two image lists match
def check_image_lists_match(input_image_list, output_image_list):
    with open(input_image_list, 'r') as f:
        inputs = [os.path.basename(line.strip()) for line in f.readlines()]
    with open(output_image_list, 'r') as f:
        outputs = [os.path.basename(line.strip()) for line in f.readlines()]

    for i in inputs:
        if i not in outputs:
            return False
    return True


class TestCommandLineDetectors(TestCaseBase):
    def test_eo_arctic_seal_yolo_pipe(self):
        images_fp = self.get_output_fp('output_images.txt')
        detections_fp = self.get_output_fp('output_detections.txt')
        log_fp = self.get_kwiver_log_file()
        pipe_fp = os.path.abspath(os.path.join(PROJECT_ROOT,
                                               "packages/VIAME-JoBBS-Models/configs/pipelines/detector_eo_arctic_seal_yolo.pipe"))
        kwr = KwiverRunner(
            pipe_fp,
            {},
            OBJECT_DETECTION_DIR,
            get_sealtk_dir(),
            pipe_args={
                'input:video_filename': get_image_list_path('Optical_Image_List.txt'),
                'detector_writer:frame_list_output': images_fp,
                'detector_writer:file_name': detections_fp,
            }
        )
        with open(log_fp, 'w') as f:
            t = kwr.run(f, f)
        t.wait(60)
        self.assertEqual(t.returncode, 0)

        image_lists_match = check_image_lists_match(get_image_list_path('Optical_Image_List.txt'), images_fp)
        self.assertTrue(image_lists_match)

    def test_eo_polar_bear_yolo_pipe(self):
        images_fp = self.get_output_fp('output_images.txt')
        detections_fp = self.get_output_fp('output_detections.txt')
        log_fp = self.get_kwiver_log_file()
        pipe_fp = os.path.abspath(os.path.join(PROJECT_ROOT,
                                               "packages/VIAME-JoBBS-Models/configs/pipelines/detector_eo_polar_bear_yolo.pipe"))
        kwr = KwiverRunner(
            pipe_fp,
            {},
            OBJECT_DETECTION_DIR,
            get_sealtk_dir(),
            pipe_args={
                'input:video_filename': get_image_list_path('Optical_Image_List.txt'),
                'detector_writer:frame_list_output': images_fp,
                'detector_writer:file_name': detections_fp,
            }
        )
        with open(log_fp, 'w') as f:
            t = kwr.run(f, f)
        t.wait(60)
        self.assertEqual(t.returncode, 0)

        image_lists_match = check_image_lists_match(get_image_list_path('Optical_Image_List.txt'), images_fp)
        self.assertTrue(image_lists_match)

    def test_ir_hotspot_pipe(self):
        images_fp = self.get_output_fp('output_images.txt')
        detections_fp = self.get_output_fp('output_detections.txt')
        log_fp = self.get_kwiver_log_file()
        pipe_fp = os.path.abspath(os.path.join(PROJECT_ROOT,
                                               "packages/VIAME-JoBBS-Models/configs/pipelines/detector_ir_yolo.pipe"))
        kwr = KwiverRunner(
            pipe_fp,
            {},
            OBJECT_DETECTION_DIR,
            get_sealtk_dir(),
            pipe_args={
                'input:video_filename': get_image_list_path('Thermal_Image_List.txt'),
                'detector_writer:frame_list_output': images_fp,
                'detector_writer:file_name': detections_fp,
            }
        )
        with open(log_fp, 'w') as f:
            t = kwr.run(f, f)
        t.wait(60)
        self.assertEqual(t.returncode, 0)

        image_lists_match = check_image_lists_match(get_image_list_path('Thermal_Image_List.txt'), images_fp)
        self.assertTrue(image_lists_match)

    def test_pb_seal_yolo_ir_eo_region_trigger_pipe(self):
        images_fp_eo = self.get_output_fp('output_images_eo.txt')
        detections_fp_eo = self.get_output_fp('output_detections_eo.txt')
        images_fp_ir = self.get_output_fp('output_images_ir.txt')
        detections_fp_ir = self.get_output_fp('output_detections_ir.txt')

        log_fp = self.get_kwiver_log_file()
        pipe_fp = os.path.abspath(os.path.join(PROJECT_ROOT,
                                               "packages/VIAME-JoBBS-Models/configs/pipelines/detector_pb_seal_yolo_ir_eo_region_trigger.pipe"))
        transform_fp = os.path.abspath(os.path.join(PROJECT_ROOT,
                                                    'packages/VIAME-JoBBS-Models/configs/pipelines/transformations/A90_RGB-IR_C_100mm_0deg_20190509-10_fl5-6.h5'))
        kwr = KwiverRunner(
            pipe_fp,
            {},
            OBJECT_DETECTION_DIR,
            get_sealtk_dir(),
            pipe_args={
                'optical_input:video_filename': get_image_list_path('Optical_Image_List.txt'),
                'thermal_input:video_filename': get_image_list_path('Thermal_Image_List.txt'),
                'thermal_writer_csv:frame_list_output': images_fp_ir,
                'thermal_writer_csv:file_name': detections_fp_ir,
                'optical_writer_csv:frame_list_output': images_fp_eo,
                'optical_writer_csv:file_name': detections_fp_eo,
                'warp_ir_detections_to_eo:transformation_file': transform_fp
            }
        )
        with open(log_fp, 'w') as f:
            t = kwr.run(f, f)
        t.wait(60)
        self.assertEqual(t.returncode, 0)

        eo_image_lists_match = check_image_lists_match(get_image_list_path('Optical_Image_List.txt'), images_fp_eo)
        self.assertTrue(eo_image_lists_match)

        ir_image_lists_match = check_image_lists_match(get_image_list_path('Thermal_Image_List.txt'), images_fp_ir)
        self.assertTrue(ir_image_lists_match)
