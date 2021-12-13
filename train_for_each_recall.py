import shutil
import glob
import subprocess
import os

files = glob.glob('LOO/*/*')
# A file to show the correspondance between number and file name.�
with open('meaning.txt', 'a') as f:
    for i, file in enumerate(files):
        f.write(f'{i}, {file}\n')

for i, file in enumerate(files):
    shutil.copytree('LOO', 'TRAIN')
    output_dir = f'outputs/{i}' 

    os.makedirs(output_dir)
    test_image = file.replace('LOO', 'TRAIN')

    os.makedirs(f'outputs/{i}/image')
    shutil.move(test_image, f'outputs/{i}/image')
    subprocess.run(f'python3 train_high_recall.py TRAIN --output {output_dir} --model tf_efficientnetv2_s_in21ft1k --pretrained -b 64 -w0 60.0 -w1 40.0', shell=True)    


    shutil.rmtree('TRAIN')

