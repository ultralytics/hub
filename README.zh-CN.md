<div align="center">
  <p>
    <a href="https://platform.ultralytics.com/" target="_blank">
      <img width="100%" src="https://cdn.jsdelivr.net/gh/ultralytics/assets@main/docs/platform/dataset-screenshot.avif" alt="Ultralytics Platform dataset interface"></a>
  </p>

[中文](https://docs.ultralytics.com/zh/platform) | [한국어](https://docs.ultralytics.com/ko/platform) | [日本語](https://docs.ultralytics.com/ja/platform) | [Русский](https://docs.ultralytics.com/ru/platform) | [Deutsch](https://docs.ultralytics.com/de/platform) | [Français](https://docs.ultralytics.com/fr/platform) | [Español](https://docs.ultralytics.com/es/platform) | [Português](https://docs.ultralytics.com/pt/platform) | [Türkçe](https://docs.ultralytics.com/tr/platform) | [Tiếng Việt](https://docs.ultralytics.com/vi/platform) | [العربية](https://docs.ultralytics.com/ar/platform)

[![Ultralytics Actions](https://github.com/ultralytics/hub/actions/workflows/ci.yml/badge.svg)](https://github.com/ultralytics/hub/actions/workflows/ci.yml)
[![Ultralytics Discord](https://img.shields.io/discord/1089800235347353640?logo=discord&logoColor=white&label=Discord&color=blue)](https://discord.com/invite/ultralytics)
[![Ultralytics Forums](https://img.shields.io/discourse/users?server=https%3A%2F%2Fcommunity.ultralytics.com&logo=discourse&label=Forums&color=blue)](https://community.ultralytics.com/)
[![Ultralytics Reddit](https://img.shields.io/reddit/subreddit-subscribers/ultralytics?style=flat&logo=reddit&logoColor=white&label=Reddit&color=blue)](https://reddit.com/r/ultralytics)
<a href="https://colab.research.google.com/github/ultralytics/hub/blob/main/hub.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a>

👋 来自 [Ultralytics](https://www.ultralytics.com/) 团队的问候！[Ultralytics HUB](https://hub.ultralytics.com/) 正在逐步停用，并将于 2026 年 7 月底完成下线。新项目请使用全新的 [Ultralytics Platform](https://platform.ultralytics.com/)，这是面向计算机视觉的端到端平台，覆盖数据准备、图像标注、YOLO 模型训练、生产格式导出和全球多区域端点部署 🚀！

请创建 [Platform 账号](https://platform.ultralytics.com/) 开始新的工作流。现有 HUB 用户在创建账号后，可进入 **Settings > Integrations > Ultralytics HUB** 粘贴 HUB API key，直接迁移所有 HUB 数据集和模型。欢迎查阅 [Ultralytics Platform 文档](https://docs.ultralytics.com/platform) 了解详细指南，在 [GitHub Issues](https://github.com/ultralytics/hub/issues/new/choose) 提交旧版 HUB 仓库支持问题，并加入我们的 [Discord 社区](https://discord.com/invite/ultralytics) 参与讨论！

<br>
<div align="center">
  <a href="https://github.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-github.png" width="2%" alt="Ultralytics GitHub"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="2%">
  <a href="https://www.linkedin.com/company/ultralytics/"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-linkedin.png" width="2%" alt="Ultralytics LinkedIn"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="2%">
  <a href="https://twitter.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-twitter.png" width="2%" alt="Ultralytics Twitter"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="2%">
  <a href="https://www.youtube.com/ultralytics?sub_confirmation=1"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-youtube.png" width="2%" alt="Ultralytics YouTube"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="2%">
  <a href="https://www.tiktok.com/@ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-tiktok.png" width="2%" alt="Ultralytics TikTok"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="2%">
  <a href="https://ultralytics.com/bilibili"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-bilibili.png" width="2%" alt="Ultralytics BiliBili"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="2%">
  <a href="https://discord.com/invite/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-discord.png" width="2%" alt="Ultralytics Discord"></a>
</div>
</div>

## 🗂️ 准备和上传数据集

Ultralytics Platform 数据集格式与 [YOLO11](https://docs.ultralytics.com/models/yolo11)、[YOLOv8](https://docs.ultralytics.com/models/yolov8) 和 [YOLOv5](https://docs.ultralytics.com/models/yolov5) 完全兼容。它们采用统一的结构和标签规范，支持 [目标检测](https://docs.ultralytics.com/tasks/detect)、[实例分割](https://docs.ultralytics.com/tasks/segment)、[姿态估计](https://docs.ultralytics.com/tasks/pose)、[定向目标检测](https://docs.ultralytics.com/tasks/obb) 和 [图像分类](https://docs.ultralytics.com/tasks/classify) 等任务。

### 数据集准备

请确保您的数据集根目录下包含描述数据集的 YAML 文件。准备好后，将整个目录压缩为 ZIP 文件，便于上传至 [Ultralytics Platform](https://platform.ultralytics.com/)。YAML 文件、其所在目录及压缩包需保持同名。

例如，若您的数据集名为 'coco8'，请参考 [ultralytics/hub/example_datasets/coco8.zip](./example_datasets/coco8.zip) 的结构，在 `coco8/` 目录下放置 `coco8.yaml` 文件。然后使用如下命令将其压缩：

```bash
# 压缩数据集目录以便上传
zip -r coco8.zip coco8
```

建议浏览 [example_datasets/coco8.zip](./example_datasets/coco8.zip) 获取自定义数据集构建的实际案例。更多数据集格式说明，请参阅 [Ultralytics 数据集文档](https://docs.ultralytics.com/datasets)。

<p align="center">
<img width="100%" src="https://raw.githubusercontent.com/ultralytics/assets/main/docs/hub/datasets/hub_upload_dataset_1.jpg" title="COCO8 Example Dataset Structure" />
</p>

### YAML 规范

数据集 YAML 文件遵循 YOLO 格式规范。详细说明请参考 [训练自定义数据指南](https://docs.ultralytics.com/guides/model-training-tips)。

```yaml
# 自定义数据集 YAML 配置示例
path: ../datasets/coco8 # 数据集根目录（相对或绝对路径）
train: images/train # 训练图像（相对 'path'）8 张图像
val: images/val # 验证图像（相对 'path'）8 张图像
test: # 测试图像（可选）

# 类别标签
names:
  0: person
  1: bicycle
  2: car
  3: motorcycle
  # 可根据需要添加更多类别
```

登录 [Ultralytics Platform](https://platform.ultralytics.com/)，前往 ['Datasets' 页面](https://docs.ultralytics.com/platform)，点击 'Upload Dataset' 上传您的 ZIP 数据集。上传后，您可在同一工作流中预览、分析、标注并训练数据集。

<p align="center">
  <img width="100%" alt="Ultralytics Platform Dataset Upload Interface" src="https://user-images.githubusercontent.com/26833433/216763338-9a8812c8-a4e5-4362-8102-40dad7818396.png">
</p>

## 🚀 训练模型

使用 [Ultralytics Platform](https://platform.ultralytics.com/) 可在云端 GPU 上训练 YOLO 模型、流式同步远程训练指标、在项目中比较实验结果，并集中管理训练好的 `.pt` 模型。旧版 HUB notebook 工作流会在 HUB 下线过渡期内继续保留给现有用户，但新的训练工作应从 Platform 开始。

<a href="https://colab.research.google.com/github/ultralytics/hub/blob/main/hub.ipynb" target="_blank">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" />
</a>

## 🌐 部署到现实世界

利用 [Ultralytics Platform](https://platform.ultralytics.com/) 或 [导出模式](https://docs.ultralytics.com/modes/export)，可将训练好的模型部署到生产环境。Platform 支持浏览器预测、监控部署、全球专用端点，以及 17+ 种导出格式，包括 [TensorFlow](https://www.tensorflow.org/)、[ONNX](https://onnx.ai/)、[OpenVINO](https://docs.openvino.ai/latest/index.html)、[TensorRT](https://developer.nvidia.com/tensorrt)、[CoreML](https://developer.apple.com/documentation/coreml)、[PaddlePaddle](https://www.paddlepaddle.org.cn/en) 等。下载 [Ultralytics App](https://www.ultralytics.com/app-install)，即可在 [iOS](https://apps.apple.com/app/ultralytics/id1583935240) 或 [Android](https://play.google.com/store/apps/details?id=com.ultralytics.ultralytics_app) 移动设备上直接运行您的模型！探索更多适用于边缘设备和云平台的 [模型部署选项](https://docs.ultralytics.com/guides/model-deployment-options)。

## ❓ 有问题或疑问？

新项目请从 [Ultralytics Platform](https://platform.ultralytics.com/) 和 [Platform 文档](https://docs.ultralytics.com/platform) 开始。如果您需要在 2026 年 7 月底 HUB 下线前迁移现有工作，请创建 Platform 账号，并在 **Settings > Integrations > Ultralytics HUB** 粘贴 HUB API key，即可迁移所有 HUB 数据集和模型。[GitHub Issues](https://github.com/ultralytics/hub/issues) 可用于旧版 HUB 仓库支持和迁移问题反馈。

## 贡献

我们欢迎您的贡献！❤️ 请参阅 [贡献指南](https://docs.ultralytics.com/help/contributing) 了解参与方式。感谢所有为 Ultralytics 生态做出贡献的开发者！

[![Ultralytics open-source contributors](https://raw.githubusercontent.com/ultralytics/assets/main/im/image-contributors.png)](https://github.com/ultralytics/ultralytics/graphs/contributors)

<br>
<div align="center">
  <a href="https://github.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-github.png" width="3%" alt="Ultralytics GitHub"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%">
  <a href="https://www.linkedin.com/company/ultralytics/"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-linkedin.png" width="3%" alt="Ultralytics LinkedIn"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%">
  <a href="https://twitter.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-twitter.png" width="3%" alt="Ultralytics Twitter"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%">
  <a href="https://www.youtube.com/ultralytics?sub_confirmation=1"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-youtube.png" width="3%" alt="Ultralytics YouTube"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%">
  <a href="https://www.tiktok.com/@ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-tiktok.png" width="3%" alt="Ultralytics TikTok"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%">
  <a href="https://ultralytics.com/bilibili"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-bilibili.png" width="3%" alt="Ultralytics BiliBili"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%">
  <a href="https://discord.com/invite/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-discord.png" width="3%" alt="Ultralytics Discord"></a>
</div>
