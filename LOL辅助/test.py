from head.my_time import Time, tt
class Robot:
    def __init__(self, model = 'rank', hero = '铁男', ban = None):
        self.ret_queueing = False       # 是否返回了排队界面
        self.game_start = False
        pass

    def run(self):
        self.open_lol_wind()    # 打开lol客户端
        self.select_model()     # 选择游戏模式


        # 开启检测线程, 如果 re_queue == True, 则重新开始 queue() 和 banpick().
        if(self.re_queue()):    # 是否要排队
            self.queue()        # 排队
            self.banpick()      # banpick

        pass

    def open_lol_wind(self):
        pass

    def select_model(self):
        pass

    def queue(self):
        # 排队
        pass

    def re_queue(self):
        # 检测是否重新进入了队伍
        pass

    def banpick(self):
        pass

    def ban(self):
        pass

    def pick(self):
        pass

    def hang_up(self):
        pass

    pass
if __name__ == '__main__':
    robot = Robot()
    robot.run()
    tt.tqdm_sleep(3)
