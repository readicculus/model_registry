 #!/bin/sh

# Setup VIAME Paths (no need to run multiple times if you already ran it)

export VIAME_INSTALL=./../..

source ${VIAME_INSTALL}/setup_viame.sh 

# Run pipeline

kwiver runner ${VIAME_INSTALL}/configs/pipelines/detector_pb_seal_yolo_ir_eo_region_trigger.pipe \
              -s optical_input:video_filename=input_image_list_eo.txt \
	      -s thermal_input:video_filename=input_image_list_ir.txt
