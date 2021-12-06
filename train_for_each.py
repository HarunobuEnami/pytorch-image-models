import shutil
import glob
import subprocess
import os

files = glob.glob('LOO/*/*')
# 何番目がどのクラスなのかをあとから参照するために作成するファイル
with open('meaning.txt', 'a') as f:
    for i, file in enumerate(files):
        f.write(f'{i}, {file}\n')

for i, file in enumerate(files):
    shutil.copytree('LOO', 'TRAIN')
    output_dir = f'outputs/{i}' 

    os.makedirs(output_dir)
    test_image = file.replace('LOO', 'TRAIN')
    
    shutil.move(test_image, f'outputs/{i}')
    subprocess.run(f'python3 train.py TRAIN --output {output_dir} --model tf_efficientnetv2_s_in21ft1k --pretrained -b 64', shell=True)    


    shutil.rmtree('TRAIN')

