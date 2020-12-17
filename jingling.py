import random
import time

class Monsters():

    def __init__(self, name):
        self.__name = name
        # 初始等级
        self.__level = 1
        # 动态血量，供计算和展示
        self.__hp = 300
        # 等级固定血量，供升级计算
        self.__max_hp = 300
        # 初始攻击力在80 ~ 100之间随机
        self.__ap = random.randint(80, 100)
        # 初始防御力在0 ~ 1之间随机
        self.__df = random.random()
        # 动态经验，供计算和展示
        self.__exp = 0
        # 等级固定经验，供升级计算
        self.__max_exp = 100


    def get_info(self, name=False, lev=False, hp=False, ap=False, df=False, exp=False, mexp=False, mhp=False):
        if name == True:
            return self.__name
        elif lev == True:
            return self.__level
        elif hp == True:
            return self.__hp
        elif ap == True:
            return self.__ap
        elif df == True:
            return self.__df
        elif exp == True:
            return self.__exp
        elif mexp == True:
            return self.__max_exp
        elif mhp == True:
            return self.__max_hp
        else:
            return self.__name, self.__level, self.__hp, self.__ap, self.__df, self.__exp, self.__max_exp


    def attack(self, opponent):
        damage, result = opponent.take_attck(self.__ap)
        # 对手血量小于0被击败
        if result <= 0:
            # 击败经验+20
            self.__exp += 20
            print("%s 对 %s 造成 %.2f 伤害，%s 打败了 %s " %
                  (self.__name, opponent.__name, damage, self.__name,opponent.__name))
        else:  # 展示结果，未击败经验+10
            self.__exp += 10
            print("%s 对 %s 造成 %.2f 伤害，%s 还剩 %.2f 体力" %
                  (self.__name, opponent.__name, damage, opponent.__name, result))
        # 判断是否升级
        self.__level_up()
        # 返回对手结果给主程序做后续判定
        return result


    def take_attck(self, ap):
        # 造成的伤害和防御力有关，并提升经验
        damage = ap * (1 - self.__df)
        self.__hp = self.__hp - damage
        self.__exp += 5
        # 如果未被击败，判断是否升级
        if self.__hp > 0:
            self.__level_up()
        # 返回造成的伤害和最后的生命值
        return damage, self.__hp

    def __level_up(self):
        if self.__exp >= self.__max_exp:
            self.__exp = 0
            self.__max_exp *= 1.1
            self.__level += 1
            self.__max_hp *= 1 + random.random()
            self.__hp = self.__max_hp
            self.__ap *= 1 + random.random()
            if self.__df + 0.05 > 1:
                self.__df = 0.99
            else:
                self.__df += 0.05
            print("%s 升为 %d 级！" % (self.__name, self.__level))
            print("最大体力变为 %.2f, 攻击力变为 %.2f，防御力变为 %.2f" %
                  (self.__hp, self.__ap, self.__df))
            print("下次升级需要 %.2f 经验" % self.__max_exp)


    def rest(self):
        recovering = 30 * self.__level
        if self.__hp + recovering <= self.__max_hp:
            self.__hp += recovering
        else:
            recovering = self.__max_hp - self.__hp
            self.__hp = self.__max_hp
        print("%s 恢复了 %.2f 体力，现在有 %.2f 体力" % (self.__name, recovering, self.__hp))


    def defence(self, df=True):
        if df == True:
            if self.__df < 0.8:
                self.__df = random.uniform(0.95, 0.8)
            else:
                self.__df = 1
        else:
            self.__df = df
#精灵对战
monsters_pool = ['火柴鼠', '瞌睡熊', '板牙狸', '博学企鹅', '绅士企鹅',
                 '漂浮龟', '皮皮', '贪玩虎', '黑客', '蹦蹦娃', '呱噪鸦',
                 '弹簧蛇', '喷火龙']
