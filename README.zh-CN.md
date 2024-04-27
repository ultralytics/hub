<div align="center">
  <p>
    <a href="https://bit.ly/ultralytics_hub" target="_blank">
      <img width="100%" src="https://github.com/ultralytics/assets/raw/main/im/ultralytics-hub.png"></a>
  </p>

[中文](https://docs.ultralytics.com/zh/hub/) | [한국어](https://docs.ultralytics.com/ko/hub/) | [日本語](https://docs.ultralytics.com/ja/hub/) | [Русский](https://docs.ultralytics.com/ru/hub/) | [Deutsch](https://docs.ultralytics.com/de/hub/) | [Français](https://docs.ultralytics.com/fr/hub/) | [Español](https://docs.ultralytics.com/es/hub/) | [Português](https://docs.ultralytics.com/pt/hub/) | [Türkçe](https://docs.ultralytics.com/tr/hub/) | [Tiếng Việt](https://docs.ultralytics.com/vi/hub/) | [हिन्दी](https://docs.ultralytics.com/hi/hub/) | [العربية](https://docs.ultralytics.com/ar/hub/)

<a href="https://github.com/ultralytics/hub/actions/workflows/ci.yaml"><img src="https://github.com/ultralytics/hub/actions/workflows/ci.yaml/badge.svg" alt="CI CPU"></a> <a href="https://colab.research.google.com/github/ultralytics/hub/blob/main/hub.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a> <a href="https://ultralytics.com/discord"><img alt="Discord" src="https://img.shields.io/discord/1089800235347353640?logo=discord&logoColor=white&label=Discord&color=blue"></a>

👋 欢迎来自 [Ultralytics](https://ultralytics.com/) 团队的问候！在过去的几个月里，我们一直在努力推出 [Ultralytics HUB](https://bit.ly/ultralytics_hub)，这是一个全新的网络工具，可让您在一个地方训练和部署所有的 YOLOv5 和 YOLOv8 🚀 模型！

我们希望这里的资源能帮助您充分利用 HUB。请浏览 HUB 的[文档](https://docs.ultralytics.com/)了解详情，若需要支持，请在 [GitHub](https://github.com/ultralytics/hub/issues/new/choose) 上提出问题，加入我们的 [Discord](https://ultralytics.com/discord) 社区参与问题讨论！

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

## 🗂️ 1. 上传数据集

Ultralytics HUB 的数据集格式与 [YOLOv5](https://github.com/ultralytics/yolov5) 和 [YOLOv8](https://github.com/ultralytics/ultralytics) 使用的格式相符，遵循相同的结构和标记约定，确保无缝体验。

### 数据集准备：

确保将描述您的数据集的 YAML 文件放在数据集的根目录下，如下所示。放置好后，将目录压缩并上传到 [Ultralytics HUB](https://bit.ly/ultralytics_hub)。数据集的 YAML 文件、其目录和压缩文件应具有相同的名称。

例如，对于名为 'coco8' 的数据集，如 [ultralytics/hub/example_datasets/coco8.zip](./example_datasets/coco8.zip) 所示，在 `coco8/` 目录内包含一个 `coco8.yaml`。使用以下命令将其压缩为 `coco8.zip` 以进行上传：

```bash
# 压缩数据集目录以供上传
zip -r coco8.zip coco8
```

浏览提供的 [example_datasets/coco8.zip](./example_datasets/coco8.zip) 以获得关于构建自定义数据集的洞察。

<p align="center">
<img width="80%" src="https://raw.githubusercontent.com/ultralytics/assets/main/docs/hub/datasets/hub_upload_dataset_1.jpg" title="COCO8 Example Dataset" />
</p>

### YAML 规范：

数据集 YAML 遵循已建立的 YOLOv5 和 YOLOv8 格式。有关详尽的说明，请参阅 [自定义数据训练教程](https://docs.ultralytics.com/yolov5/tutorials/train_custom_data/)。

```yaml
# 自定义数据集的 YAML 配置示例
path: # 数据集根目录（留空以适应 HUB）
train: images/train # 训练图像（相对于 'path'）8张图像
val: images/val # 验证图像（相对于 'path'）8张图像
test: # 测试图像（可选）

# 类别标签
names:
  0: person
  1: bicycle
  2: car
  3: motorcycle
  # 根据需要添加更多类别
```

通过登录、导航至“数据集”标签页并选择“上传数据集”，将您的压缩数据集上传到 [Ultralytics HUB](https://bit.ly/ultralytics_hub)，这样您就可以在训练 YOLOv5 或 YOLOv8 模型之前查看您的数据集。

<p align="center">
  <img width="100%" alt="HUB 数据集上传" src="https://user-images.githubusercontent.com/26833433/216763338-9a8812c8-a4e5-4362-8102-40dad7818396.png">
</p>

## 🚀 2. 训练模型

连接到 Ultralytics HUB 笔记本并使用您的模型 API 密钥开始模型训练！

<a href="https://colab.research.google.com/github/ultralytics/hub/blob/main/hub.ipynb" target="_blank">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" />
</a>

## 🌐 3. 部署到现实世界

将您的模型转换为 TensorFlow、ONNX、OpenVINO、CoreML、Paddle 等 13 种不同格式。通过下载 [Ultralytics App](https://ultralytics.com/app_install)，直接在您的 [iOS](https://apps.apple.com/xk/app/ultralytics/id1583935240) 或 [Android](https://play.google.com/store/apps/details?id=com.ultralytics.ultralytics_app) 移动设备上操作您的模型！

## ❓ 有问题或疑问？

对于刚开始 [Ultralytics HUB](https://bit.ly/ultralytics_hub) 之旅的人来说，[问题](https://github.com/ultralytics/hub/issues) 标签是您寻求支持的首选资源。点击“新建问题”按钮，分享您的想法或问题。我们的目标是通过宝贵的解决方案和改进来增强您的体验！ 😃

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
