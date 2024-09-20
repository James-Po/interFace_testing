"""
1. 设计一个 Game 类 (类名)
2. 属性:
• 定义一个 top_score 类属性 -> 记录游戏的历史最高分
• 定义一个 player_name 实例属性 -> 记录当前游戏的玩家姓名
3. 方法:
• 静态方法 show_help() -> 直接打印  这是游戏帮助信息
• 类方法 show_top_score() -> 显示历史最高分
• 实例方法 start_game() -> 开始当前玩家的游戏
-	3.1 输出 玩家 xxx 开始游戏
-	3.2 使用随机数,生成 10 - 100 之间的随机数字作为本次游戏的得分
-	3.3 打印 玩家 xxx 本次游戏得分 xxx
-	3.4 判断本次游戏得分和最高分之间的关系

4. 主程序步骤: __main__
	1 查看帮助信息
	2 查看历史最高分
	3 创建游戏对象，开始一次游戏
	4.查看最高分
	5.再开始一次游戏
	6.查看最高分
	7.再开始一次游戏
	8.查看最高分
"""

import random
class Game:
    # 定义一个类属性 -> 记录游戏的历史最高分
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("这是游戏帮助信息")

    @classmethod
    def show_top_score(cls):
        print(f"历史最高分是: {cls.top_score}")

    def start_game(self):
        print(f"{self.player_name} 开始游戏")
        score = random.randint(10, 100)
        print(f"{self.player_name} 本次游戏得分: {score}")
        if score > Game.top_score:
            Game.top_score = score
            print(f"{self.player_name} 本次游戏得分: {score}")
            # print("历史最高分更新为:", Game.top_score)

if __name__ == '__main__':
    Game.show_help()
    Game.show_top_score()
    game = Game("小明")
    game.start_game()
    Game.show_top_score()
    game.start_game()
    Game.show_top_score()
    game.start_game()
    Game.show_top_score()