my_monsters_list = []
op_monsters_list = []
print(r'''
 ____  ____  _  __ _____ _      ____  _
/  __\/  _ \/ |/ //  __// \__/|/  _ \/ \  /|
|  \/|| / \||   / |  \  | |\/||| / \|| |\ ||
|  __/| \_/||   \ |  /_ | |  ||| \_/|| | \||
\_/   \____/\_|\_\\____\\_/  \|\____/\_/  \|
''')


def init():
    for _ in range(3):
        monster = random.choice(monsters_pool)
        my_monsters_list.append(Monsters(monster))
        monsters_pool.remove(monster)

        monster = random.choice(monsters_pool)
        op_monsters_list.append(Monsters(monster))
        monsters_pool.remove(monster)

    print("你的小精灵有：", my_monsters_list[0].get_info(name=True), my_monsters_list[
          1].get_info(name=True), my_monsters_list[2].get_info(name=True))
    print("对手的小精灵有：", op_monsters_list[0].get_info(name=True), op_monsters_list[
          1].get_info(name=True), op_monsters_list[2].get_info(name=True))


def attacking(my, op):
    # 主动攻击
    my_result = my.attack(op)
    if my_result <= 0:
        op_monsters_list.remove(op)
    else:  # 反击
        op_result = op.attack(my)
        if op_result <= 0:
            my_monsters_list.remove(my)

def attacking1(op, my):
    # 主动攻击
    result = op.attack(my)
    if result <= 0:
        my_monsters_list.remove(my)
    else:  # 反击
        result = my.attack(op)
        if result <= 0:
            op_monsters_list.remove(op)


def resting(my):
    my.rest()


def defending(my, df=True):
    if df == True:
        df = my.get_info(df=True)
        my.defence()
        return df
    else:
        my.defence(df)


def show_names(m):
    for i in range(len(m)):
        print("%d. %s" % (i + 1, m[i].get_info(name=True)))


def show_choice():
    print("请选择你要进行的操作，按“q”退出游戏")
    print('''
        1. 攻击
        2. 防御
        3. 休息
        ''')


def main():
    init()
    while len(my_monsters_list)>0 and len(op_monsters_list)>0:
        show_choice()
        c = input("请输入选项: ")
        if c == "q":
            print("游戏结束!")
            break
        elif c == "1":
            print("你要出战的小精灵是")
            show_names(my_monsters_list)
            my_index = int(input("请输入序号：")) - 1
            my_monster = my_monsters_list[my_index]

            print("你要挑战的小精灵是")
            show_names(op_monsters_list)
            op_index = int(input("请输入序号：")) - 1
            op_monster = op_monsters_list[op_index]

            attacking(my_monster, op_monster)
        elif c == "2":
            print("你要进行防御的小精灵是")
            show_names(my_monsters_list)
            my_index = int(input("请输入序号：")) - 1
            my_monster = my_monsters_list[my_index]
            # 记录防御前的防御值
            df = defending(my_monster)
            # 防御后，电脑随机角色攻击防御角色
            op_monster = op_monsters_list[
                random.randint(0, len(op_monsters_list) - 1)]
            attacking1(op_monster, my_monster)
            # 如果防御角色未被击败，则恢复原来的防御值
            if my_monster in my_monsters_list:
                defending(my_monster, df)
        elif c == "3":
            print("你要休息的小精灵是")
            show_names(my_monsters_list)
            my_index = int(input("请输入序号：")) - 1
            my_monster = my_monsters_list[my_index]
            resting(my_monster)
            # 休息之后电脑随机角色攻击玩家随机角色
            my_monster = my_monsters_list[
                random.randint(0, len(my_monsters_list) - 1)]
            op_monster = op_monsters_list[
                random.randint(0, len(op_monsters_list) - 1)]
            attacking1(op_monster, my_monster)
        else:
            print("输入错误，请从新输入")


if __name__ == '__main__':
    main()
f
