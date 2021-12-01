import os

from subprocess_runner import  KwiverRunner
from util import PROJECT_ROOT, get_sealtk_dir, get_image_list_path, TestCaseBase, OBJECT_DETECTION_DIR


class TestCommandLineDetectors(TestCaseBase):
    def test_eo_arctic_seal_yolo_pipe(self):
        images_fp = self.get_output_fp('output_images.txt')
        detections_fp = self.get_output_fp('output_detections.txt')
        log_fp = self.get_output_fp('log.txt')
        pipe_fp = os.path.abspath(os.path.join(PROJECT_ROOT,
                                               "packages/VIAME-JoBBS-Models/configs/pipelines/detector_eo_arctic_seal_yolo.pipe"))
        kwr = KwiverRunner(
                    pipe_fp,
                    {},
                    OBJECT_DETECTION_DIR,
                    get_sealtk_dir(),
                    pipe_args={
                        'input:video_filename': get_image_list_path('input_image_list_eo.txt'),
                        'detector_writer:frame_list_output': images_fp,
                        'detector_writer:file_name': detections_fp,
                    }
                )
        with open(log_fp, 'w') as f:
            t = kwr.run(f, f)
        t.wait(60)
        self.assertEqual(t.returncode, 0)

    def test_eo_polar_bear_yolo_pipe(self):
        images_fp = self.get_output_fp('output_images.txt')
        detections_fp = self.get_output_fp('output_detections.txt')
        log_fp = self.get_output_fp('log.txt')
        pipe_fp = os.path.abspath(os.path.join(PROJECT_ROOT,
                                               "packages/VIAME-JoBBS-Models/configs/pipelines/detector_eo_polar_bear_yolo.pipe"))
        kwr = KwiverRunner(
            pipe_fp,
            {},
            OBJECT_DETECTION_DIR,
            get_sealtk_dir(),
            pipe_args={
                'input:video_filename': get_image_list_path('input_image_list_eo.txt'),
                'detector_writer:frame_list_output': images_fp,
                'detector_writer:file_name': detections_fp,
            }
        )
        with open(log_fp, 'w') as f:
            t = kwr.run(f, f)
        t.wait(60)
        self.assertEqual(t.returncode, 0)

    def test_ir_hotspot_pipe(self):
        images_fp = self.get_output_fp('output_images.txt')
        detections_fp = self.get_output_fp('output_detections.txt')
        log_fp = self.get_output_fp('log.txt')
        pipe_fp = os.path.abspath(os.path.join(PROJECT_ROOT,
                                               "packages/VIAME-JoBBS-Models/configs/pipelines/detector_ir_yolo.pipe"))
        kwr = KwiverRunner(
            pipe_fp,
            {},
            OBJECT_DETECTION_DIR,
            get_sealtk_dir(),
            pipe_args={
                'input:video_filename': get_image_list_path('input_image_list_ir.txt'),
                'detector_writer:frame_list_output': images_fp,
                'detector_writer:file_name': detections_fp,
            }
        )
        with open(log_fp, 'w') as f:
            t = kwr.run(f, f)
        t.wait(60)
        self.assertEqual(t.returncode, 0)

    def test_pb_seal_yolo_ir_eo_region_trigger_pipe(self):
        images_fp_eo = self.get_output_fp('output_images_eo.txt')
        detections_fp_eo = self.get_output_fp('output_detections_eo.txt')
        images_fp_ir = self.get_output_fp('output_images_ir.txt')
        detections_fp_ir = self.get_output_fp('output_detections_ir.txt')

        log_fp = self.get_output_fp('log.txt')
        pipe_fp = os.path.abspath(os.path.join(PROJECT_ROOT,
                                               "packages/VIAME-JoBBS-Models/configs/pipelines/detector_pb_seal_yolo_ir_eo_region_trigger.pipe"))
        kwr = KwiverRunner(
            pipe_fp,
            {},
            OBJECT_DETECTION_DIR,
            get_sealtk_dir(),
            pipe_args={
                'optical_input:video_filename': get_image_list_path('input_image_list_eo.txt'),
                'thermal_input:video_filename': get_image_list_path('input_image_list_ir.txt'),
                'thermal_writer_csv:frame_list_output': images_fp_ir,
                'thermal_writer_csv:file_name': detections_fp_ir,
                'optical_writer_csv:frame_list_output': images_fp_eo,
                'optical_writer_csv:file_name': detections_fp_eo
            }
        )
        with open(log_fp, 'w') as f:
            t = kwr.run(f, f)
        t.wait(60)
        self.assertEqual(t.returncode, 0)
