import os
import shutil

images = os.listdir('./genuine')
for i in range(1,31):
    os.mkdir(f'{i}'.zfill(3))
for i in images:
    shutil.copy(f'./genuine/{i}', f'{i.split(".")[0][-3:]}')
    
images = os.listdir('./forged')
for i in range(1,31):
    os.mkdir(f'{i}'.zfill(3)+'_forg')
for i in images:
    shutil.copy(f'./forged/{i}', f'{i.split(".")[0][-3:]}_forg')
    
