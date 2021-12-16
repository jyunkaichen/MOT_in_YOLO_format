import argparse
import cv2
import os

def convert_img(dir, dir_yolo):

    test_or_train = os.listdir('{}'.format(dir))

    for t in test_or_train:

        t_dir = os.listdir('{}/{}'.format(dir, t))
        
        for datasets in t_dir:

            dataset_name = datasets.split('-')

            if(dataset_name[2] != 'DPM'):
                continue

            img_dir = os.listdir('{}/{}/{}/img1'.format(dir, t, datasets))

            for img in img_dir:
                
                img_name = dataset_name[1] + img.split('.')[0]
                
                img_ = cv2.imread('{}/{}/{}/img1/{}'.format(dir, t, datasets, img))
                
                cv2.imwrite('{}/images/{}/{}.jpg'.format(dir_yolo, t, img_name), img_)

def convert_label(dir, dir_yolo):

    dw = 1 / 1920
    dh = 1 / 1080

    train_dir = os.listdir('{}/train'.format(dir))
    
    for datasets in train_dir:

        dataset_name = datasets.split('-')

        if(dataset_name[2] != 'DPM'):
            continue

        label_file = open('{}/train/{}/gt/gt.txt'.format(dir, datasets), 'r')

        for line in label_file.readlines():
            
            obj = line.split(',')

            # Read
            img_frame = obj[0]
            x_min = float(obj[2])
            y_min = float(obj[3])
            w = float(obj[4])
            h = float(obj[5])
            cls = int(obj[7]) - 1

            # Calculate
            x_center = (x_min + w / 2) * dw
            y_center = (y_min + h / 2) * dh
            width = w * dw
            height = h * dh

            # Write
            label_file_name = dataset_name[1] + '{:>6}'.format(img_frame).replace(' ', '0')
            label_file_yolo = open('{}/labels/train/{}.txt'.format(dir_yolo, label_file_name), 'a')
            label_file_yolo.write("%d %f %f %f %f\n" % (cls, x_center, y_center, width, height))
            label_file_yolo.close()

        label_file.close()

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", help = "Relative location of MOT17/20 dataset", required=True)
    parser.add_argument("--yolo_dir", help = "Relative location of MOT17/20_yolo dataset", required=True)
    args = parser.parse_args()

    mot_dir = args.dir
    mot_yolo_dir = args.yolo_dir

    try:
        os.mkdir(mot_yolo_dir)
        os.chdir(mot_yolo_dir)
        os.mkdir('images')
        os.chdir('images')
        os.mkdir('train')
        os.mkdir('test')
        os.chdir('../')
        os.mkdir('labels')
        os.chdir('labels')
        os.mkdir('train')
        os.chdir('../../')

        # Convert images (train & test)
        convert_img(mot_dir, mot_yolo_dir)

        # Convert labels (train)
        convert_label(mot_dir, mot_yolo_dir)

    except Exception as e:
        print(e)



    

    