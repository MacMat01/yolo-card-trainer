import os
import sys
import xml.etree.ElementTree as ET
from glob import glob

def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)

def convert_annotation(xml_fn):
    in_file = open(xml_fn)
    txt_fn = xml_fn.replace(".xml", ".txt")
    out_file = open(txt_fn, 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(f"{cls_id - 1} {bb[0]:0.6f} {bb[1]:0.6f} {bb[2]:0.6f} {bb[3]:0.6f}\n")
    in_file.close()
    out_file.close()

if len(sys.argv) != 3:
    sys.exit(1)
images_dir = sys.argv[1]
classes_fn = sys.argv[2]
if not os.path.isfile(classes_fn):
    print(f"Classes file {classes_fn} is not a file")
    sys.exit(1)
if not os.path.isdir(images_dir):
    print(f"{images_dir} is not a directory")
    sys.exit(1)
with open(classes_fn, "r") as f:
    classes = f.read().split("\n")
classes = [c for c in classes if c != '']
print(classes, len(classes))

for i, xml_fn in enumerate(glob(images_dir + "/*.xml")):
    img_fn = xml_fn.replace(".xml", ".jpg")
    convert_annotation(xml_fn)
    if (i + 1) % 100 == 0:
        print(i + 1)