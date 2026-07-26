import os

image_folder = "/home/raspberrypi/tomato_dataset/images/train"
label_folder = "/home/raspberrypi/tomato_dataset/labels/train"

os.makedirs(label_folder, exist_ok=True)

for img in os.listdir(image_folder):

    label_path = os.path.join(label_folder, img.replace(".jpg",".txt"))

    # detect healthy vs unhealthy using filename pattern
    if "healthy" in img.lower():
        class_id = 0
    else:
        class_id = 1

    with open(label_path,"w") as f:
        f.write(f"{class_id} 0.5 0.5 1.0 1.0")

