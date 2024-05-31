if __name__ == '__main__':

    from ultralytics import YOLO
    # Load a model
    model = YOLO("yolov8n.yaml")  # build a new model from scratch
    model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

    #Use the model
    results = model.train(data=r"D:\yolo_v8\ultralytics-main - train\my_data.yaml", epochs=100 ,imgsz=640,workers=0,batch=1)

