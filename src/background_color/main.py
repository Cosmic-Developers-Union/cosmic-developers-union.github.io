# coding: utf-8

"""
Created on 2024-10-07

"""

import re
import textwrap


FILE = "blogs/content/background-color.md"
EXAMPLE_TEXT = """
第一章：掉进兔子洞（Down The Rabbit Hole）

白兔先生。
一天，闷闷不乐的爱丽丝跟姐姐同坐于河畔。忽见一只古怪的白兔走过──它穿戴打扮，手持怀表，自言自语，行色匆匆。好奇的爱丽丝跟着它跑，跳进兔子洞里去。这个洞非常非常深，过了很久，爱丽丝终于着地。她惊觉自己身处奇怪的大厅，四周尽是大大小小的门，而所有门都被上了锁。她捡到一条门匙，却仅能开启一道小门。由于这道门实在太小了，她只能望过去，却发现那边有个标致的花园。她把门匙放在桌上，并在大厅别处找到一瓶写着“喝我”的饮料。爱丽丝不由分说把它喝完，发现自己缩小了，当能穿过小门，却拿不回桌上的门匙。慌乱之际，她捡到一件写着“吃我”的蛋糕。这一次，爱丽丝吃掉它后竟又急速变大，大得连头顶也贴著天花板了。

第二章：泪水之潭（The Pool of Tears）

掉进泪水中的老鼠和爱丽丝。
爱丽丝不禁大哭起来，整个门厅尽是泪水。她不经意地捡起一把扇子，身体竟又变小了，她不得不在自己的泪水中游走。途中，她遇到一只同在游泳的老鼠。爱丽丝想要跟它闲聊几句，却总是把她的家猫“黛娜”挂在嘴边，结果当然触怒了视猫为死敌的老鼠。

第三章：无谓的竞赛和长长的故事（The Caucus Race and a Long Tale）
泪水冲走了其他动物和雀鸟；一时间，爱丽丝已被一群动物包围。他们聚集在岸边，讨论如何弄干身体。老鼠发表了一场有关威廉一世的冗长演说，爱丽丝听罢觉得无聊极了；渡渡鸟则认为最好的方法就是举行一场无结果的比赛：大家绕圈跑，而没有胜负之分。爱丽丝懵懵懂懂的又说起家猫，结果把所有动物都又吓跑了。

第四章：白兔先生与蜥蜴比尔（The Rabbit Sends a Little Bill）
令爱丽丝掉进地底的白兔先生又出现了。这一回，他在寻找公爵夫人的手套和扇子。白兔先生命令爱丽丝入屋拿回物品，可是，爱丽丝刚进屋，看到一块饼干便吃了起来，身体又变大了，吓坏了的白兔先生，于是命令园丁蜥蜴比尔从烟囱爬进屋内以寻失物。此时，屋外已经聚集了一群动物，他们呆呆地看着爱丽丝偌大的手臂，并开始向她猛投卵石。卵石却化成一件件蛋糕；爱丽丝把它们一一吃下，身体又缩小了。

第五章：毛毛虫的建议（Advice from a Caterpillar）
爱丽丝见到一棵蘑菇，上面坐着一条蓝色的毛虫。他抽著水烟，向爱丽丝探问起来。爱丽丝回应他，自己正在个性转变期之中，时常心绪不宁，她甚至连一首诗都记不起来。毛虫离开之前，告诉了她蘑菇的秘密：吃其中一半会使她变高，吃另一半会使她变矮。于是，她把蘑菇一分为二，果然，吃其中一半使她矮小无比，吃另一半则令她的脖子增长。她的脑袋直达树丛之中，树上的鸽子甚至误以为她长长的脖子是一条毒蛇。经过一番努力，爱丽丝终于恢复原来的身高。她蹒跚地走，偶然进入了一个小庄园。同时，她又利用蘑菇调校最适合的身高。

第六章：小猪与胡椒（Pig and Pepper）
鱼先生想把邀请信交予屋内的公爵夫人，于是将事情交托给蛙先生。爱丽丝观察著这个过程，并跟蛙先生讲了一堆晦涩难懂的话，最后还是让自己走进屋内。原来公爵夫人的厨娘正把碗碟乱扔和煮浓汤，并加入了大量胡椒。胡椒实在太多了，令爱丽丝、公爵夫人和她的婴儿不停打喷嚏，厨子和咧著嘴笑的柴郡猫却不受影响。婴儿不禁嚎啕大哭，而一向脾气暴躁的公爵夫人当然对此十分厌恶，最后还把婴儿交给爱丽丝照顾。爱丽丝抱着婴儿走，不久却惊觉婴儿竟变成了一头猪。

第七章：疯狂下午茶（A Mad Tea Party）
柴郡猫在树上出现，向爱丽丝指示往三月兔家的方向。接着他就消失了，他露齿的笑容却还在那儿，在空中浮现，这令爱丽丝注意到，她见过的猫大抵没有笑脸，却从没见过只有猫的笑容而没有其身。

然后，爱丽丝到三月兔的家里去。那时三月兔、帽子先生（现多被称为疯帽子）和睡鼠正举行疯狂茶聚，爱丽丝因而成为茶聚的宾客。在这一章，睡鼠几乎一直处于熟睡的状态；其他人则向爱丽丝讲谜语和轶事。疯帽子向她透露，由于他受到惩罚，使时间永远停留在下午六时，也就是下午茶时间，所以他们不得不整天都停留在茶点。言谈之间，爱丽丝受到侮辱，又受不了谜题和故事的疲劳轰炸，决定离开。临走前，她更断言这是她去过最无聊的茶聚。

第八章：王后的槌球场（The Queen's Croquet Ground）
爱丽丝离开茶聚，走进了一个花园。她遇到三个嬉戏玩乐的纸牌仆人，他们正为讨厌白玫瑰的红心王后将树上的白玫瑰涂上红色。接着，更多纸牌仆人、国王和王后都列队进入了花园，连白兔先生也来了。爱丽丝会见了国王和王后。那个王后很难讨好，她说自己平日只要对事物有些微的不满，就会大喊她的口头禅“给我砍掉他的头颅！”

王后邀请（或许有些人会认为那是命令）爱丽丝跟他们一起打槌球，可是，这场比赛很快便沦为一片混乱。他们把活生生的火烈鸟当作球棍，又把刺猬当作球。接着，爱丽丝再一次遇上柴郡猫。红心王后命人砍下柴郡猫的头，刽子手却抱怨他没可能做到，因为他只能看见柴郡猫的头。由于柴郡猫是属于公爵夫人的，王后只好将公爵夫人从监狱释放，再处理斩首的事。

第九章：假海龟的故事（The Mock Turtle's Story）
在爱丽丝的要求下，公爵夫人被带到槌球场，她深思著身边所有事物的意义。红心王后打消了给柴郡猫斩首的念头，并将爱丽丝介绍予鹫头飞狮认识。鹫头飞狮带爱丽丝去找假海龟。假海龟虽然没有什么可悲的事情，却感到极度失落。他诉说自己曾经在学校做过一只真正的海龟。然而，鹫头飞狮打断了他的话，好让他们能够一起玩游戏。

第十章：龙虾方块舞（Lobster Quadrille）
假海龟和鹫头飞狮跳起龙虾方块舞，而爱丽丝则背诵“这是龙虾的声音”。最后假海龟替爱丽丝唱了首《甲鱼汤》（Beautiful Soup），此时远处传来了“审判开始”的声音，于是鹫头飞狮带着爱丽丝参加审判。

第十一章：谁偷了馅饼（Who Stole the Tarts?）
爱丽丝到了审判的场所，红心骑士（Knave of Hearts）被控偷了红心王后的馅饼。陪审团由各种动物担任，包括蜥蜴比尔，白兔先生则担任喇叭手。在审判期间，爱丽丝发现自己愈长愈大，睡鼠（dormouse）说爱丽丝无权以这么快的速度长高，把他挤得喘不过气。爱丽丝回道睡鼠的控诉荒谬，因为每个人都会长大，而她自己没办法停下这个过程。同时，疯帽子和公爵夫人的厨师被传唤作证，当这两人的询问结束以后，爱丽丝被白兔先生传唤为下个证人。

第十二章：爱丽丝的证明（Alice's Evidence）
爱丽丝被传为证人，当她站起来时因为长太大了而弄倒了陪审员席，国王只得命令审判暂停到陪审员回到席次上。国王和王后引用第42条规定：身高一英里以上者必须退出法庭，但爱丽丝否认并拒绝离开。最后，王后和爱丽丝在一阵争吵以后，下令砍掉爱丽丝的头，但爱丽丝并不怕，她认为他们只不过是纸牌。整副牌此时飞上天，又落到爱丽丝身上，爱丽丝正要挥去这些牌，却发现自己在河边醒来，头还枕在姐姐的腿上，姐姐正挥去爱丽丝脸上的枯叶。爱丽丝把这个梦告诉姐姐，然后先离去了，姐姐则一边想着爱丽丝的奇怪梦境，一边恍惚地睡着了。
"""


