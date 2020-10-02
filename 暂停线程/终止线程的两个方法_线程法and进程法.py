import threading
import multiprocessing
from head.my_time import tt

def f(T = 5):
    # tt = Time()
    tt.__init__()
    while(tt.during(T)):

        print(tt.now(1))
        tt.sleep(0.01)

        if(tt.stop_alt('s')):   break

    print('End.')
    return 1

class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self,  *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def run(self, T = 5):
        tt.__init__()
        while (tt.during(T)):

            print(tt.now(1))
            tt.sleep(0.01)

            if (tt.stop_alt('s')):   break

        print('End.')
        return 1

    1

# 多线程
if(1):
    thread = threading.Thread(target=f)
    thread.start()

    print("begin run main thread")
    st = StoppableThread()
    st.run()
    tt.sleep(2)
    st.stop()
    # st.stopped()
    print("main thread end")


if __name__ == '__main__':
    proc = multiprocessing.Process(target=f, args=(3,))
    print('start! ')
    tt.sleep(2)
    proc.start()
    tt.sleep(3)
    proc.terminate()

