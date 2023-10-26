<div align="center">
  <p>
    <a href="https://hub.ultralytics.com" target="_blank">
      <img width="100%" src="https://github.com/ultralytics/assets/raw/main/im/ultralytics-hub.png"></a>
  </p>

[English](README.md) | [简体中文](README.zh-CN.md)

<a href="https://github.com/ultralytics/hub/actions/workflows/ci.yaml">
    <img src="https://github.com/ultralytics/hub/actions/workflows/ci.yaml/badge.svg" alt="CI CPU"></a>
  <a href="https://colab.research.google.com/github/ultralytics/hub/blob/master/hub.ipynb">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a>
</div>
<br>

👋 来自 [Ultralytics](https://ultralytics.com/) 团队的问候！在过去的几个月里，我们一直在努力推出 [Ultralytics HUB](https://bit.ly/ultralytics_hub)，一个用于从一个地方训练和部署所有您的 YOLOv5 和 YOLOv8 🚀模型的新网络工具！

我们希望这里的资源能帮助您充分利用 HUB。请浏览 HUB 的<a href="https://docs.ultralytics.com/">文档</a>以获取详细信息，在 <a href="https://github.com/ultralytics/hub/issues/new/choose">GitHub</a> 上提出问题以获取支持，并加入我们的 <a href="https://ultralytics.com/discord">Discord</a> 社区进行问题和讨论！

<br>

## 1. 上传数据集

Ultralytics HUB 数据集就像 [YOLOv5](https://github.com/ultralytics/yolov5) 和 [YOLOv8](https://github.com/ultralytics/ultralytics) 🚀数据集一样，它们使用相同的结构和相同的标签格式以保持一切简单。

当您将数据集上传到 Ultralytics HUB 时，请确保**将您的数据集 YAML 放在数据集根目录内**，如下面的示例所示，然后压缩以上传到 [https://hub.ultralytics.com](https://hub.ultralytics.com/)。您的**数据集 YAML、目录和 zip** 应该都有相同的名称。例如，如果您的数据集叫做 'coco8'，如我们的示例 [ultralytics/hub/example_datasets/coco8.zip](./example_datasets/coco8.zip)，那么您应该在您的 `coco8/` 目录内有一个 `coco8.yaml`，然后压缩为 `coco8.zip` 以进行上传：

```bash
zip -r coco8.zip coco8
```

此存储库中的 [example_datasets/coco8.zip](./example_datasets/coco8.zip) 数据集可以下载和解压缩，以准确地了解如何构造您的自定义数据集。

<p align="center">
<img width="80%" src="https://user-images.githubusercontent.com/26833433/201424843-20fa081b-ad4b-4d6c-a095-e810775908d8.png" title="COCO8" />
</p>

数据集 YAML 是标准的 YOLOv5 和 YOLOv8 YAML 格式。请参阅 [YOLOv5 和 YOLOv8 训练自定义数据教程](https://docs.ultralytics.com/yolov5/tutorials/train_custom_data/) 以获取全部详细信息。

```yaml
# 训练/验证/测试集为 1）目录：path/to/imgs，2）文件：path/to/imgs.txt，或 3）列表：[path/to/imgs1, path/to/imgs2, ..]
path:  # 数据集根目录（HUB 为空）
train: images/train  # 训练图像（相对于 'path'）8 张图像
val: images/val  # 验证图像（相对于 'path'）8 张图像
test:  # 测试图像（可选）

# 类别
names:
  0: 人
  1: 自行车
  2: 汽车
  3: 摩托车
  ...
```

在压缩您的数据集后，登录到 [Ultralytics HUB](https://bit.ly/ultralytics_hub) 并点击数据集选项卡。 点击 '上传数据集' 以上传、扫描和可视化您的新数据集，然后在其上训练新的 YOLOv5 或 YOLOv8 模型！

<img width="100%" alt="HUB 数据集上传" src="https://user-images.githubusercontent.com/26833433/216763338-9a8812c8-a4e5-4362-8102-40dad7818396.png">

## 2. 训练模型

连接到 Ultralytics HUB 笔记本，并使用您的模型 API 密钥开始训练！

<a href="https://colab.research.google.com/github/ultralytics/hub/blob/master/hub.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="在 Colab 中打开"></a>

## 3. 部署到现实世界

将您的模型导出到 13 种不同的格式，包括 TensorFlow、ONNX、OpenVINO、CoreML、Paddle 等等。通过下载 [Ultralytics 应用](https://ultralytics.com/app_install)，直接在您的 [iOS](https://apps.apple.com/xk/app/ultralytics/id1583935240) 或 [Android](https://play.google.com/store/apps/details?id=com.ultralytics.ultralytics_app) 移动设备上运行模型！

## ❓ 问题

如果您是新的 [Ultralytics HUB](https://bit.ly/ultralytics_hub) 用户，并且有问题或意见，您来对了地方！请点击此 repo 中 [Issues](https://github.com/ultralytics/hub/issues) 选项卡中的 [新建问题](https://github.com/ultralytics/hub/issues/new/choose) 按钮，让
