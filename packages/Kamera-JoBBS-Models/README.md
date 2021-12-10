# Polar Ecosystems Program Inflight Kamera Detection Pipelines Documentation

## Installation
Download the `viame-configs` archive from zenodo and copy the contents into Kamera's 
`viame-configs` folder.

## Folder structure
```
Kamera-JoBBS-Models
├── viame-configs/
│   └── pipelines/                          
│       ├── embedded_dual_stream/           # pipelines used by Kamera
│       ├── models/                         # Darknet model files (.cfg, .weights, .names) for each model.
│       ├── transformations/                # .h5 transformation files for JoBSS (you should put your h5 files you want to use here as well)
│       ├── common_*.pipe                   # re-usable "common" pipelines
│       └── JoBBS.config                    # Configuration file for the pipelines see below (JoBBS Global Config)
└── Kamera-JoBBS-Models_RELEASE_NOTES.txt   # Release notes for versions
```

### Available Pipelines
All of the following pipelines can be found in `viame-configs/pipelines/embedded_dual_stream`.

The following pipelines are the ones we used in Kamera for JoBSS and are all the same except that they point to different 
`.h5` transformation files.
```
Dual_Region_Trigger_Otter_C_100mm_0deg.pipe   
Dual_Region_Trigger_Otter_L_100mm_25deg.pipe  
Dual_Region_Trigger_Otter_R_100mm_25deg.pipe  
```

The 'Sync' pipelines do not downsample meaning there is no parallelization going on with the models.  This is not
recommended in flight but may be useful for debugging.
```
Sync_Dual_Region_Trigger_Otter_C_100mm_0deg.pipe
Sync_Dual_Region_Trigger_Otter_L_100mm_25deg.pipe
Sync_Dual_Region_Trigger_Otter_R_100mm_25deg.pipe
```

The following pipelines I added in case there is a need to run IR only, EO Polar Bear, or EO Seal detection pipelines inflight.
```
IR_Hotspot_Detector.pipe
EO_Polar_Bear_Detector.pipe                   
EO_Seal_Detector.pipe
```

### JoBBS Global Config
This config is used to configure the pipeline parameters of all pipelines and can be found in `viame-configs/pipelines/JoBBS.config`
```
config global
   # dual stream subregion configurations
   :trigger_threshold                        0.1
   :seal_max_subregion_count                 100
   :polar_bear_max_subregion_count           2

   # general detector configurations
   :detection_threshold_seal                 0.1
   :detection_threshold_polar_bear           0.8
   :detection_threshold_hotspot              0.1

   # output metadata information
   :eo_seal_model_identifier                 eo_seals_yolo_tiny_3l_512_1to1bg_nounk.cfg
   :eo_polar_bear_model_identifier           eo_pb_yolo_tiny_3l.cfg
   :ir_hotspot_model_identifier              ir_yolo_tiny_1L64x80.cfg
```
