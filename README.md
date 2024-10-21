## Damage Detection in Structural Health Monitoring Using Transformers ##
This project applies transformer-based machine learning models to classify damage in composite structures using Lamb wave responses. The primary focus is on improving the accuracy of damage detection in Structural Health Monitoring (SHM) systems by leveraging transformers, which excel in handling long-range dependencies in time-series data. The project involves working with the Open Guided Waves (OGW) dataset, which provides guided wave signals collected at various temperatures and damage states.

## Table of Contents ##
1. Introduction
2. Dataset
3. Model Architecture
4. Installation
5. Usage
6. Results

## Introduction ##
Structural Health Monitoring (SHM) is a crucial technique for ensuring the safety and longevity of complex structures, especially in aerospace, civil, and mechanical engineering. Lamb waves are commonly used for detecting damage in such structures due to their long-range scanning capability and sensitivity to small defects. This project introduces a transformer-based approach for classifying damaged and undamaged states in composite structures using guided wave data.

### The key contributions of this project are: ###

- Developing a transformer-based architecture to process Lamb wave signals.
- Implementing data preprocessing techniques such as downsampling and normalization.
- Evaluating the model's performance using various metrics including accuracy, precision, recall, and F1-score.

## Dataset ##
The project uses the Open Guided Waves (OGW) dataset, which contains guided wave signals recorded under both pristine and damaged conditions of a carbon fiber-reinforced polymer (CFRP) plate. The dataset is divided into:

Training and testing samples with an equal number of damaged and undamaged data points.
Signals recorded at different temperatures (from 20°C to 60°C).
You can download the dataset from the [Open Guided Waves](https://openguidedwaves.de/ "OGW#2 dataset") repository.

## Data Preprocessing ##


## Model Architecture ##
The proposed transformer-based model leverages multi-head self-attention mechanisms to process the time-series data efficiently. The architecture includes:

- Input Layer: Takes a downsampled 1D array representing the Lamb wave response.
- Multi-Head Attention Layer: Captures long-range dependencies in the data.
- Convolutional Layers: Used to capture local features and patterns.
- Dense Layers: For classification into damaged or undamaged states.
- Optimizer: Adam optimizer with binary cross-entropy loss.
- The model is trained using a batch size of 32 over 300 epochs.

## Results ##

### Confusion Matrices###
The confusion matrices for the test as well as the evaluation modes have been depicted below. They showcase a good generalisation performance of the tranformer based classifier

The transformer-based model achieved an overall test accuracy of 84.14%. Below are the key evaluation metrics:

Precision: 0.91
Recall: 0.74
F1-Score: 0.82
Training and validation accuracy plots, as well as confusion matrices, are available in the results/ folder.