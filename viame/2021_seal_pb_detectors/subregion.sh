 #!/bin/sh

# Setup VIAME Paths (no need to run multiple times if you already ran it)

export VIAME_INSTALL="$(cd "$(dirname ${BASH_SOURCE[0]})" && pwd)/../../../build/install"

source ${VIAME_INSTALL}/setup_viame.sh

# Run pipeline

kwiver runner pipelines/ir_to_eo_subregion_detector.pipe \
              -s optical_input:video_filename=eo_list_tif.txt \
              -s thermal_input:video_filename=ir_list_tif.txt

