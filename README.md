<div align="center">
  <p>
    <a href="https://bit.ly/ultralytics_hub" target="_blank">
      <img width="100%" src="https://github.com/ultralytics/assets/raw/main/im/ultralytics-hub.png"></a>
  </p>

[中文](https://docs.ultralytics.com/zh/hub/) | [한국어](https://docs.ultralytics.com/ko/hub/) | [日本語](https://docs.ultralytics.com/ja/hub/) | [Русский](https://docs.ultralytics.com/ru/hub/) | [Deutsch](https://docs.ultralytics.com/de/hub/) | [Français](https://docs.ultralytics.com/fr/hub/) | [Español](https://docs.ultralytics.com/es/hub/) | [Português](https://docs.ultralytics.com/pt/hub/) | [Türkçe](https://docs.ultralytics.com/tr/hub/) | [Tiếng Việt](https://docs.ultralytics.com/vi/hub/) | [हिन्दी](https://docs.ultralytics.com/hi/hub/) | [العربية](https://docs.ultralytics.com/ar/hub/)

<a href="https://github.com/ultralytics/hub/actions/workflows/ci.yaml"><img src="https://github.com/ultralytics/hub/actions/workflows/ci.yaml/badge.svg" alt="CI CPU"></a> <a href="https://colab.research.google.com/github/ultralytics/hub/blob/main/hub.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a> <a href="https://ultralytics.com/discord"><img alt="Discord" src="https://img.shields.io/discord/1089800235347353640?logo=discord&logoColor=white&label=Discord&color=blue"></a>

👋 Hello from the [Ultralytics](https://ultralytics.com/) Team! We've been working hard these last few months to launch [Ultralytics HUB](https://bit.ly/ultralytics_hub), a new web tool for training and deploying all your YOLOv5 and YOLOv8 🚀 models from one spot!

We hope that the resources here will help you get the most out of HUB. Please browse the HUB <a href="https://docs.ultralytics.com/">Docs</a> for details, raise an issue on <a href="https://github.com/ultralytics/hub/issues/new/choose">GitHub</a> for support, and join our <a href="https://ultralytics.com/discord">Discord</a> community for questions and discussions!

<br>
<div align="center">
  <a href="https://github.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-github.png" width="2%" alt="Ultralytics GitHub"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="2%">
  <a href="https://www.linkedin.com/company/ultralytics/"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-linkedin.png" width="2%" alt="Ultralytics LinkedIn"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="2%">
  <a href="https://twitter.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-twitter.png" width="2%" alt="Ultralytics Twitter"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="2%">
  <a href="https://youtube.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-youtube.png" width="2%" alt="Ultralytics YouTube"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="2%">
  <a href="https://www.tiktok.com/@ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-tiktok.png" width="2%" alt="Ultralytics TikTok"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="2%">
  <a href="https://www.instagram.com/ultralytics/"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-instagram.png" width="2%" alt="Ultralytics Instagram"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="2%">
  <a href="https://ultralytics.com/discord"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-discord.png" width="2%" alt="Ultralytics Discord"></a>
</div>
</div>

## 🗂️ 1. Upload a Dataset

Ultralytics HUB datasets align with the format used by [YOLOv5](https://github.com/ultralytics/yolov5) and [YOLOv8](https://github.com/ultralytics/ultralytics). They adhere to the same structural and labeling conventions, ensuring a seamless experience.

### Dataset Preparation:

Ensure that the YAML file describing your dataset is placed in the root directory of your dataset, as illustrated below. Once in place, zip the directory for uploading to [Ultralytics HUB](https://bit.ly/ultralytics_hub). The dataset YAML, its directory, and the zip file should all bear the identical name.

For instance, with a dataset named 'coco8', as shown in [ultralytics/hub/example_datasets/coco8.zip](./example_datasets/coco8.zip), include a `coco8.yaml` within the `coco8/` directory. Zip this to form `coco8.zip` for upload with the command:

```bash
# Zipping the dataset directory for upload
zip -r coco8.zip coco8
```

Explore the provided [example_datasets/coco8.zip](./example_datasets/coco8.zip) for insights on structuring your custom dataset.

<p align="center">
<img width="80%" src="https://user-images.githubusercontent.com/26833433/201424843-20fa081b-ad4b-4d6c-a095-e810775908d8.png" title="COCO8" />
</p>

### YAML Specifications:

The dataset YAML follows the established YOLOv5 and YOLOv8 format. For exhaustive instructions, refer to the [Train Custom Data tutorial](https://docs.ultralytics.com/yolov5/tutorials/train_custom_data/).

```yaml
# YAML configuration example for custom datasets
path: # dataset root dir (leave empty for HUB integration)
train: images/train # train images (relative to 'path') 8 images
val: images/val # val images (relative to 'path') 8 images
test: # test images (optional)

# Class labels
names:
  0: person
  1: bicycle
  2: car
  3: motorcycle
  # Add more classes as needed
```

Upload your zipped dataset to [Ultralytics HUB](https://bit.ly/ultralytics_hub) by logging in, navigating to the 'Datasets' tab, and selecting 'Upload Dataset'. This lets you scan and view your dataset prior to training YOLOv5 or YOLOv8 models.

<p align="center">
  <img width="100%" alt="HUB Dataset Upload" src="https://user-images.githubusercontent.com/26833433/216763338-9a8812c8-a4e5-4362-8102-40dad7818396.png">
</p>

## 🚀 2. Train a Model

Connect to the Ultralytics HUB notebook and employ your model API key to embark on model training!

<a href="https://colab.research.google.com/github/ultralytics/hub/blob/main/hub.ipynb" target="_blank">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" />
</a>

## 🌐 3. Deploy to the Real World

Transition your model to 13 different formats including TensorFlow, ONNX, OpenVINO, CoreML, Paddle, and more. Operate your models directly on your [iOS](https://apps.apple.com/xk/app/ultralytics/id1583935240) or [Android](https://play.google.com/store/apps/details?id=com.ultralytics.ultralytics_app) mobile device by downloading the [Ultralytics App](https://ultralytics.com/app_install)!

## ❓ Have Issues or Questions?

For those just embarking on their [Ultralytics HUB](https://bit.ly/ultralytics_hub) journey, the [Issues](https://github.com/ultralytics/hub/issues) tab is your go-to resource for support. Click the 'New Issue' button and share your thoughts or questions. Our aim is to enhance your experience with invaluable solutions and improvements! 😃

<br>
<div align="center">
  <a href="https://github.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-github.png" width="3%" alt="Ultralytics GitHub"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%">
  <a href="https://www.linkedin.com/company/ultralytics/"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-linkedin.png" width="3%" alt="Ultralytics LinkedIn"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%">
  <a href="https://twitter.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-twitter.png" width="3%" alt="Ultralytics Twitter"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%">
  <a href="https://youtube.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-youtube.png" width="3%" alt="Ultralytics YouTube"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%">
  <a href="https://www.tiktok.com/@ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-tiktok.png" width="3%" alt="Ultralytics TikTok"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%">
  <a href="https://www.instagram.com/ultralytics/"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-instagram.png" width="3%" alt="Ultralytics Instagram"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%">
  <a href="https://ultralytics.com/discord"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-discord.png" width="3%" alt="Ultralytics Discord"></a>
</div>
