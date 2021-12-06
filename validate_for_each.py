import shutil
import glob
import subprocess
import os

dirs = glob.glob('outputs/*')
for dir in dirs:
    ckpt = glob.glob(f'{dir}/20*')
    ckpt = ckpt[0] + '/model_best.pth.tar'
    subprocess.run(f'python3 inference.py {dir}/image --output_dir {dir} --model tf_efficientnetv2_s_in21ft1k --checkpoint {ckpt}', shell=True)