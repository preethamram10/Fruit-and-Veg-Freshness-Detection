This repository contains an implementation of a deep learning model using TensorFlow/Keras to classify fruits and vegetables based on their freshness. The model is designed to identify whether an image corresponds to a fresh or rotten fruit/vegetable across multiple categories. It is built with an efficient MobileNetV2 backbone and a custom classification head for high performance and accuracy.

The model leverages the pre-trained MobileNetV2 as its base for feature extraction. This ensures computational efficiency while retaining the ability to generalize well. On top of this base, additional layers are added, including global average pooling, dropout for regularization, and dense layers for multi-class classification. This architecture is particularly effective for distinguishing between the 20 target classes, which include fresh and rotten states of popular fruits and vegetables.

For data preprocessing, the script uses Keras' ImageDataGenerator to perform real-time data augmentation. Techniques such as rescaling, shearing, zooming, and horizontal flipping are applied to enhance model robustness and generalization. The dataset is expected to be organized into a hierarchical directory structure, with subdirectories for each class under a main directory for fruits and vegetables.

The training process involves freezing the MobileNetV2 base initially and training only the added layers. The model is compiled with the Adam optimizer and categorical cross-entropy loss and trained for 10 epochs. Both training and validation data are dynamically managed using data generators, ensuring an efficient workflow.

Once the model is trained, it is saved as fruit_veg_freshness_model.h5 for future use. The saved model can be loaded and used for inference, allowing users to classify images of fruits and vegetables into their respective categories.

This implementation is highly modular and can be extended to include additional classes, datasets, or fine-tuning of the MobileNetV2 layers. Potential future enhancements include deploying the model using TensorFlow Lite or Flask APIs for real-world applications, as well as expanding the dataset for broader applicability.

This repository provides a practical and efficient approach to building a freshness classification system, making it suitable for academic projects, agricultural applications, and inventory management systems. Feel free to use, modify, and extend the code as needed, with attribution greatly appreciated!
