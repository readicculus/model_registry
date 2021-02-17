# eo_seals_yolo_tiny_3l_512_1to1bg_nounk

| Model Info    |  |
| ------------- | ------------- |
| Input Size    | 512x512       |
| Classes       | Ringed Seal, Bearded Seal    |
| Detection layers       | P<sub>5</sub>/32, P<sub>4</sub>/16, P<sub>3</sub>/8    |
| Epochs       | ~60,000   |
| Repo | AlexyAB/darknet b5ff7f4 |
| Initialization       | yolov3-tiny.conv.15   |
| Training Net       | [eo_seals_yolo_tiny_3l_512_1to1bg_nounk_TRAIN.cfg](model/eo_seals_yolo_tiny_3l_512_1to1bg_nounk_TRAIN.cfg)  |
| Inference Net       | [eo_seals_yolo_tiny_3l_512_1to1bg_nounk.cfg](model/eo_seals_yolo_tiny_3l_512_1to1bg_nounk.cfg)  |

Notes: The reason we have a train net and an inference net is so that model is compatible with pjreddie's darknet.  Class distribution scaling and other training-time improvements were used that are not compatible with the older darknet network parser.

| Dataset Info    |  |
| ------------- | ------------- |
| Background Ratio Train | ~1:1     |
| Background Ratio Test | ~1:1     |

**Benchmark speed (1080ti,batch_size=1):**


| Results @ .25 IOU, Thresh = .25    | Ringed Seal | Bearded Seal  | Combined |
| ------------- | ------------- | ------------- | ------------- |
| TP | 2645     |  283 | 2928     |
| FP | 423     | 141  | 564     |
| FN | 200     | 10  | 210     |
| Precision | 0.87     |  .67 | 0.84     |
| Recall | 0.93     |  .93 |  .93 |


### Model Performance
![alt text](figures/roc.png)
![alt text](figures/precision_recall.png)

Train Set          |  Test Set
:-------------------------:|:-------------------------:
![alt text](figures/dataset_stats/train_labels.jpg)  |  ![alt text](figures/dataset_stats/test_labels.jpg)
![alt text](figures/dataset_stats/train_labels_correlogram.jpg)   |   ![alt text](figures/dataset_stats/test_labels_correlogram.jpg)

