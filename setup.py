from setuptools import setup, find_packages

setup(name='yolo-card-trainer', version='1.0.0', license='MIT',
    description='A project for creating dataset and training a YOLO model', author='MacMat01, SenseiBonsai2k',
    author_email='matteo.machella01@gmail.com, cristian.marinozzi1@gmail.com',
    url='https://github.com/MacMat01/yolo-card-trainer', packages=find_packages(),
    install_requires=['opendatasets', 'ultralytics', 'opencv-python-headless',  # py-opencv
        'pandas', 'seaborn', 'matplotlib', 'ipykernel', 'torch', 'torchvision', 'torchaudio', 'imgaug', 'tqdm',
        'requests', 'pyzbar'], classifiers=['Development Status :: 3 - Alpha', 'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License', 'Programming Language :: Python :: 3.12.3', ], )
