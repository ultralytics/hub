<div align="center">
  <p>
    <a href="https://platform.ultralytics.com/ultralytics/yolo26?utm_source=github&utm_medium=referral&utm_campaign=platform_launch&utm_content=banner&utm_term=platform_readme" target="_blank">
      <img width="100%" src="https://raw.githubusercontent.com/ultralytics/assets/main/yolov8/banner-yolov8.png" alt="Ultralytics YOLO banner"></a>
  </p>

[中文](README.zh-CN.md) | [한국어](https://docs.ultralytics.com/ko/platform) | [日本語](https://docs.ultralytics.com/ja/platform) | [Русский](https://docs.ultralytics.com/ru/platform) | [Deutsch](https://docs.ultralytics.com/de/platform) | [Français](https://docs.ultralytics.com/fr/platform) | [Español](https://docs.ultralytics.com/es/platform) | [Português](https://docs.ultralytics.com/pt/platform) | [Türkçe](https://docs.ultralytics.com/tr/platform) | [Tiếng Việt](https://docs.ultralytics.com/vi/platform) | [العربية](https://docs.ultralytics.com/ar/platform)

[![Ultralytics Discord](https://img.shields.io/discord/1089800235347353640?logo=discord&logoColor=white&label=Discord&color=blue)](https://discord.com/invite/ultralytics)
[![Ultralytics Forums](https://img.shields.io/discourse/users?server=https%3A%2F%2Fcommunity.ultralytics.com&logo=discourse&label=Forums&color=blue)](https://community.ultralytics.com/)
[![Ultralytics Reddit](https://img.shields.io/reddit/subreddit-subscribers/ultralytics?style=flat&logo=reddit&logoColor=white&label=Reddit&color=blue)](https://reddit.com/r/ultralytics)

</div>

Welcome from the [Ultralytics](https://www.ultralytics.com/) team. This repository now provides legacy support for existing Ultralytics HUB users while they migrate datasets, models, and workflows to [Ultralytics Platform](https://platform.ultralytics.com), the end-to-end computer vision platform for data preparation, annotation, YOLO model training, export, deployment, and monitoring.

> [!WARNING]
> Ultralytics HUB is being deprecated and will be wound down at the end of July 2026. Start all new computer vision work on Ultralytics Platform. Existing HUB users should migrate active datasets and models to Platform before the shutdown date.

Create a [Platform account](https://platform.ultralytics.com) to start new work. Existing HUB users can migrate datasets and models by creating a Platform account, then pasting their HUB API key into **Settings > Integrations > Ultralytics HUB**. For legacy repository support and migration questions, open an issue from this repository's **Issues** tab.

<p align="center">
  <img width="100%" src="https://cdn.jsdelivr.net/gh/ultralytics/assets@main/docs/platform/dataset-screenshot.avif" alt="Ultralytics Platform dataset interface">
</p>

<br>
<div align="center">
  <a href="https://github.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-github.png" width="2%" alt="Ultralytics GitHub"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="2%" alt="space">
  <a href="https://www.linkedin.com/company/ultralytics/"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-linkedin.png" width="2%" alt="Ultralytics LinkedIn"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="2%" alt="space">
  <a href="https://twitter.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-twitter.png" width="2%" alt="Ultralytics Twitter"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="2%" alt="space">
  <a href="https://www.youtube.com/ultralytics?sub_confirmation=1"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-youtube.png" width="2%" alt="Ultralytics YouTube"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="2%" alt="space">
  <a href="https://www.tiktok.com/@ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-tiktok.png" width="2%" alt="Ultralytics TikTok"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="2%" alt="space">
  <a href="https://ultralytics.com/bilibili"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-bilibili.png" width="2%" alt="Ultralytics BiliBili"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="2%" alt="space">
  <a href="https://discord.com/invite/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-discord.png" width="2%" alt="Ultralytics Discord"></a>
</div>

## 🗂️ Prepare and Upload Datasets

Ultralytics Platform datasets support the same YOLO task families used across [YOLO26](https://docs.ultralytics.com/models/yolo26), [YOLO11](https://docs.ultralytics.com/models/yolo11), [YOLOv8](https://docs.ultralytics.com/models/yolov8), and [YOLOv5](https://docs.ultralytics.com/models/yolov5): [object detection](https://docs.ultralytics.com/tasks/detect), [instance segmentation](https://docs.ultralytics.com/tasks/segment), [pose estimation](https://docs.ultralytics.com/tasks/pose), [oriented object detection](https://docs.ultralytics.com/tasks/obb), and [image classification](https://docs.ultralytics.com/tasks/classify).

- Upload images up to 50 MB, videos up to 1 GB, and ZIP, TAR, `.tar.gz`, `.tgz`, or NDJSON dataset files.
- Use Platform to automatically validate uploads, resize large images, generate thumbnails, parse labels, and compute statistics.
- Review and label data in grid, compact, and table views with annotation overlays, split filters, label filters, class filters, and filename search.
- Annotate detect, segment, pose, OBB, and classify datasets with manual tools, skeleton templates, Smart Annotation with SAM, and YOLO auto-labeling.
- Review dataset best practices in the [Ultralytics datasets documentation](https://docs.ultralytics.com/datasets).
- Learn about dataset annotation and preparation in the [data collection and annotation guide](https://docs.ultralytics.com/guides/data-collection-and-annotation).
- Explore open-source datasets such as [COCO](https://docs.ultralytics.com/datasets/detect/coco), [LVIS](https://docs.ultralytics.com/datasets/detect/lvis), and [ImageNet](https://docs.ultralytics.com/datasets/classify/imagenet).

### Dataset Preparation

Navigate to **Annotate** in Platform and click **New Dataset**, or drag files onto the Datasets card on the Home dashboard. For best results, upload a ZIP or TAR archive with a standard YOLO structure:

```text
my-dataset.zip
├── data.yaml
├── train/
│   ├── images/
│   │   ├── img001.jpg
│   │   └── img002.jpg
│   └── labels/
│       ├── img001.txt
│       └── img002.txt
└── val/
    ├── images/
    └── labels/
```

You can zip your dataset using:

```bash
# Zip the dataset directory for upload
cd my-dataset && zip -r ../my-dataset.zip .
```

See [example_datasets/coco8.zip](./example_datasets/coco8.zip) and the local `example_datasets/` directory for small YOLO-format archives. For more on dataset formats, visit the [Ultralytics datasets documentation](https://docs.ultralytics.com/datasets). Platform also accepts COCO JSON annotations, Ultralytics NDJSON exports, classification folder layouts, videos, and raw unannotated images for labeling in the annotation editor.

<p align="center">
  <img width="100%" src="https://cdn.jsdelivr.net/gh/ultralytics/assets@main/docs/platform/platform-quickstart-upload-dialog.avif" alt="Ultralytics Platform upload dialog">
</p>

### YAML Specifications

The dataset YAML should define dataset paths and class names using standard [YOLO dataset format](https://docs.ultralytics.com/guides/model-training-tips) conventions. For detailed instructions, see the [model training tips guide](https://docs.ultralytics.com/guides/model-training-tips).

```yaml
# Example YAML configuration for a custom dataset
path: .
train: train/images
val: val/images
test: # test images (optional)

# Class labels
names:
  0: person
  1: bicycle
  2: car
  3: motorcycle
  # Add more classes as needed
```

After upload, Platform checks image and label validity, generates previews, computes class and dimension statistics, and makes ready datasets available for annotation, cloud training, and local training through `ul://` dataset URIs.

## 🚀 Train a Model

Use [Ultralytics Platform](https://platform.ultralytics.com) to train YOLO models on cloud GPUs, compare experiments inside projects, manage trained `.pt` models, and stream local training metrics. Legacy HUB support remains available in this repository during the migration window, but new training should start on Platform.

- Click **Train Model** from a project, select a dataset, choose an official YOLO model or one of your trained models, set epochs and image size, and select a GPU.
- Monitor real-time charts, console logs, and system metrics while training runs.
- Use the best checkpoint after training for download, export, browser prediction, and deployment.
- Train locally with `ultralytics>=8.4.35` and stream metrics to Platform using your API key.
- Discover [model training tips](https://docs.ultralytics.com/guides/model-training-tips) for best practices.
- Learn about [hyperparameter tuning](https://docs.ultralytics.com/guides/hyperparameter-tuning) to optimize your results.
- Explore [experiment tracking integrations](https://docs.ultralytics.com/integrations/mlflow) for reproducible research.

<p align="center">
  <img width="100%" src="https://cdn.jsdelivr.net/gh/ultralytics/assets@main/docs/platform/platform-quickstart-training-dialog-cloud-tab.avif" alt="Ultralytics Platform cloud training dialog">
</p>

```bash
pip install -U ultralytics
export ULTRALYTICS_API_KEY="YOUR_API_KEY"

yolo train model=yolo26n.pt data=coco.yaml epochs=100 project=username/my-project name=experiment-1
```

Platform datasets can be used directly from training jobs with `ul://` dataset URIs:

```bash
yolo train model=yolo26n.pt data=ul://username/datasets/my-dataset epochs=100 project=username/my-project name=experiment-1
```

## 🌐 Deploy to the Real World

After training, use Platform to test models in the browser, export to production formats, and deploy dedicated endpoints. Platform supports browser prediction, monitored deployments, 43 global deployment regions, scale-to-zero behavior, and 17 export formats including [ONNX](https://onnx.ai/), [TensorRT](https://developer.nvidia.com/tensorrt), [CoreML](https://developer.apple.com/documentation/coreml), [TFLite](https://www.tensorflow.org/lite), [OpenVINO](https://docs.openvino.ai/latest/index.html), and TorchScript.

- Open the model **Predict** tab to upload images, tune confidence, IoU, and image size, and review predictions on canvas.
- Use the **Deploy** tab to select a region from the latency map and create a dedicated HTTPS endpoint.
- Monitor endpoint health, request logs, P95 latency, error rate, and usage metrics from Platform.
- Use ready-to-run Python, JavaScript, and cURL examples generated for your endpoint.
- Learn about [model deployment options](https://docs.ultralytics.com/guides/model-deployment-options) for edge and cloud.
- Explore [optimizing OpenVINO latency vs throughput](https://docs.ultralytics.com/guides/optimizing-openvino-latency-vs-throughput-modes) for real-time inference.
- Run models on [iOS](https://apps.apple.com/app/ultralytics/id1583935240) or [Android](https://play.google.com/store/apps/details?id=com.ultralytics.ultralytics_app) devices with the [Ultralytics App](https://www.ultralytics.com/app-install).

<p align="center">
  <img width="100%" src="https://cdn.jsdelivr.net/gh/ultralytics/assets@main/docs/platform/platform-deploy-tab-region-map-with-latency.avif" alt="Ultralytics Platform deployment region map">
</p>

## ❓ Have Issues or Questions?

For new work, start with [Ultralytics Platform](https://platform.ultralytics.com) and the [Platform quickstart](https://docs.ultralytics.com/platform/quickstart). If you need to move existing HUB work before the end of July 2026 wind-down, create a Platform account and paste your HUB API key into **Settings > Integrations > Ultralytics HUB** to migrate datasets and models.

- Use this repository's **Issues** tab for legacy HUB repository support and migration questions.
- Visit the [Ultralytics help center](https://docs.ultralytics.com/help/FAQ) for quick answers.
- Explore the [Ultralytics help center](https://docs.ultralytics.com/help) for troubleshooting and best practices.
- Explore the [Ultralytics Platform documentation](https://docs.ultralytics.com/platform) for current workflows.
- Join the [Ultralytics Discord community](https://discord.com/invite/ultralytics) for real-time discussions.

## 🤝 Contribute

We welcome contributions that improve legacy migration support, clarify Platform onboarding, or fix repository examples. See our [Contributing Guide](https://docs.ultralytics.com/help/contributing) for details on how to get involved. Thank you to all our contributors!

[![Ultralytics open-source contributors](https://raw.githubusercontent.com/ultralytics/assets/main/im/image-contributors.png)](https://github.com/ultralytics/ultralytics/graphs/contributors)

<br>
<div align="center">
  <a href="https://github.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-github.png" width="3%" alt="Ultralytics GitHub"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://www.linkedin.com/company/ultralytics/"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-linkedin.png" width="3%" alt="Ultralytics LinkedIn"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://twitter.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-twitter.png" width="3%" alt="Ultralytics Twitter"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://www.youtube.com/ultralytics?sub_confirmation=1"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-youtube.png" width="3%" alt="Ultralytics YouTube"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://www.tiktok.com/@ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-tiktok.png" width="3%" alt="Ultralytics TikTok"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://ultralytics.com/bilibili"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-bilibili.png" width="3%" alt="Ultralytics BiliBili"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://discord.com/invite/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-discord.png" width="3%" alt="Ultralytics Discord"></a>
</div>
