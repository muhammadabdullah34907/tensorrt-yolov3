"""yolov3_classes.py

NOTE: Number of YOLOv3 COCO output classes differs from SSD COCO models.
"""

COCO_CLASSES_LIST = [
'motorcycle',
'car',
'truck',
'bus',
'utilitario',
'bike'
]

# For translating YOLOv3 class ids (0~79) to SSD class ids (0~90)
yolov3_cls_to_ssd = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 27, 28, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58,
    59, 60, 61, 62, 63, 64, 65, 67, 70, 72, 73, 74, 75, 76, 77, 78, 79,
    80, 81, 82, 84, 85, 86, 87, 88, 89, 90,
]


def get_cls_dict(model):
    """Get the class ID to name translation dictionary."""
    if model == 'coco':
        cls_list = COCO_CLASSES_LIST
    else:
        raise ValueError('Bad model name')
    return {i: n for i, n in enumerate(cls_list)}