class Markdown:
    """
    A class to handle Markdown file operations and conversion to HTML.
    Attributes:
        file (file object): The file object to write Markdown content to.
    Methods:
        __init__(file):
            Initializes the Markdown object with a file object.
        block(content, dedent=True):
            Writes a block of content to the file, optionally dedenting it.
        h1(content):
            Writes a level 1 header to the file.
        h2(content):
            Writes a level 2 header to the file.
        h3(content):
            Writes a level 3 header to the file.
        raw(content):
            Writes raw content wrapped in raw tags to the file.
        to_html(content: str):
            Converts Markdown content to HTML.
    """

    def __init__(self, file) -> None:
        self.file = file

    def block(self, content, dedent=True):
        if dedent:
            content = textwrap.dedent(content)
        self.file.write(f"{content}\n\n")

    def h1(self, content):
        self.file.write(f"# {content}\n\n")

    def h2(self, content):
        self.file.write(f"## {content}\n\n")

    def h3(self, content):
        self.file.write(f"### {content}\n\n")

    def raw(self, content):
        self.file.write(f"{{{{<raw>}}}}\n\n{content}{{{{</raw>}}}}\n\n")

    @classmethod
    def to_html(cls, content: str):
        blocks = []
        for block in content.split("\n\n"):
            block = block.strip()
            if not block:
                continue
            if re.match(r"^#+ .*$", block):
                ...
            else:
                blocks.append(f'<p>{block}</p>')
        return ''.join(blocks)


