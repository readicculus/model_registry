# eo_pb_yolo_tiny_3l

| Model Info    |  |
| ------------- | ------------- |
| Input Size    | 416x416      |
| Classes       | Polar Bear    |
| Detection layers       | P<sub>5</sub>/32, P<sub>4</sub>/16, P<sub>3</sub>/8    |
| Iterations       | ~7,000  |
| Repo | AlexyAB/darknet b5ff7f4 |
| Initialization       | yolov3-tiny.conv.15  |
| Network       | [eo_pb_yolo_tiny_3l.cfg](model/eo_pb_yolo_tiny_3l.cfg)  |



| Dataset Info    |  |
| ------------- | ------------- |
| Background Ratio Train | N/A     |
| Background Ratio Test | N/A    |

**Benchmark speed (1080ti,batch_size=1): 371.2 FPS**


| Results @ .1 IOU, Thresh = .1    | Hotspot |
| ------------- | ------------- |
| TP | 78     |
| FP | 6     |
| FN | 13     |
| Precision | .93     |
| Recall | .86    |


### Model Performance
![alt text](figures/roc.png)
![alt text](figures/precision_recall.png)

Train Set          |  Test Set
:-------------------------:|:-------------------------:
![alt text](figures/dataset_stats/train_labels.jpg)  |  ![alt text](figures/dataset_stats/test_labels.jpg)
![alt text](figures/dataset_stats/train_labels_correlogram.jpg)   |   ![alt text](figures/dataset_stats/test_labels_correlogram.jpg)

