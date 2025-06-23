# Stable-Diffusion-metadata-generator

This repository provides a toolkit to assist in evaluating whether metadata or visual fidelity is preserved across image generation pipelines. It supports image preprocessing, conversion to a standard format, and similarity comparison using both deep learning (ViT) and traditional metrics (SSIM).

## ✨ Features

- ✅ **Image Format Conversion**: Converts `.jfif` files to `.png` to ensure uniformity.
- ✅ **Image Preprocessing**: Resizes and normalizes images for neural network compatibility.
- ✅ **ViT-based Cosine Similarity**: Measures similarity in the feature space using a pretrained Vision Transformer (ViT).
- ✅ **SSIM Metric**: Computes perceptual similarity in the pixel space.
- ✅ **Batch Comparison of Image Pairs**: Automatically compares matching images from `original/` and `embedded/` directories.

## 🧪 Applications

* Evaluation of embedded metadata after image reconstruction
* Image quality benchmarking in generative pipelines
* Reproducibility support for AI image-processing research

## 📝 License

This project is released under the GPL-3.0 License.

## 🔖 Citation

This code supports a scientific paper currently under peer review. Citation details will be updated upon publication.
