<div align="center">
  <p>
    <a href="https://bit.ly/ultralytics_hub" target="_blank">
      <img width="100%" src="https://github.com/ultralytics/assets/raw/main/im/ultralytics-hub.png"></a>
  </p>

[中文](https://docs.ultralytics.com/zh/) | [한국어](https://docs.ultralytics.com/ko/) | [日本語](https://docs.ultralytics.com/ja/) | [Русский](https://docs.ultralytics.com/ru/) | [Deutsch](https://docs.ultralytics.com/de/) | [Français](https://docs.ultralytics.com/fr/) | [Español](https://docs.ultralytics.com/es/) | [Português](https://docs.ultralytics.com/pt/) | [हिन्दी](https://docs.ultralytics.com/hi/) | [العربية](https://docs.ultralytics.com/ar/)

<a href="https://github.com/ultralytics/hub/actions/workflows/ci.yaml">
    <img src="https://github.com/ultralytics/hub/actions/workflows/ci.yaml/badge.svg" alt="CI CPU"></a>
  <a href="https://colab.research.google.com/github/ultralytics/hub/blob/master/hub.ipynb">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a>
</div>
<br>

👋 欢迎来到 [Ultralytics](https://ultralytics.com/) 团队！在过去的几个月里，我们一直在努力推出 [Ultralytics HUB](https://bit.ly/ultralytics_hub)，一个新的网络工具，用于从一个地方训练和部署您所有的 YOLOv5 和 YOLOv8 🚀 模型！

我们希望这里的资源能帮助您充分利用 HUB。请浏览 HUB 的<a href="https://docs.ultralytics.com/">文档</a>了解详细信息，在 <a href="https://github.com/ultralytics/hub/issues/new/choose">GitHub</a> 上提出问题寻求支持，并加入我们的 <a href="https://ultralytics.com/discord">Discord</a> 社区进行问题讨论和交流！

## 🗂️ 1. 上传数据集

Ultralytics HUB 数据集与 [YOLOv5](https://github.com/ultralytics/yolov5) 和 [YOLOv8](https://github.com/ultralytics/ultralytics) 使用的格式一致。它们遵循相同的结构和标记规范，确保体验的无缝对接。

### 数据集准备：

确保将描述您的数据集的 YAML 文件放在数据集的根目录下，如下所示。放置好后，将目录压缩以上传到 [Ultralytics HUB](https://bit.ly/ultralytics_hub/)。数据集 YAML、其目录和 zip 文件应该全部具有相同的名称。

例如，对于名为 'coco8' 的数据集，如 [ultralytics/hub/example_datasets/coco8.zip](./example_datasets/coco8.zip) 所示，包含一个 `coco8.yaml` 文件在 `coco8/` 目录中。将其压缩成 `coco8.zip` 以使用以下命令上传：

```bash
# 压缩数据集目录以便上传
zip -r coco8.zip coco8
```

探索提供的 [example_datasets/coco8.zip](./example_datasets/coco8.zip) 以获取构建自定义数据集的见解。

<p align="center">
<img width="80%" src="https://user-images.githubusercontent.com/26833433/201424843-20fa081b-ad4b-4d6c-a095-e810775908d8.png" title="COCO8">
</p>

### YAML 规范：

数据集 YAML 遵循已建立的 YOLOv5 和 YOLOv8 格式。有关详尽说明，请参阅 [自定义数据训练教程](https://docs.ultralytics.com/yolov5/tutorials/train_custom_data/)。

```yaml
# 自定义数据集的 YAML 配置示例
path: # 数据集根目录（集成 HUB 时留空）
train: images/train # 训练图片（相对于 'path'）8张图片
val: images/val # 验证图片（相对于 'path'）8张图片
test: # 测试图片（可选）

# 类别标签
names:
  0: person
  1: bicycle
  2: car
  3: motorcycle
  # 根据需要添加更多类别
```

通过登录 [Ultralytics HUB](https://bit.ly/ultralytics_hub)，导航到 '数据集' 标签页，并选择 '上传数据集'，将您的压缩数据集上传。这样您就可以在训练 YOLOv5 或 YOLOv8 模型之前预览并查看您的数据集。

<p align="center">
  <img width="100%" alt="HUB 数据集上传" src="https://user-images.githubusercontent.com/26833433/216763338-9a8812c8-a4e5-4362-8102-40dad7818396.png">
</p>

## 🚀 2. 训练模型

连接到 Ultralytics HUB 笔记本并使用您的模型 API 密钥开始训练模型！

<a href="https://colab.research.google.com/github/ultralytics/hub/blob/master/hub.ipynb" target="_blank">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="在 Colab 中打开" />
</a>

## 🌐 3. 部署到现实世界

将您的模型转换为 TensorFlow、ONNX、OpenVINO、CoreML、Paddle 等 13 种不同的格式。通过下载 [Ultralytics 应用程序](https://ultralytics.com/app_install)，直接在您的 [iOS](https://apps.apple.com/xk/app/ultralytics/id1583935240) 或 [Android](https://play.google.com/store/apps/details?id=com.ultralytics.ultralytics_app) 移动设备上操作模型！

## ❓ 有问题或疑问？

对于刚开始 [Ultralytics HUB](https://bit.ly/ultralytics_hub) 之旅的用户，[问题](https://github.com/ultralytics/hub/issues)标签页是您寻求支持的首选资源。点击 '新建问题' 按钮并分享您的想法或问题。我们的目标是通过提供宝贵的解决方案和改进来增强您的体验！😃
