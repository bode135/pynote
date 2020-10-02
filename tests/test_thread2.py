import multiprocessing  # 重点!
from head.my_time import tt
from tqdm import tqdm
# from tqdm._tqdm import trange

def f(T = 5, fresh = 0.1):

    run_times = round(T/fresh)

    for i in tqdm(range(run_times), 'Running... '):
        tt.sleep(fresh)

        if (tt.stop_alt('s')):  break

    return 1

def main():

    T = 10

    proc = multiprocessing.Process(target=f, args=(T,))
    print('start! ', 'expect run_T: ', T)
    # tt.sleep(1)
    tt.tqdm_sleep(3)
    proc.start()  # 开始

    tt.sleep(10)

    proc.terminate()  # 结束
    print(' --- Stop! --- ')



if __name__ == '__main__':
    # 一定要放在 '__main__' 函数里面运行, 不然报错!!
    main()