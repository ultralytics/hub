<a href="https://www.ultralytics.com/"><img src="https://raw.githubusercontent.com/ultralytics/assets/main/logo/Ultralytics_Logotype_Original.svg" width="320" alt="Ultralytics logo"></a>

# Ultralytics coco8-human Dataset

The Ultralytics `coco8-human` dataset is a compact yet versatile collection designed for testing and development purposes within the [Ultralytics YOLO](https://github.com/ultralytics/ultralytics) ecosystem. It comprises 8 images carefully selected from the widely-used [COCO](https://cocodataset.org/#home) 2017 training set.

These 8 images are split evenly: 4 for training and 4 for validation. Each image features annotations specifically for the 'person' class, including standard [bounding boxes](https://www.ultralytics.com/glossary/bounding-box). Additionally, this dataset provides rich attribute information for each detected human:

-   Weight (kg)
-   Height (cm)
-   Gender (0: female, 1: male)
-   Age (years)
-   Ethnicity (0: Asian, 1: White, 2: Middle Eastern, 3: Indian, 4: Latino, 5: Black)

Despite its small size, `coco8-human` offers sufficient diversity to effectively test [object detection](https://www.ultralytics.com/glossary/object-detection) model [training](https://docs.ultralytics.com/modes/train/) pipelines for potential errors or serve as a quick sanity check before committing resources to larger datasets like the full [COCO dataset](https://docs.ultralytics.com/datasets/detect/coco/). It is particularly well-suited for experimenting with models like [Ultralytics YOLOv8](https://docs.ultralytics.com/models/yolov8/).

This dataset is intended for use with Ultralytics models and integrates seamlessly with the Ultralytics framework.

For further information on datasets and model training, please refer to the [Ultralytics documentation](https://docs.ultralytics.com/). Join the conversation and get support from the community at the [Ultralytics Community Forums](https://community.ultralytics.com/).

## Contributions

We value contributions from the community! If you'd like to improve the `coco8-human` dataset or suggest new features, please visit our [GitHub repository](https://github.com/ultralytics/ultralytics) and submit a pull request or open an issue. Thank you for helping us make Ultralytics tools better for everyone.