with open(FILE, "w", encoding='utf-8') as f:
    md = Markdown(f)
    md.h1("Background Color")

    md.h2("Introduction")
    md.block(
        """
        阅读的颜色很重要！

        对于许多计算机用户而言，他们需要每天至少 8 个小时看到屏幕内容。

        多数情况下，他们的看到的都是枯燥的背景和文字，这些情况大大的影响了他们的阅读体验。

        字体色彩几乎有三种选择：与背景

        """)

    md.h2("Examples")
    for name,  bg_color, color in [
        ("Light Gray", "#f5f5f5", "#333333"),
        ("Off-White", "#FFF8F0", "#333333"),
        ("Pale Yellow", "#FFFACD", "#4a4a4a"),
        ("Pale Green", "#C7EDCC", "#2f4f2f"),
        ("Soft Beige (#F5F5DC)", "#F5F5DC", "#4A4A4A"),
        ("Cream (#FAFAD2)", "#FAFAD2", "#333333"),
        ("Light Blue-Gray (#D3E0E9)", "#D3E0E9", "#1c1c4f"),
        ("Muted Light Green (#90EE90)", "#90EE90", "#2E8B57"),
    ]:
        md.h3(name)
        md.raw(
            f'<div style="background: {bg_color};color: {color}">{Markdown.to_html(EXAMPLE_TEXT)}</div>')
