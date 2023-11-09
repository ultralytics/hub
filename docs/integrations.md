# Ultralytics HUB Integrations

🚧 **Under Construction** 🚧

Welcome to the Integrations guide for [Ultralytics HUB](https://bit.ly/ultralytics_hub)!

We are in the process of expanding this section to provide you with comprehensive guidance on integrating your YOLOv5 and YOLOv8 models with various platforms and formats. Currently, Roboflow is our available dataset integration, with a wide range of export integrations for your trained models.

<p align="center">
  <br>
  <iframe width="720" height="405" src="https://www.youtube.com/embed/lveF9iCMIzc?si=_Q4WB5kMB5qNe7q6"
    title="YouTube video player" frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowfullscreen>
  </iframe>
  <br>
  <strong>Watch:</strong> Train Your Custom YOLO Models In A Few Clicks with Ultralytics HUB.
</p>

## Available Integrations

### Dataset Integrations

- **Roboflow**: Seamlessly import your datasets for training.

### Export Integrations

| Format                                                             | `format` Argument | Model                     | Metadata | Arguments                                           |
| ------------------------------------------------------------------ | ----------------- | ------------------------- | -------- | --------------------------------------------------- |
| [PyTorch](https://pytorch.org/)                                    | -                 | `yolov8n.pt`              | ✅       | -                                                   |
| [TorchScript](https://pytorch.org/docs/stable/jit.html)            | `torchscript`     | `yolov8n.torchscript`     | ✅       | `imgsz`, `optimize`                                 |
| [ONNX](https://onnx.ai/)                                           | `onnx`            | `yolov8n.onnx`            | ✅       | `imgsz`, `half`, `dynamic`, `simplify`, `opset`     |
| [OpenVINO](../integrations/openvino.md)                            | `openvino`        | `yolov8n_openvino_model/` | ✅       | `imgsz`, `half`                                     |
| [TensorRT](https://developer.nvidia.com/tensorrt)                  | `engine`          | `yolov8n.engine`          | ✅       | `imgsz`, `half`, `dynamic`, `simplify`, `workspace` |
| [CoreML](https://github.com/apple/coremltools)                     | `coreml`          | `yolov8n.mlpackage`       | ✅       | `imgsz`, `half`, `int8`, `nms`                      |
| [TF SavedModel](https://www.tensorflow.org/guide/saved_model)      | `saved_model`     | `yolov8n_saved_model/`    | ✅       | `imgsz`, `keras`                                    |
| [TF GraphDef](https://www.tensorflow.org/api_docs/python/tf/Graph) | `pb`              | `yolov8n.pb`              | ❌       | `imgsz`                                             |
| [TF Lite](https://www.tensorflow.org/lite)                         | `tflite`          | `yolov8n.tflite`          | ✅       | `imgsz`, `half`, `int8`                             |
| [TF Edge TPU](https://coral.ai/docs/edgetpu/models-intro/)         | `edgetpu`         | `yolov8n_edgetpu.tflite`  | ✅       | `imgsz`                                             |
| [TF.js](https://www.tensorflow.org/js)                             | `tfjs`            | `yolov8n_web_model/`      | ✅       | `imgsz`                                             |
| [PaddlePaddle](https://github.com/PaddlePaddle)                    | `paddle`          | `yolov8n_paddle_model/`   | ✅       | `imgsz`                                             |
| [NCNN](https://github.com/Tencent/ncnn)                            | `ncnn`            | `yolov8n_ncnn_model/`     | ✅       | `imgsz`, `half`                                     |

## Coming Soon

- Additional Dataset Integrations
- Detailed Export Integration Guides
- Step-by-Step Tutorials for Each Integration

## Need Help Now?

While we're polishing this page, feel free to:

- Browse the [Ultralytics HUB Docs](../) for detailed guides and tutorials.
- Raise an issue on our [GitHub](https://github.com/ultralytics/hub/issues/new/choose) for support.
- Join our [Discord Community](https://ultralytics.com/discord) for questions and discussions.

We appreciate your patience as we work to make this section comprehensive and user-friendly. Stay tuned for updates!
