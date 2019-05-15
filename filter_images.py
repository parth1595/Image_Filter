import os
import glob
import sys
import shutil
import argparse

parser = argparse.ArgumentParser(description='Process Dataset.')
parser.add_argument('--path', type=str, required=True,
                    help='Dataset Path')
parser.add_argument('--copy', type=bool,required=True,
                    help='copy flag for dataset copying)')
parser.add_argument('--count', type=int,required=True,
                    help='copy flag for dataset copying)')

args = parser.parse_args()

cwd = os.getcwd()

path = args.path
flag = args.copy
count = args.count

dir_path = os.path.dirname(os.path.realpath(path))

os.chdir(path)
file_count = 0

NEW_DIRECTORY = path + "_updated"
TRAINING_DIRECTORY = "training"
IMAGESETS_DIRECTORY = "ImageSets"

if os.path.exists(dir_path + '/' + NEW_DIRECTORY):
    shutil.rmtree(dir_path + '/' + NEW_DIRECTORY)

os.mkdir(dir_path + '/' + NEW_DIRECTORY)

main_dir_path = os.path.join(dir_path, NEW_DIRECTORY)
os.mkdir(main_dir_path + '/' + TRAINING_DIRECTORY)
os.mkdir(main_dir_path + '/' + IMAGESETS_DIRECTORY)

train_dir_path = os.path.join(dir_path, NEW_DIRECTORY, TRAINING_DIRECTORY)
os.mkdir(train_dir_path + '/label_2')
os.mkdir(train_dir_path + '/image_2')

annotation_path = os.path.join(dir_path, path, 'training/label_2')

for fn in glob.glob(annotation_path + '/*.txt'):
        with open(fn) as f:
            num_lines = 0
            for line in f:
                num_lines += 1
            if num_lines <= count:
                file_count = file_count + 1
                if flag:
                    shutil.copy(fn, dir_path + '/' + NEW_DIRECTORY + '/training/label_2')
                    file_name = fn.split(path + "/training/label_2")[1]
                    t = file_name.split(".")[0]
                    image = t + '.jpg'
                    print("Copying Image File " + image + "  ..........")
                    shutil.copy(dir_path + '/' + path + '/training/image_2/' + image, dir_path + '/' + NEW_DIRECTORY + '/training/image_2/')
                    with open(dir_path + '/' + NEW_DIRECTORY + '/' + IMAGESETS_DIRECTORY + '/trainval.txt', 'a+') as w:
                        w.write(t + '\n')
                    w.close()

print("Number of Files with person count" + str(count) + "= " + str(file_count))
