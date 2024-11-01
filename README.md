# Cards Object Detection

[![CodeQL](https://github.com/MacMat01/cards-object-detection/actions/workflows/codeql.yml/badge.svg)](https://github.com/MacMat01/cards-object-detection/actions/workflows/codeql.yml)

This project aims to detect strategic fruits cards using YOLOv8. It is implemented in Python and uses several libraries
for data processing and model training.

## Project Structure

The project has the following structure:

- `src/`: Contains the source code of the project.
    - `dataset_creation/`: Contains the scripts for creating the dataset.
    - `model_training/`: Contains the scripts for training the YOLOv8 model.
- `environment.yml`: Contains the conda environment configuration.
- `setup.py`: Contains the setup configuration for the Python package.

## Getting Started

### Prerequisites

Ensure you have the following installed on your system:

- [Python](https://www.python.org/downloads/) 3.12.3 or higher
- [Conda package manager](https://www.anaconda.com/download)
- [Cuda Toolkit](https://developer.nvidia.com/cuda-toolkit-archive) 12.3 or higher
- Suggested IDE:
  - [VSCode](https://code.visualstudio.com/Download) with Python and Jupyter extensions
  - [PyCharm Professional](https://www.jetbrains.com/pycharm/download/?section=windows) is also a good choice if you
    have a license

### Installation

1. Clone the repository:

```bash
git clone https://github.com/MacMat01/yolo-card-trainer.git
```

2. Navigate to the project directory:

```bash
cd yolo-card-trainer
```

3. Create a new conda environment from the `environment.yml` file:

```bash
conda env create --name <your-environment-name> -f environment.yml
```

4. Activate the conda environment:

```bash
conda activate <your-environment-name>
```

5. Install the `build` and `pip` tools:

```bash
pip install --upgrade build pip
```

6. Build a source distribution (sdist) and a binary distribution (wheel) of your package:

```bash
python -m build
```

7. Install the package from the wheel file:

```bash
pip install --user dist/*.whl # If it doesn't work, change </*.whl> to the name of the wheel file generated in step 6
```

8. (OPTIONAL) If gpu isn't working for model training, install pytorch-cuda manually (remember to restart pc, it often
   works):

```bash
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
```

### Running the Application

Follow the instruction in the following Jupyter notebooks:

1. `Cards Extraction.ipynb`
2. `Dataset Creation.ipynb`
3. `YOLO Card Trainer.ipynb`

## License

This project is licensed under the MIT License—see the [LICENSE](LICENSE) file for details.
