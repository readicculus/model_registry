
@echo off

REM Setup VIAME Paths (no need to set if installed to registry or already set up)

SET VIAME_INSTALL=.\..\..

CALL "%VIAME_INSTALL%\setup_viame.bat"

REM Run Pipeline

kwiver.exe runner "%VIAME_INSTALL%/configs/pipelines/detector_pb_seal_yolo_ir_eo_region_trigger.pipe" ^
                  -s input:video_filename=input_image_list_eo.txt ^
                  -s thermal_input:video_filename=input_image_list_ir.txt

pause