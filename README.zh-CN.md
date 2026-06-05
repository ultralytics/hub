<div align="center">
  <p>
    <a href="https://platform.ultralytics.com/ultralytics/yolo26?utm_source=github&utm_medium=referral&utm_campaign=platform_launch&utm_content=banner&utm_term=platform_readme" target="_blank">
      <img width="100%" src="https://raw.githubusercontent.com/ultralytics/assets/main/yolov8/banner-yolov8.png" alt="Ultralytics YOLO banner"></a>
  </p>

[English](README.md) | [한국어](https://docs.ultralytics.com/ko/platform) | [日本語](https://docs.ultralytics.com/ja/platform) | [Русский](https://docs.ultralytics.com/ru/platform) | [Deutsch](https://docs.ultralytics.com/de/platform) | [Français](https://docs.ultralytics.com/fr/platform) | [Español](https://docs.ultralytics.com/es/platform) | [Português](https://docs.ultralytics.com/pt/platform) | [Türkçe](https://docs.ultralytics.com/tr/platform) | [Tiếng Việt](https://docs.ultralytics.com/vi/platform) | [العربية](https://docs.ultralytics.com/ar/platform)

[![Ultralytics Discord](https://img.shields.io/discord/1089800235347353640?logo=discord&logoColor=white&label=Discord&color=blue)](https://discord.com/invite/ultralytics)
[![Ultralytics Forums](https://img.shields.io/discourse/users?server=https%3A%2F%2Fcommunity.ultralytics.com&logo=discourse&label=Forums&color=blue)](https://community.ultralytics.com/)
[![Ultralytics Reddit](https://img.shields.io/reddit/subreddit-subscribers/ultralytics?style=flat&logo=reddit&logoColor=white&label=Reddit&color=blue)](https://reddit.com/r/ultralytics)

</div>

来自 [Ultralytics](https://www.ultralytics.com/) 团队的问候。本仓库现在用于为现有 Ultralytics HUB 用户提供旧版支持，帮助他们将数据集、模型和工作流迁移到 [Ultralytics Platform](https://platform.ultralytics.com)。Platform 是端到端计算机视觉平台，覆盖数据准备、标注、YOLO 模型训练、导出、部署和监控。

> [!WARNING]
> Ultralytics HUB 正在逐步停用，并将于 2026 年 7 月底完成下线。所有新的计算机视觉工作都应从 Ultralytics Platform 开始。现有 HUB 用户应在下线日期前将仍在使用的数据集和模型迁移到 Platform。

请创建 [Platform 账号](https://platform.ultralytics.com) 开始新的工作流。现有 HUB 用户可在创建 Platform 账号后，进入 **Settings > Integrations > Ultralytics HUB** 粘贴 HUB API key，迁移数据集和模型。如需旧版仓库支持或迁移帮助，请在本仓库的 **Issues** 页面提交问题。

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

## 🗂️ 准备和上传数据集

Ultralytics Platform 数据集支持 [YOLO26](https://docs.ultralytics.com/models/yolo26)、[YOLO11](https://docs.ultralytics.com/models/yolo11)、[YOLOv8](https://docs.ultralytics.com/models/yolov8) 和 [YOLOv5](https://docs.ultralytics.com/models/yolov5) 使用的 YOLO 任务体系：[目标检测](https://docs.ultralytics.com/tasks/detect)、[实例分割](https://docs.ultralytics.com/tasks/segment)、[姿态估计](https://docs.ultralytics.com/tasks/pose)、[定向目标检测](https://docs.ultralytics.com/tasks/obb) 和 [图像分类](https://docs.ultralytics.com/tasks/classify)。

- 可上传最大 50 MB 图像、最大 1 GB 视频，以及 ZIP、TAR、`.tar.gz`、`.tgz` 或 NDJSON 数据集文件。
- Platform 会自动校验上传内容、缩放大图、生成缩略图、解析标签并计算统计信息。
- 可在 grid、compact 和 table 视图中查看标注叠加层，并使用 split、标签、类别和文件名过滤。
- 支持使用手动工具、骨架模板、SAM Smart Annotation 和 YOLO 自动标注处理 detect、segment、pose、OBB 和 classify 数据集。
- 请查看 [Ultralytics 数据集文档](https://docs.ultralytics.com/datasets) 了解数据集最佳实践。
- 通过 [数据收集与标注指南](https://docs.ultralytics.com/guides/data-collection-and-annotation) 学习数据准备和标注流程。
- 探索 [COCO](https://docs.ultralytics.com/datasets/detect/coco)、[LVIS](https://docs.ultralytics.com/datasets/detect/lvis) 和 [ImageNet](https://docs.ultralytics.com/datasets/classify/imagenet) 等开源数据集。

### 数据集准备

进入 Platform 的 **Annotate** 并点击 **New Dataset**，或将文件拖放到 Home dashboard 的 Datasets 卡片中。建议上传采用标准 YOLO 结构的 ZIP 或 TAR 压缩包：

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

可以使用以下命令压缩数据集：

```bash
# 压缩数据集目录以便上传
cd my-dataset && zip -r ../my-dataset.zip .
```

请参考 [example_datasets/coco8.zip](./example_datasets/coco8.zip) 和本地 `example_datasets/` 目录中的小型 YOLO 格式压缩包示例。更多数据集格式说明，请参阅 [Ultralytics 数据集文档](https://docs.ultralytics.com/datasets)。Platform 也支持 COCO JSON 标注、Ultralytics NDJSON 导出、分类文件夹布局、视频，以及用于在线标注的原始未标注图像。

<p align="center">
  <img width="100%" src="https://cdn.jsdelivr.net/gh/ultralytics/assets@main/docs/platform/platform-quickstart-upload-dialog.avif" alt="Ultralytics Platform upload dialog">
</p>

### YAML 规范

数据集 YAML 文件应使用标准 [YOLO 数据集格式](https://docs.ultralytics.com/guides/model-training-tips) 约定定义数据路径和类别名称。详细说明请参考 [模型训练技巧指南](https://docs.ultralytics.com/guides/model-training-tips)。

```yaml
# 自定义数据集 YAML 配置示例
path: .
train: train/images
val: val/images
test: # 测试图像（可选）

# 类别标签
names:
  0: person
  1: bicycle
  2: car
  3: motorcycle
  # 可根据需要添加更多类别
```

上传后，Platform 会检查图像和标签有效性、生成预览、计算类别和尺寸统计信息，并让 ready 状态的数据集可用于标注、云端训练，以及通过 `ul://` 数据集 URI 进行本地训练。

## 🚀 训练模型

使用 [Ultralytics Platform](https://platform.ultralytics.com) 可在云端 GPU 上训练 YOLO 模型、在项目中比较实验、管理训练好的 `.pt` 模型，并流式同步本地训练指标。本仓库会在迁移窗口内继续提供旧版 HUB 支持，但新的训练工作应从 Platform 开始。

- 在项目中点击 **Train Model**，选择数据集、官方 YOLO 模型或您自己的已训练模型，设置 epochs 和 image size，然后选择 GPU。
- 训练运行时可查看实时图表、控制台日志和系统指标。
- 训练完成后，最佳 checkpoint 可用于下载、导出、浏览器预测和部署。
- 使用 `ultralytics>=8.4.35` 和 API key，可在本地训练并将指标流式同步到 Platform。
- 阅读 [模型训练技巧](https://docs.ultralytics.com/guides/model-training-tips) 了解最佳实践。
- 学习 [超参数调优](https://docs.ultralytics.com/guides/hyperparameter-tuning) 以优化结果。
- 探索 [实验跟踪集成](https://docs.ultralytics.com/integrations/mlflow)，支持可复现研究。

<p align="center">
  <img width="100%" src="https://cdn.jsdelivr.net/gh/ultralytics/assets@main/docs/platform/platform-quickstart-training-dialog-cloud-tab.avif" alt="Ultralytics Platform cloud training dialog">
</p>

```bash
pip install -U ultralytics
export ULTRALYTICS_API_KEY="YOUR_API_KEY"

yolo train model=yolo26n.pt data=coco.yaml epochs=100 project=username/my-project name=experiment-1
```

Platform 数据集也可通过 `ul://` URI 直接用于训练任务：

```bash
yolo train model=yolo26n.pt data=ul://username/datasets/my-dataset epochs=100 project=username/my-project name=experiment-1
```

## 🌐 部署到现实世界

训练完成后，可使用 Platform 在浏览器中测试模型、导出生产格式并部署专用端点。Platform 支持浏览器预测、监控部署、43 个全球部署区域、scale-to-zero，以及 17 种导出格式，包括 [ONNX](https://onnx.ai/)、[TensorRT](https://developer.nvidia.com/tensorrt)、[CoreML](https://developer.apple.com/documentation/coreml)、[TFLite](https://www.tensorflow.org/lite)、[OpenVINO](https://docs.openvino.ai/latest/index.html) 和 TorchScript。

- 打开模型 **Predict** 标签页即可上传图像、调整 confidence、IoU 和 image size，并在画布上查看预测结果。
- 在 **Deploy** 标签页中，从延迟地图选择区域并创建专用 HTTPS 端点。
- 可在 Platform 中监控端点健康状态、请求日志、P95 延迟、错误率和用量指标。
- Platform 会为您的端点生成可直接使用的 Python、JavaScript 和 cURL 示例。
- 了解适用于边缘设备和云端的 [模型部署选项](https://docs.ultralytics.com/guides/model-deployment-options)。
- 探索 [OpenVINO 延迟与吞吐优化](https://docs.ultralytics.com/guides/optimizing-openvino-latency-vs-throughput-modes)，用于实时推理。
- 下载 [Ultralytics App](https://www.ultralytics.com/app-install)，即可在 [iOS](https://apps.apple.com/app/ultralytics/id1583935240) 或 [Android](https://play.google.com/store/apps/details?id=com.ultralytics.ultralytics_app) 移动设备上运行模型。

<p align="center">
  <img width="100%" src="https://cdn.jsdelivr.net/gh/ultralytics/assets@main/docs/platform/platform-deploy-tab-region-map-with-latency.avif" alt="Ultralytics Platform deployment region map">
</p>

## ❓ 有问题或疑问？

新的工作请从 [Ultralytics Platform](https://platform.ultralytics.com) 和 [Platform 快速开始](https://docs.ultralytics.com/platform/quickstart) 开始。如果您需要在 2026 年 7 月底 HUB 下线前迁移现有工作，请创建 Platform 账号，并在 **Settings > Integrations > Ultralytics HUB** 粘贴 HUB API key，以迁移数据集和模型。

- 请使用本仓库的 **Issues** 页面提交旧版 HUB 仓库支持和迁移问题。
- 访问 [Ultralytics 帮助中心](https://docs.ultralytics.com/help/FAQ) 获取快速答案。
- 浏览 [Ultralytics 帮助中心](https://docs.ultralytics.com/help) 了解故障排除和最佳实践。
- 浏览 [Ultralytics Platform 文档](https://docs.ultralytics.com/platform) 了解当前工作流。
- 加入 [Ultralytics Discord 社区](https://discord.com/invite/ultralytics) 参与实时讨论。

## 贡献

我们欢迎能够改进旧版迁移支持、澄清 Platform 入门流程或修复仓库示例的贡献。请参阅 [贡献指南](https://docs.ultralytics.com/help/contributing) 了解参与方式。感谢所有贡献者！

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
