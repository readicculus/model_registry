# VIAME JoBBS Models
Pipelines for use in desktop applications VIAME, SEAL-TK, or through the command line kwiver pipeline runner.

### JoBBS Global Config
This config is global so changes to the values here will change it in all JoBBS pipelines.  Most pipelines only use a few of these parameters, so for example changing `trigger_threshold` will not effect runs of an ir-only or eo-only detector.

**important**: `transformation_file` is not actually a relative path, I may change this down the road but for now just put the file name of the transform you are using and place that transform `.h5` in `configs/pipelines/transformations/`
```
# file configs/JoBBS.config
config global
   # dual stream subregion configurations
   relativepath transformation_file =        Kotz-2019-Flight5C_gmb.h5
   :trigger_threshold                        0.1
   :seal_max_subregion_count                 30
   :polar_bear_max_subregion_count           2

   # general detector configurations
   :detection_threshold_seal                 0.1
   :detection_threshold_polar_bear           0.5
   :detection_threshold_hotspot              0.1

   # output metadata information
   :version_identifier                       VIAME-JoBBS-Models-v2021.02.23
   :eo_seal_model_identifier                 eo_seals_yolo_tiny_3l_512_1to1bg_nounk.cfg
   :eo_polar_bear_model_identifier           eo_pb_yolo_tiny_3l.cfg
   :ir_hotspot_model_identifier              ir_yolo_tiny_1L64x80.cfg
```


### Seal-TK GUI Pipelines
located in `configs/pipelines/embedded_dual_stream/`  

| Pipeline   |  Description |
| :------------- | :------------- |
| `JoBBS_eo_arctic_seal_yolo_detector.pipe` | Detect seals in full frame EO images by chipping.     |
| `JoBBS_eo_polar_bear_yolo_detector.pipe` | Detect polar bears in full frame EO images by chipping.     |
| `JoBBS_ir_hotspot_yolo_detector.pipe` | Detect hotspots in IR images.     |
| `JoBBS_pb_seal_yolo_ir_eo_region_trigger.pipe` | Detect hotspots in IR images then detect polar bears and seals in subregions of the EO image based on the projected IR detections.     |
| `sync_JoBBS_pb_seal_yolo_ir_eo_region_trigger.pipe` | Synchronous execution version of the previous pipeline.  |
| `JoBBS_seal_yolo_ir_eo_region_trigger.pipe` | Same as the previous one except **only runs seal detector** on the EO subregions.   **Important Note:** If evaluating seal detection results using a trigger pipeline use this pipeline.  Because the polar bear model is still quite poor it will predict some seals with high confidence and the pipeline will output seals with the label polar bear as the confidence was higher than the seal detection. |
| `sync_JoBBS_seal_yolo_ir_eo_region_trigger.pipe` | Synchronous execution version of the seal only trigger pipeline.  |

Notes:  

- If the GUI crashes when loading images it is most likely because the filenames were not in a format it could parse.  In this case you can use the command line through seal-tk or viame.  You can also report this to me or directly to Matt D. to fix in a future release of seal-tk.


### VIAME GUI Pipelines
located in `configs/pipelines/embedded_single_stream/`  

| Pipeline   |  Description |
| :------------- | :------------- |
| `JoBBS_eo_arctic_seal_yolo_detector.pipe` | Detect seals in full frame EO images by chipping.     |
| `JoBBS_eo_polar_bear_yolo_detector.pipe` | Detect polar bears in full frame EO images by chipping.    |
| `JoBBS_ir_hotspot_yolo_detector.pipe` | Detect hotspots in IR images.    |

Notes:  

- VIAME pipelines cannot currently output a detection CSV file, this can only be done once the pipeline is finished running through the GUI.

### Command line Pipelines
located in `configs/pipelines/`, `.sh` and `.bat` files in `examples/object_detection/`

| Pipeline   |  Description |
| :------------- | :------------- |
| `run_eo_arctic_seal_yolo.sh or .bat` | Detect seals in full frame EO images by chipping.     |
| `run_eo_polar_bear_yolo.sh or .bat`  | Detect polar bears in full frame EO images by chipping.     |
| `run_ir_yolo.sh or .bat` | Detect hotspots in IR images.     |
| `run_ir_eo_subregion_trigger.sh or .bat` | Run the trigger pipeline |

Notes:

- Command line pipelines can be run through both viame and seal-tk binaries.
- **Important** - subregion trigger will only work in Seal-TK binaries because the library needed for warping/projections does not come in the VIAME binaries.


**Running command line pipelines:**  
Example imagery is provided in the package so you can test these without changing anything but when you want to run on your own images open the `.bat`(Windows) file or the `.sh`(Linux) file and modify the image list(lists if running trigger).  

For example to run `run_ir_yolo.bat` on your own ir images open this file and change the .txt file name to your own file:
```
kwiver.exe runner "%VIAME_INSTALL%/configs/pipelines/detector_ir_yolo.pipe" ^
                  -s input:video_filename=my_ir_image_list.txt
```

To run `.bat` files on Windows, double click the file.  

To run `.sh` files on Linux open a shell, navigate to `examples/object_detection/` and run:  
`bash run_xxx.sh`

