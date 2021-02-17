# Kamera JoBBS Pipelines
### Pipelines

#### Dual Stream
1. Dual_Region_Trigger_Otter_C_100mm_0deg.pipe
2. Dual_Region_Trigger_Otter_L_100mm_25deg.pipe
3. Dual_Region_Trigger_Otter_R_100mm_25deg.pipe

(Each pipeline is the same, only difference is the `.h5` transform.  One pipeline per camera configuration.)

**Notable Parameters**:

 - `ir_detector`
     +  `model`: [ir_yolo_tiny_1L64x80](../../models/ir_yolo_tiny_1L64x80/)
     
 - `optical_subregion_selector1`
     + `:max_subregion_count` = 30
     + `:fixed_size` = 512
     + `:threshold` = 0.1 (trigger threshold)
        +  `detector`
            *  `model`: [eo_seals_yolo_tiny_3l_512_1to1bg_nounk](../../models/eo_seals_yolo_tiny_3l_512_1to1bg_nounk/)
            *  `:threshold` = 0.1 (output threshold, only output detections greater than this)
     
 - `optical_subregion_selector2`
     + `:max_subregion_count` = 2
     + `:fixed_size` = 416
     + `:threshold` = 0.1 (trigger threshold)
        +  `detector`
            *  `model`: [eo_pb_yolo_tiny_3l](../../models/eo_pb_yolo_tiny_3l/)
            *  `:threshold` = 0.5 (output threshold, only output detections greater than this)

 - `optical_detector_output`
     + `:nms` = 0.8

