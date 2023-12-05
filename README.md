# Welcome to Ultralytics HUB!

👋 Welcome to [Ultralytics](https://ultralytics.com/)! We're excited to introduce the [Ultralytics HUB](https://bit.ly/ultralytics_hub), an innovative platform designed for training and deploying your YOLOv5 and YOLOv8 models with ease and efficiency! 🎉

Our goal is to provide you with comprehensive tools and documentation to help you leverage HUB's full potential. You can find detailed guidance in our [HUB Documentation](https://docs.ultralytics.com/). Should you have any inquiries or require assistance, feel free to submit a [GitHub Issue](https://github.com/ultralytics/hub/issues/new/choose), or join our vibrant [Discord Community](https://ultralytics.com/discord) for discussion and support.

<div align="center">
  <a href="https://github.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-github.png" width="20px" alt="Ultralytics GitHub"></a>
  &nbsp;&nbsp;&nbsp;
  <a href="https://www.linkedin.com/company/ultralytics/"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-linkedin.png" width="20px" alt="Ultralytics LinkedIn"></a>
  &nbsp;&nbsp;&nbsp;
  <a href="https://twitter.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-twitter.png" width="20px" alt="Ultralytics Twitter"></a>
  &nbsp;&nbsp;&nbsp;
  <a href="https://youtube.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-youtube.png" width="20px" alt="Ultralytics YouTube"></a>
  &nbsp;&nbsp;&nbsp;
  <a href="https://www.tiktok.com/@ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-tiktok.png" width="20px" alt="Ultralytics TikTok"></a>
  &nbsp;&nbsp;&nbsp;
  <a href="https://www.instagram.com/ultralytics/"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-instagram.png" width="20px" alt="Ultralytics Instagram"></a>
  &nbsp;&nbsp;&nbsp;
  <a href="https://ultralytics.com/discord"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-discord.png" width="20px" alt="Ultralytics Discord"></a>
</div>

## 🗂️ 1. Upload a Dataset

Ultralytics HUB datasets align with the format used by [YOLOv5](https://github.com/ultralytics/yolov5) and [YOLOv8](https://github.com/ultralytics/ultralytics). They adhere to the same structural and labeling conventions, ensuring a seamless experience.

### Dataset Preparation:
Ensure that the YAML file describing your dataset is placed in the root directory of your dataset, as illustrated below. Once in place, zip the directory for uploading to [Ultralytics HUB](https://hub.ultralytics.com/). The dataset YAML, its directory, and the zip file should all bear the identical name.

For instance, with a dataset named 'coco8', as shown in [ultralytics/hub/example_datasets/coco8.zip](./example_datasets/coco8.zip), include a `coco8.yaml` within the `coco8/` directory. Zip this to form `coco8.zip` for upload with the command:

```bash
# Zipping the dataset directory for upload
zip -r coco8.zip coco8
```

Explore the provided [example_datasets/coco8.zip](./example_datasets/coco8.zip) for insights on structuring your custom dataset. 

### YAML Specifications:
The dataset YAML follows the established YOLOv5 and YOLOv8 format. For exhaustive instructions, refer to the [Train Custom Data tutorial](https://docs.ultralytics.com/yolov5/tutorials/train_custom_data/).

```yaml
# YAML configuration example for custom datasets
path:  # dataset root dir (leave empty for HUB integration)
train: images/train  # train images (relative to 'path') 8 images
val: images/val  # val images (relative to 'path') 8 images
test:  # test images (optional)

# Class labels
names:
  0: person
  1: bicycle
  2: car
  3: motorcycle
  # Add more classes as needed
```

Upload your dataset to [Ultralytics HUB](https://bit.ly/ultralytics_hub) by logging in, navigating to the 'Datasets' tab, and selecting 'Upload Dataset'. This lets you scan and view your dataset prior to training YOLOv5 or YOLOv8 models.

<p align="center">
  <img width="80%" src="https://user-images.githubusercontent.com/26833433/201424843-20fa081b-ad4b-4d6c-a095-e810775908d8.png" title="COCO8 Dataset Example" />
</p>

## 🚀 2. Train a Model

Connect to the Ultralytics HUB notebook and employ your model API key to embark on model training!

<a href="https://colab.research.google.com/github/ultralytics/hub/blob/master/hub.ipynb" target="_blank">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" />
</a>

## 🌐 3. Deploy to the Real World

Transition your model to 13 different formats including TensorFlow, ONNX, OpenVINO, CoreML, Paddle, and more. Operate your models directly on your [iOS](https://apps.apple.com/xk/app/ultralytics/id1583935240) or
[Android](https://play.google.com/store/apps/details?id=com.ultralytics.ultralytics_app) mobile device by downloading the [Ultralytics App](https://ultralytics.com/app_install)!

## ❓ Have Issues or Questions?

For those just embarking on their [Ultralytics HUB](https://bit.ly/ultralytics_hub) journey, the [Issues](https://github.com/ultralytics/hub/issues) tab is your go-to resource for support. Click the 'New Issue' button and share your thoughts or questions. Our aim is to enhance your experience with invaluable solutions and improvements! 😃

<div align="center">
  <a href="https://github.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-github.png" width="30px" alt="Ultralytics GitHub"></a>
  &nbsp;&nbsp;&nbsp;
  <a href="https://www.linkedin.com/company/ultralytics/"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-linkedin.png" width="30px" alt="Ultralytics LinkedIn"></a>
  &nbsp;&nbsp;&nbsp;
  <a href="https://twitter.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-twitter.png" width="30px" alt="Ultralytics Twitter"></a>
  &nbsp;&nbsp;&nbsp;
  <a href="https://youtube.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-youtube.png" width="30px" alt="Ultralytics YouTube"></a>
  &nbsp;&nbsp;&nbsp;
  <a href="https://www.tiktok.com/@ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-tiktok.png" width="30px" alt="Ultralytics TikTok"></a>
  &nbsp;&nbsp;&nbsp;
  <a href="https://www.instagram.com/ultralytics/"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-instagram.png" width="30px" alt="Ultralytics Instagram"></a>
  &nbsp;&nbsp;&nbsp;
  <a href="https://ultralytics.com/discord"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-discord.png" width="30px" alt="Ultralytics Discord"></a>
</div>
