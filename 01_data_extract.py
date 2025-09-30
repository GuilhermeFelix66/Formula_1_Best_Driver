# The dataset is from Kaggle.com. To access it, we need to connect with KaggleHub, via import.

import kagglehub

# Download latest version
path = kagglehub.dataset_download("julianbloise/winners-formula-1-1950-to-2025")

print("Path to dataset files:", path)