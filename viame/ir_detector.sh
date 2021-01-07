 #!/bin/sh

# Setup VIAME Paths (no need to run multiple times if you already ran it)

export VIAME_INSTALL="$(cd "$(dirname ${BASH_SOURCE[0]})" && pwd)/../../../build/install"

source ${VIAME_INSTALL}/setup_viame.sh

# Run pipeline

kwiver runner 2021_pipelines/ir_detector.pipe \
              -s thermal_input:video_filename=ir_list_tif.txt

