import xml.etree.ElementTree as ET
from os import getcwd
import glob

classes = ["deer", "beam", "gcooter", "others"]

def convert_annotation(annotation_voc, train_all_file, class_id):
    txt_file = open(f'{annotation_voc}', 'r')
    box_list = txt_file.read().split('\n')[0].split(' ')[1:]

    box = ''
    for b in box_list:
        if box == '':
            box = b
        else:
            box = box + ',' + b
        #print(box)
    train_all_file.write(" "+ box + ',' + str(class_id))

train_all_file = open('./data/light/train_all.txt', 'w')

# Get annotations_voc list
for className in classes:
    annotations_voc = glob.glob(f'./data/light/image/train/v*.txt')
    for annotation_voc in annotations_voc:
        #print(annotation_voc)
        #print(annotation_voc.split('/')[-1].split('\\')[-1].split('.')[0])
        
        txt_file = open(f'{annotation_voc}', 'r')
        class_id = txt_file.read().split('\n')[0].split(' ')[0]
        
        ''' class 여러개일 경우
        class_id = []
        for line in txt_file.read().split('\n'):
            if line != '':
                class_id.append(line.split(' ')[0])
        print(class_id)
        '''
        
        image_id = annotation_voc.split('/')[-1].split('\\')[-1].split('.')[0]+'.JPG'
        train_all_file.write(f'./data/light/image/train/{class_id}/{image_id}')
        convert_annotation(annotation_voc, train_all_file, class_id)
        train_all_file.write('\n')
train_all_file.close()