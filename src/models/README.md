# Running pretrained YOLOv5s models

Model weights are stored in the 'weights' folder. In order to run model inference first: 

```
git clone https://github.com/KMacfarlaneGreen/yolov5.git

pip install -r requirements.txt

```

Then run:

```
python detect.py --source '<input_image>' --weights <weights>.pt --conf 0.25

```

