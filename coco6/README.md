## COCO6 Dataset

Ultralytics [COCO6](https://github.com/ultralytics/hub/tree/master/coco6) is an example small tutorial dataset composed of the first 6 images in Microsoft [COCO](https://github.com/ultralytics/yolov5/blob/master/data/coco.yaml) train2017. 3 images are used for training and 3 for validation. The intention of COCO6 is to provide an example for structuring custom YOLOv5 datasets and to provide a sanity check for YOLOv5 trainings with `python train.py --data coco6.yaml`.


### 1.1 Create dataset.yaml

[coco6.yaml](https://github.com/ultralytics/hub/blob/master/coco6/coco6.yaml), shown below, is the dataset config file that defines 1) the dataset root directory `path` and relative paths to `train` / `val` / `test` image directories (or *.txt files with image paths), 2) the number of classes `nc` and 3) a list of class `names`:

```yaml
# COCO6 dataset https://github.com/ultralytics/hub (first 6 images from COCO train2017)
# Example usage: python train.py --data coco6.yaml
# parent
# ├── yolov5
# └── datasets
#     └── coco6  ← downloads here


# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path:  # dataset root dir (leave empty for HUB)
train: images/train  # train images (relative to 'path') 8 images
val: images/val  # val images (relative to 'path') 8 images
test:  # test images (optional)

# Classes
names:
  0: person
  1: bicycle
  2: car
  3: motorcycle
  4: airplane
  5: bus
  6: train
  7: truck
  8: boat
  9: traffic light
  10: fire hydrant
  11: stop sign
  12: parking meter
  13: bench
  14: bird
  15: cat
  16: dog
  17: horse
  18: sheep
  19: cow
  20: elephant
  21: bear
  22: zebra
  23: giraffe
  24: backpack
  25: umbrella
  26: handbag
  27: tie
  28: suitcase
  29: frisbee
  30: skis
  31: snowboard
  32: sports ball
  33: kite
  34: baseball bat
  35: baseball glove
  36: skateboard
  37: surfboard
  38: tennis racket
  39: bottle
  40: wine glass
  41: cup
  42: fork
  43: knife
  44: spoon
  45: bowl
  46: banana
  47: apple
  48: sandwich
  49: orange
  50: broccoli
  51: carrot
  52: hot dog
  53: pizza
  54: donut
  55: cake
  56: chair
  57: couch
  58: potted plant
  59: bed
  60: dining table
  61: toilet
  62: tv
  63: laptop
  64: mouse
  65: remote
  66: keyboard
  67: cell phone
  68: microwave
  69: oven
  70: toaster
  71: sink
  72: refrigerator
  73: book
  74: clock
  75: vase
  76: scissors
  77: teddy bear
  78: hair drier
  79: toothbrush
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
