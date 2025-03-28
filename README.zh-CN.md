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

👋 来自 [Ultralytics](https://www.ultralytics.com/) 团队的问候！过去几个月我们一直努力工作，推出了 [Ultralytics HUB](https://www.ultralytics.com/hub)，这是一个全新的平台，用于在一个中心位置训练和部署您所有的 [Ultralytics YOLOv5](https://docs.ultralytics.com/models/yolov5/) 和 [YOLOv8](https://docs.ultralytics.com/models/yolov8/) 🚀 模型！

我们希望这里的资源能帮助您充分利用 Ultralytics HUB。请浏览 [Ultralytics HUB 文档](https://docs.ultralytics.com/hub/) 获取详细信息，在 [GitHub](https://github.com/ultralytics/hub/issues/new/choose) 上提出问题以获得支持，并加入我们的 [Discord 社区](https://discord.com/invite/ultralytics) 进行提问和讨论！

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

## 🗂️ 上传数据集

Ultralytics HUB 数据集与 [YOLOv5](https://github.com/ultralytics/yolov5) 和 [YOLOv8](https://github.com/ultralytics/ultralytics) 使用的格式保持一致。它们遵循相同的结构和标签约定，确保为[目标检测](https://docs.ultralytics.com/tasks/detect/)、[分割](https://docs.ultralytics.com/tasks/segment/)和[分类](https://docs.ultralytics.com/tasks/classify/)任务提供无缝体验。

### 数据集准备

确保描述您数据集的 YAML 文件放置在数据集的根目录中，如下所示。放置好后，将该目录压缩以便上传到 [Ultralytics HUB](https://www.ultralytics.com/hub)。数据集 YAML 文件、其目录以及 zip 压缩文件应具有完全相同的名称。

例如，对于名为 'coco8' 的数据集，如 [ultralytics/hub/example_datasets/coco8.zip](./example_datasets/coco8.zip) 所示，在 `coco8/` 目录中包含一个 `coco8.yaml` 文件。使用类似以下的命令将此目录压缩成 `coco8.zip` 以供上传：

```bash
# 压缩数据集目录以上传
zip -r coco8.zip coco8
```

浏览提供的 [example_datasets/coco8.zip](./example_datasets/coco8.zip) 以获取有关构建自定义数据集的见解。您可以在我们的[数据集文档](https://docs.ultralytics.com/datasets/)中找到有关数据集格式的更多信息。

<p align="center">
<img width="70%" src="https://raw.githubusercontent.com/ultralytics/assets/main/docs/hub/datasets/hub_upload_dataset_1.jpg" title="COCO8 Example Dataset Structure" />
</p>

### YAML 规范

数据集 YAML 遵循既定的 YOLOv5 和 YOLOv8 格式。有关详细说明，请参阅[训练自定义数据指南](https://docs.ultralytics.com/guides/model-training-tips/)。

```yaml
# 自定义数据集的 YAML 配置示例
path: ../datasets/coco8 # 数据集根目录（可以是相对路径或绝对路径）
train: images/train # 训练图像（相对于 'path'）8 张图像
val: images/val # 验证图像（相对于 'path'）8 张图像
test: # 测试图像（可选）

# 类别标签
names:
  0: person
  1: bicycle
  2: car
  3: motorcycle
  # 根据需要添加更多类别
```

登录 [Ultralytics HUB](https://www.ultralytics.com/hub)，导航到 ['Datasets' 选项卡](https://docs.ultralytics.com/hub/datasets/)，然后选择 'Upload Dataset' 来上传您的压缩数据集。这使您能够在训练 YOLOv5 或 YOLOv8 模型之前扫描和查看您的数据集。

<p align="center">
  <img width="100%" alt="Ultralytics HUB Dataset Upload Interface" src="https://user-images.githubusercontent.com/26833433/216763338-9a8812c8-a4e5-4362-8102-40dad7818396.png">
</p>

## 🚀 训练模型

连接到 Ultralytics HUB notebook 并使用您的 API 密钥开始[模型训练](https://docs.ultralytics.com/modes/train/)！Ultralytics HUB 提供简化的[云训练](https://docs.ultralytics.com/hub/cloud-training/)选项，使您无需受本地硬件限制即可轻松训练模型。

<a href="https://colab.research.google.com/github/ultralytics/hub/blob/main/hub.ipynb" target="_blank">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" />
</a>

## 🌐 部署到现实世界

使用[导出模式](https://docs.ultralytics.com/modes/export/)将您训练好的模型转换为各种格式，包括 [TensorFlow](https://www.tensorflow.org/)、[ONNX](https://onnx.ai/)、[OpenVINO](https://docs.openvino.ai/latest/index.html)、[CoreML](https://developer.apple.com/documentation/coreml)、[PaddlePaddle](https://www.paddlepaddle.org.cn/en) 等（支持 13+ 种格式）。通过下载 [Ultralytics App](https://www.ultralytics.com/app-install)，直接在您的 [iOS](https://apps.apple.com/app/ultralytics/id1583935240) 或 [Android](https://play.google.com/store/apps/details?id=com.ultralytics.ultralytics_app) 移动设备上运行您的模型！探索适用于边缘设备和云平台的各种[模型部署选项](https://docs.ultralytics.com/guides/model-deployment-options/)。

## ❓ 有问题或疑问？

对于刚开始使用 [Ultralytics HUB](https://www.ultralytics.com/hub) 的用户，[GitHub Issues](https://github.com/ultralytics/hub/issues) 选项卡是您获取支持和报告错误的主要资源。点击 'New Issue' 按钮，分享您的想法、问题或报告遇到的困难。我们的目标是通过提供有价值的解决方案和持续改进来提升您的体验！😃

## 贡献

我们欢迎贡献！❤️ 请参阅我们的[贡献指南](https://docs.ultralytics.com/help/contributing/)了解如何参与的更多详情。感谢所有贡献者！

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
