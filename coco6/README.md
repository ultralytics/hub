## COCO6 Dataset

Ultralytics [COCO6](https://github.com/ultralytics/hub/tree/master/coco6) is an example small tutorial dataset composed of the first 6 images in Microsoft [COCO](https://github.com/ultralytics/yolov5/blob/master/data/coco.yaml) train2017. 3 images are used for training and 3 for validation. The intention of COCO6 is to provide an example for structuring custom YOLOv5 datasets and to provide a sanity check for YOLOv5 trainings with `python train.py --data coco6.yaml`.


### 1.1 Create dataset.yaml

[coco6.yaml](https://github.com/ultralytics/hub/blob/master/coco6/coco6.yaml), shown below, is the dataset config file that defines 1) the dataset root directory `path` and relative paths to `train` / `val` / `test` image directories (or *.txt files with image paths), 2) the number of classes `nc` and 3) a list of class `names`:
```yaml
# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: # dataset root dir
train: images/train  # train images (relative to 'path') 3 images
val: images/val  # val images (relative to 'path') 3 images
test:  # test images (optional)

# Classes
nc: 80  # number of classes
names: [ 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light',
         'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
         'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee',
         'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard',
         'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
         'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch',
         'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
         'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear',
         'hair drier', 'toothbrush' ]  # class names
```


### 1.2 Create Labels

After using a tool like [Roboflow Annotate](https://roboflow.com/annotate?ref=ultralytics) to label your images, export your labels to **YOLO format**, with one `*.txt` file per image (if no objects in image, no `*.txt` file is required). The `*.txt` file specifications are:

- One row per object
- Each row is `class x_center y_center width height` format.
- Box coordinates must be in **normalized xywh** format (from 0 - 1). If your boxes are in pixels, divide `x_center` and `width` by image width, and `y_center` and `height` by image height.
- Class numbers are zero-indexed (start from 0).

<p align="center"><img width="700" src="https://user-images.githubusercontent.com/26833433/91506361-c7965000-e886-11ea-8291-c72b98c25eec.jpg"></p>

The label file corresponding to the above image contains 2 persons (class `0`) and a tie (class `27`):

<p align="center"><img width="428" src="https://user-images.githubusercontent.com/26833433/112467037-d2568c00-8d66-11eb-8796-55402ac0d62f.png"></p>


### 1.3 Organize Directories

Organize your train and val images and labels according to the example below. YOLOv5 assumes  `/coco6` is inside a `/datasets` directory **next to** the `/yolov5` directory:

```
├── yolov5
└── datasets
    └── coco6  ← downloads here (<1 MB)
        └── images
            ├── train
            └── val
        └── labels
            ├── train
            └── val
        └── coco6.yaml
```

**YOLOv5 locates labels automatically for each image** by replacing the last instance of `/images/` in each image path with `/labels/`. For example:

```bash
datasets/coco6/images/im0.jpg  # image
datasets/coco6/labels/im0.txt  # label
```

<p align="center"><img width="800" src="https://user-images.githubusercontent.com/26833433/141502652-e4b0477c-6c2a-41b3-b21a-b3d1444cdda7.png" title="COCO6" /></p>


## Support

Good luck 🍀! If you have any [YOLOv5](https://github.com/ultralytics/yolov5) or [HUB](https://hub.ultralytics.com/) questions or comments please visit:

- YOLOv5 support: https://github.com/ultralytics/yolov5/issues
- HUB support: https://github.com/ultralytics/hub/issues
- Community Forum: https://community.ultralytics.com/
