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

👋 Welcome from the [Ultralytics](https://www.ultralytics.com/) Team! We're excited to introduce [Ultralytics HUB](https://www.ultralytics.com/hub), your all-in-one platform for training, deploying, and managing [Ultralytics YOLO](https://www.ultralytics.com/yolo) models—including [YOLO11](https://docs.ultralytics.com/models/yolo11/), [YOLOv8](https://docs.ultralytics.com/models/yolov8/), [YOLOv5](https://docs.ultralytics.com/models/yolov5/), and more—from a single, intuitive interface. 🚀

Explore the [Ultralytics HUB documentation](https://docs.ultralytics.com/hub/) for comprehensive guides, open [GitHub Issues](https://github.com/ultralytics/hub/issues/new/choose) for support, and join our [Discord community](https://discord.com/invite/ultralytics) for discussions and collaboration!

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

Ultralytics HUB datasets follow the same structure and labeling conventions as [YOLO11](https://docs.ultralytics.com/models/yolo11/), [YOLOv8](https://docs.ultralytics.com/models/yolov8/), and [YOLOv5](https://docs.ultralytics.com/models/yolov5/), ensuring seamless compatibility for [object detection](https://docs.ultralytics.com/tasks/detect/), [instance segmentation](https://docs.ultralytics.com/tasks/segment/), and [image classification](https://docs.ultralytics.com/tasks/classify/) projects.

- Review dataset best practices in the [Ultralytics datasets documentation](https://docs.ultralytics.com/datasets/).
- Learn about dataset annotation and preparation in the [data collection and annotation guide](https://docs.ultralytics.com/guides/data-collection-and-annotation/).
- Explore open-source datasets such as [COCO](https://docs.ultralytics.com/datasets/detect/coco/), [LVIS](https://docs.ultralytics.com/datasets/detect/lvis/), and [ImageNet](https://docs.ultralytics.com/datasets/classify/imagenet/).

### Dataset Preparation

Place your dataset YAML file in the root directory of your dataset. The YAML file, its directory, and the zipped archive should all share the same name for easy upload to [Ultralytics HUB](https://www.ultralytics.com/hub). For example, for a dataset called `coco8`, your structure should look like:

- `coco8/`
  - `coco8.yaml`
  - `images/`
  - `labels/`
- `coco8.zip` (the zipped directory for upload)

You can zip your dataset using:

```bash
# Zip the dataset directory for upload
zip -r coco8.zip coco8
```

See [example_datasets/coco8.zip](./example_datasets/coco8.zip) for a working example. For more on dataset formats, visit the [Ultralytics datasets documentation](https://docs.ultralytics.com/datasets/).

<p align="center">
<img width="100%" src="https://raw.githubusercontent.com/ultralytics/assets/main/docs/hub/datasets/hub_upload_dataset_1.jpg" title="COCO8 Example Dataset Structure" />
</p>

### YAML Specifications

The dataset YAML should follow the [YOLO dataset format](https://docs.ultralytics.com/guides/model-training-tips/). For detailed instructions, see the [model training tips guide](https://docs.ultralytics.com/guides/model-training-tips/).

```yaml
# Example YAML configuration for a custom dataset
path: ../datasets/coco8 # dataset root directory (relative or absolute)
train: images/train # training images (relative to 'path')
val: images/val # validation images (relative to 'path')
test: # test images (optional)

# Class labels
names:
  0: person
  1: bicycle
  2: car
  3: motorcycle
  # Add more classes as needed
```

Upload your zipped dataset to [Ultralytics HUB](https://www.ultralytics.com/hub) by logging in, navigating to the [Datasets tab](https://docs.ultralytics.com/hub/datasets/), and selecting 'Upload Dataset'. You can preview and scan your dataset before training your YOLO models.

<p align="center">
  <img width="100%" alt="Ultralytics HUB Dataset Upload Interface" src="https://user-images.githubusercontent.com/26833433/216763338-9a8812c8-a4e5-4362-8102-40dad7818396.png">
</p>

## 🚀 Train a Model

Connect to the Ultralytics HUB notebook and use your API key to start [training your models](https://docs.ultralytics.com/modes/train/)! Ultralytics HUB provides [cloud training](https://docs.ultralytics.com/hub/cloud-training/) for fast, scalable model development—no local GPU required.

- Discover [model training tips](https://docs.ultralytics.com/guides/model-training-tips/) for best practices.
- Learn about [hyperparameter tuning](https://docs.ultralytics.com/guides/hyperparameter-tuning/) to optimize your results.
- Explore [experiment tracking integrations](https://docs.ultralytics.com/integrations/mlflow/) for reproducible research.

<a href="https://colab.research.google.com/github/ultralytics/hub/blob/main/hub.ipynb" target="_blank">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" />
</a>

## 🌐 Deploy to the Real World

After training, deploy your models to production using the [Export mode](https://docs.ultralytics.com/modes/export/). Ultralytics HUB supports 13+ export formats, including [TensorFlow](https://www.tensorflow.org/), [ONNX](https://onnx.ai/), [OpenVINO](https://docs.openvino.ai/latest/index.html), [CoreML](https://developer.apple.com/documentation/coreml), [PaddlePaddle](https://www.paddlepaddle.org.cn/en), and more.

- Learn about [model deployment options](https://docs.ultralytics.com/guides/model-deployment-options/) for edge and cloud.
- Explore [optimizing OpenVINO latency vs throughput](https://docs.ultralytics.com/guides/optimizing-openvino-latency-vs-throughput-modes/) for real-time inference.
- Run your models on [iOS](https://apps.apple.com/app/ultralytics/id1583935240) or [Android](https://play.google.com/store/apps/details?id=com.ultralytics.ultralytics_app) devices with the [Ultralytics App](https://www.ultralytics.com/app-install).

## ❓ Have Issues or Questions?

If you're new to [Ultralytics HUB](https://www.ultralytics.com/hub), the [GitHub Issues](https://github.com/ultralytics/hub/issues) tab is your go-to resource for support and bug reporting. Click 'New Issue' to share your questions, feedback, or report problems. Our team is dedicated to providing solutions and continuously improving your experience! 😃

- Visit the [Ultralytics HUB FAQ](https://docs.ultralytics.com/help/FAQ/) for quick answers.
- Explore the [Ultralytics help center](https://docs.ultralytics.com/help/) for troubleshooting and best practices.
- Join the [Ultralytics Discord community](https://discord.com/invite/ultralytics) for real-time discussions.

## 🤝 Contribute

We welcome and value your contributions! ❤️ See our [Contributing Guide](https://docs.ultralytics.com/help/contributing/) for details on how to get involved. Thank you to all our amazing contributors!

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

