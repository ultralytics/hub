<a align="center" href="https://ultralytics.com" target="_blank">
<img width="1024", src="https://user-images.githubusercontent.com/26833433/142024981-979d6214-1520-4c3b-b29b-1bdb3355229d.png"></a>
<br><br>
<div align="center">
   <a href="https://github.com/ultralytics">
   <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-social-github.png" width="2%"/>
   </a>
   <img width="2%" />
   <a href="https://www.linkedin.com/company/ultralytics">
   <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-social-linkedin.png" width="2%"/>
   </a>
   <img width="2%" />
   <a href="https://twitter.com/ultralytics">
   <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-social-twitter.png" width="2%"/>
   </a>
   <img width="2%" />
   <a href="https://youtube.com/ultralytics">
   <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-social-youtube.png" width="2%"/>
   </a>
   <img width="2%" />
   <a href="https://www.facebook.com/ultralytics">
   <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-social-facebook.png" width="2%"/>
   </a>
   <img width="2%" />
   <a href="https://www.instagram.com/ultralytics/">
   <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-social-instagram.png" width="2%"/>
   </a>
</div>
<br>

👋 Hello from the [Ultralytics](https://ultralytics.com/) Team! We've been working hard these last few months to launch [Ultralytics HUB](https://ultralytics.com/hub), a new web tool for training and deploying all your YOLOv5 🚀 models from one spot!


## 1. Create a Dataset

Ultralytics HUB datasets are just like YOLOv5 🚀 datasets, they use the same structure and the same label formats to keep everything simple. 

When you upload a dataset to Ultralytics HUB, make sure to **place your dataset yaml inside the dataset root directory** as in the example shown below, and then zip for upload to https://hub.ultralytics.com/. Your **dataset yaml, directory and zip** should all share the same name. For example, if your dataset is called 'coco6' as in our example [ultralytics/hub/coco6.zip](https://github.com/ultralytics/hub/blob/master/coco6.zip), then you should have a coco6.yaml inside your coco6/ directory, which should zip to create coco6.zip for upload:

```bash
zip -r coco6.zip coco6
```

The example [coco6.zip](https://github.com/ultralytics/hub/blob/master/coco6.zip) dataset in this repository can be downloaded and unzipped to see exactly how to structure your custom dataset.
<p align="center"><img width="800" src="https://user-images.githubusercontent.com/26833433/141502652-e4b0477c-6c2a-41b3-b21a-b3d1444cdda7.png" title="COCO6" /></p>

The dataset yaml is the same standard YOLOv5 yaml format. See the [YOLOv5 Train Custom Data tutorial](https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data) for full details.
```yaml
# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path:  # dataset root dir (leave empty for HUB)
train: images/train  # train images (relative to 'path') 8 images
val: images/val  # val images (relative to 'path') 8 images
test:  # test images (optional)

# Classes
nc: 80  # number of classes
names: [ 'person', 'bicycle', 'car', ...]
```

After zipping your dataset, sign in to HUB at https://hub.ultralytics.com and click on the Datasets tab. Click 'Upload Dataset' to upload, scan and visualize your new dataset before training new YOLOv5 models on it!

<img width="1200" alt="HUB Dataset Upload" src="https://user-images.githubusercontent.com/26833433/141504055-cf2cb4bf-6045-4957-bf23-d4d2c8a94fae.png">

## 2. Train a Model

TODO


## ❓ Issues

If you are a new Ultralytics HUB user and have questions or comments, you are in the right place! Please click the [New Issue](https://github.com/ultralytics/hub/issues/new/choose) button in the [Issues](https://github.com/ultralytics/hub/issues) tab in this [ultralytics/hub](https://github.com/ultralytics/hub) repo and let us know what we can do to make your life better 😃!

<p align="center"><img width="900" src="https://user-images.githubusercontent.com/26833433/141508090-9d0fee01-e3c5-40e4-a762-7617bfff5d2e.png" title="Raise an Issue" /></p>


<br>
<div align="center">
    <a href="https://github.com/ultralytics">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-social-github.png" width="3%"/>
    </a>
    <img width="3%" />
    <a href="https://www.linkedin.com/company/ultralytics">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-social-linkedin.png" width="3%"/>
    </a>
    <img width="3%" />
    <a href="https://twitter.com/ultralytics">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-social-twitter.png" width="3%"/>
    </a>
    <img width="3%" />
    <a href="https://youtube.com/ultralytics">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-social-youtube.png" width="3%"/>
    </a>
    <img width="3%" />
    <a href="https://www.facebook.com/ultralytics">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-social-facebook.png" width="3%"/>
    </a>
    <img width="3%" />
    <a href="https://www.instagram.com/ultralytics/">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-social-instagram.png" width="3%"/>
    </a>
</div>
