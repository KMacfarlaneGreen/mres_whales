# Running YOLOv5s models

Model weights are stored in the 'weights' folder. In order to run model inference first: 

```
git clone https://github.com/KMacfarlaneGreen/yolov5.git

pip install -r requirements.txt

```

Then run:

```
python detect.py --source '<input_image>' --weights <weights>.pt --conf 0.25

```

In order to train your own models you can run:

```
python train.py --img 640 --batch 32 --epochs 300 --data <input_data>.yaml --cfg ./models/yolov5s.yaml --weights yolov5s.pt --cache
```



