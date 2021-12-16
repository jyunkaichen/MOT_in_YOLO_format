# MOT17/20 dataset in YOLO format 
This tool converts MOT17/20 dataset to the format of YOLO.
The generated labels can be directly used to start a Training on the MOT17/20 data for 2D object detection with YOLO.

## Setup

Install the packages:

```
pip3 install -r requirements.txt
```

## MOT17/20 dataset

Download the MOT17 dataset from the link https://motchallenge.net/data/MOT17/

Download the MOT20 dataset from the link https://motchallenge.net/data/MOT20/

## Usage (Take MOT17.zip as an example)

Unzip MOT17.zip and put MOT_to_yolo.py at the same folder with it:

```
MOT17/
MOT_to_yolo.py
```

Run MOT_to_yolo.py:

```
python MOT_to_yolo.py --dir ./MOT17 --yolo_dir ./MOT17_yolo 
```

## After usage

You will get:

```
MOT17/
MOT17_yolo/
MOT_to_yolo.py
```
