<div align="center">
  <p>
    <a href="https://www.ultralytics.com/hub" target="_blank">
      <img width="100%" src="https://github.com/ultralytics/assets/raw/main/im/ultralytics-hub.png"></a>
  </p>

[中文](https://docs.ultralytics.com/zh/hub/) | [한국어](https://docs.ultralytics.com/ko/hub/) | [日本語](https://docs.ultralytics.com/ja/hub/) | [Русский](https://docs.ultralytics.com/ru/hub/) | [Deutsch](https://docs.ultralytics.com/de/hub/) | [Français](https://docs.ultralytics.com/fr/hub/) | [Español](https://docs.ultralytics.com/es/hub/) | [Português](https://docs.ultralytics.com/pt/hub/) | [Türkçe](https://docs.ultralytics.com/tr/hub/) | [Tiếng Việt](https://docs.ultralytics.com/vi/hub/) | [العربية](https://docs.ultralytics.com/ar/hub/)

[![Ultralytics Actions](https://github.com/ultralytics/hub/actions/workflows/ci.yml/badge.svg)](https://github.com/ultralytics/hub/actions/workflows/ci.yml)
[![Ultralytics Discord](https://img.shields.io/discord/1089800235347353640?logo=discord&logoColor=white&label=Discord&color=blue)](https://discord.com/invite/ultralytics)
[![Ultralytics Forums](https://img.shields.io/discourse/users?server=https%3A%2F%2Fcommunity.ultralytics.com&logo=discourse&label=Forums&color=blue)](https://community.ultralytics.com/)
[![Ultralytics Reddit](https://img.shields.io/reddit/subreddit-subscribers/ultralytics?style=flat&logo=reddit&logoColor=white&label=Reddit&color=blue)](https://reddit.com/r/ultralytics)
<a href="https://colab.research.google.com/github/ultralytics/hub/blob/main/hub.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a>

👋 Hello from the [Ultralytics](https://www.ultralytics.com/) Team! We've been working hard these last few months to launch [Ultralytics HUB](https://www.ultralytics.com/hub), a new platform for training and deploying all your [Ultralytics YOLOv5](https://docs.ultralytics.com/models/yolov5/) and [YOLOv8](https://docs.ultralytics.com/models/yolov8/) 🚀 models from one central location!

We hope that the resources here will help you get the most out of Ultralytics HUB. Please browse the [Ultralytics HUB documentation](https://docs.ultralytics.com/hub/) for details, raise an issue on [GitHub](https://github.com/ultralytics/hub/issues/new/choose) for support, and join our [Discord community](https://discord.com/invite/ultralytics) for questions and discussions!

<br>
<div align="center">
  <a href="https://github.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-github.png" width="2%" alt="Ultralytics GitHub"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="2%">
  <a href="https://www.linkedin.com/company/ultralytics/"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-linkedin.png" width="2%" alt="Ultralytics LinkedIn"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="2%">
  <a href="https://twitter.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-twitter.png" width="2%" alt="Ultralytics Twitter"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="2%">
  <a href="https://youtube.com/ultralytics?sub_confirmation=1"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-youtube.png" width="2%" alt="Ultralytics YouTube"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="2%">
  <a href="https://www.tiktok.com/@ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-tiktok.png" width="2%" alt="Ultralytics TikTok"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="2%">
  <a href="https://ultralytics.com/bilibili"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-bilibili.png" width="2%" alt="Ultralytics BiliBili"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="2%">
  <a href="https://discord.com/invite/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-discord.png" width="2%" alt="Ultralytics Discord"></a>
</div>
</div>

## 🗂️ Upload a Dataset

Ultralytics HUB datasets align with the format used by [YOLOv5](https://github.com/ultralytics/yolov5) and [YOLOv8](https://github.com/ultralytics/ultralytics). They adhere to the same structural and labeling conventions, ensuring a seamless experience for [object detection](https://docs.ultralytics.com/tasks/detect/), [segmentation](https://docs.ultralytics.com/tasks/segment/), and [classification](https://docs.ultralytics.com/tasks/classify/) tasks.

### Dataset Preparation

Ensure that the YAML file describing your dataset is placed in the root directory of your dataset, as illustrated below. Once in place, zip the directory for uploading to [Ultralytics HUB](https://www.ultralytics.com/hub). The dataset YAML, its directory, and the zip file should all share the identical name.

For instance, with a dataset named 'coco8', as shown in [ultralytics/hub/example_datasets/coco8.zip](./example_datasets/coco8.zip), include a `coco8.yaml` within the `coco8/` directory. Zip this directory to form `coco8.zip` for upload using a command like:

```bash
# Zipping the dataset directory for upload
zip -r coco8.zip coco8
```

Explore the provided [example_datasets/coco8.zip](./example_datasets/coco8.zip) for insights on structuring your custom dataset. You can find more information on dataset formats in our [datasets documentation](https://docs.ultralytics.com/datasets/).

<p align="center">
<img width="70%" src="https://raw.githubusercontent.com/ultralytics/assets/main/docs/hub/datasets/hub_upload_dataset_1.jpg" title="COCO8 Example Dataset Structure" />
</p>

### YAML Specifications

The dataset YAML follows the established YOLOv5 and YOLOv8 format. For comprehensive instructions, refer to the [Train Custom Data guide](https://docs.ultralytics.com/guides/model-training-tips/).

```yaml
# YAML configuration example for custom datasets
path: ../datasets/coco8 # dataset root dir (can be relative or absolute)
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

Upload your zipped dataset to [Ultralytics HUB](https://www.ultralytics.com/hub) by logging in, navigating to the ['Datasets' tab](https://docs.ultralytics.com/hub/datasets/), and selecting 'Upload Dataset'. This allows you to scan and view your dataset prior to training YOLOv5 or YOLOv8 models.

<p align="center">
  <img width="100%" alt="Ultralytics HUB Dataset Upload Interface" src="https://user-images.githubusercontent.com/26833433/216763338-9a8812c8-a4e5-4362-8102-40dad7818396.png">
</p>

## 🚀 Train a Model

Connect to the Ultralytics HUB notebook and use your API key to start [model training](https://docs.ultralytics.com/modes/train/)! Ultralytics HUB offers streamlined [cloud training](https://docs.ultralytics.com/hub/cloud-training/) options, making it easy to train models without local hardware constraints.

<a href="https://colab.research.google.com/github/ultralytics/hub/blob/main/hub.ipynb" target="_blank">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" />
</a>

## 🌐 Deploy to the Real World

Transition your trained model to various formats using the [Export mode](https://docs.ultralytics.com/modes/export/), including [TensorFlow](https://www.tensorflow.org/), [ONNX](https://onnx.ai/), [OpenVINO](https://docs.openvino.ai/latest/index.html), [CoreML](https://developer.apple.com/documentation/coreml), [PaddlePaddle](https://www.paddlepaddle.org.cn/en), and more (13+ formats supported). Operate your models directly on your [iOS](https://apps.apple.com/app/ultralytics/id1583935240) or [Android](https://play.google.com/store/apps/details?id=com.ultralytics.ultralytics_app) mobile device by downloading the [Ultralytics App](https://www.ultralytics.com/app-install)! Explore various [model deployment options](https://docs.ultralytics.com/guides/model-deployment-options/) for edge devices and cloud platforms.

## ❓ Have Issues or Questions?

For those just starting their [Ultralytics HUB](https://www.ultralytics.com/hub) journey, the [GitHub Issues](https://github.com/ultralytics/hub/issues) tab is your primary resource for support and bug reporting. Click the 'New Issue' button and share your thoughts, questions, or report problems. Our aim is to enhance your experience by providing valuable solutions and continuous improvements! 😃

## Contribute

We love contributions! ❤️ See our [Contributing Guide](https://docs.ultralytics.com/help/contributing/) for more details on how to get involved. Thank you to all our contributors!

[![Ultralytics open-source contributors](https://raw.githubusercontent.com/ultralytics/assets/main/im/image-contributors.png)](https://github.com/ultralytics/ultralytics/graphs/contributors)

<br>
<div align="center">
  <a href="https://github.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-github.png" width="3%" alt="Ultralytics GitHub"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%">
  <a href="https://www.linkedin.com/company/ultralytics/"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-linkedin.png" width="3%" alt="Ultralytics LinkedIn"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%">
  <a href="https://twitter.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-twitter.png" width="3%" alt="Ultralytics Twitter"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%">
  <a href="https://youtube.com/ultralytics?sub_confirmation=1"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-youtube.png" width="3%" alt="Ultralytics YouTube"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%">
  <a href="https://www.tiktok.com/@ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-tiktok.png" width="3%" alt="Ultralytics TikTok"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%">
  <a href="https://ultralytics.com/bilibili"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-bilibili.png" width="3%" alt="Ultralytics BiliBili"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%">
  <a href="https://discord.com/invite/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-discord.png" width="3%" alt="Ultralytics Discord"></a>
</div>
