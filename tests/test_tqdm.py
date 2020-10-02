import time
from tqdm import tqdm

with tqdm(total=1000) as pbar:
    pbar.set_description('Processing:')
    # total表示总的项目, 循环的次数20*10(每次更新数目) = 200(total)
    for i in range(100):
        # 进行动作, 这里是过0.1s
        time.sleep(0.1)
        # 进行进度更新, 这里设置10个
        pbar.update(10)

from tqdm import tqdm
import time

for i in tqdm(range(200)):
    time.sleep(0.1)