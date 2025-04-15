<a href="https://www.ultralytics.com/"><img src="https://raw.githubusercontent.com/ultralytics/assets/main/logo/Ultralytics_Logotype_Original.svg" width="320" alt="Ultralytics logo"></a>

# Ultralytics coco8-human Dataset

The **Ultralytics `coco8-human` dataset** is a compact, attribute-rich dataset designed for rapid testing and development within the [Ultralytics YOLO](https://github.com/ultralytics/ultralytics) ecosystem. It consists of 8 carefully selected images from the [COCO 2017 training set](https://cocodataset.org/#home), making it ideal for validating pipelines and experimenting with new features.

These 8 images are split evenly, with 4 images for training and 4 for validation. Each image is annotated for the **'person'** class, including standard [bounding boxes](https://www.ultralytics.com/glossary/bounding-box) and detailed human attributes:

- **Weight (kg)**
- **Height (cm)**
- **Gender** (0: female, 1: male)
- **Age (years)**
- **Ethnicity**  
  (0: Asian, 1: White, 2: Middle Eastern, 3: Indian, 4: Latino, 5: Black)

Despite its small size, the `coco8-human` dataset provides enough diversity to effectively test [object detection](https://www.ultralytics.com/glossary/object-detection) [training pipelines](https://docs.ultralytics.com/modes/train/) for errors or serve as a quick sanity check before scaling up to larger datasets such as the [full COCO dataset](https://docs.ultralytics.com/datasets/detect/coco/). It is particularly useful for experimenting with models like [Ultralytics YOLO](https://docs.ultralytics.com/models/yolo11/), [YOLOv8](https://docs.ultralytics.com/models/yolov8/), and other [YOLO model versions](https://docs.ultralytics.com/models/).

This dataset is fully compatible with the Ultralytics framework and integrates seamlessly with [Ultralytics HUB](https://docs.ultralytics.com/hub/), enabling fast prototyping and validation.

For more information on datasets, model training, and best practices, explore the [Ultralytics documentation](https://docs.ultralytics.com/), learn about [data annotation and collection](https://docs.ultralytics.com/guides/data-collection-and-annotation/), or discover [object detection solutions](https://www.ultralytics.com/solutions/ai-in-automotive). If you're interested in the latest trends in computer vision, check out the [Ultralytics blog](https://www.ultralytics.com/blog/a-guide-to-deep-dive-into-object-detection-in-2025).

Join the discussion and get support from the community at the [Ultralytics Community Forums](https://community.ultralytics.com/) or connect with other users on [Ultralytics Discord](https://discord.com/invite/ultralytics).

## 📚 Resources

Enhance your experience with COCO8-human and Ultralytics tools using these valuable resources:

- [Ultralytics HUB Quickstart](https://docs.ultralytics.com/hub/quickstart/): Step-by-step guide to training models on datasets like COCO8 using Ultralytics HUB.
- [Ultralytics Documentation](https://docs.ultralytics.com/): Comprehensive guides on model usage, best practices, and advanced features.
- [COCO Dataset Overview](https://docs.ultralytics.com/datasets/detect/coco/): Learn more about the full COCO dataset and its applications in computer vision.
- [Ultralytics Models](https://docs.ultralytics.com/models/): Explore available YOLO models for object detection, segmentation, and more.
- [Ultralytics HUB GitHub Issues](https://github.com/ultralytics/hub/issues/new/choose): Report bugs, request features, or seek troubleshooting support.
- [Ultralytics Discord Community](https://discord.com/invite/ultralytics): Connect with users, developers, and the Ultralytics team for real-time discussions.
- [Ultralytics Community Forums](https://community.ultralytics.com/): Share your projects, ask questions, and engage with the broader Ultralytics community.
- [Ultralytics YOLO11 Model Page](https://docs.ultralytics.com/models/yolo11/): Details on the latest YOLO model architecture and usage.
- [Ultralytics Tasks Overview](https://docs.ultralytics.com/tasks/): Learn about supported computer vision tasks, including detection, segmentation, and more.
- [Ultralytics Model Training Tips](https://docs.ultralytics.com/guides/model-training-tips/): Best practices for efficient and effective model training.
- [Ultralytics Model Evaluation Insights](https://docs.ultralytics.com/guides/model-evaluation-insights/): Guidance on evaluating model performance and interpreting results.
- [Ultralytics Model Deployment Options](https://docs.ultralytics.com/guides/model-deployment-options/): Explore deployment strategies for your trained models.
- [Ultralytics License Information](https://www.ultralytics.com/license): For commercial use or custom solutions, complete the form to obtain an Enterprise License.

## 🚀 Contributions

We welcome and value contributions from the community! If you'd like to improve the `coco8-human` dataset, suggest new features, or report issues, please visit the [Ultralytics GitHub repository](https://github.com/ultralytics/ultralytics) to submit a pull request or open an issue. Your feedback helps us make Ultralytics tools better for everyone.

[![Ultralytics open-source contributors](https://raw.githubusercontent.com/ultralytics/assets/main/im/image-contributors.png)](https://github.com/ultralytics/ultralytics/graphs/contributors)
