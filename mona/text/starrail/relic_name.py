import random
from mona.text.text_generator import TextGenerator

# https://github.com/Mar-7th/StarRailRes/blob/master/index_new/cn/relics.json
relic_name = [
    # 云无留迹的过客
    '过客的逢春木簪',
    '过客的游龙臂鞲',
    '过客的残绣风衣',
    '过客的冥途游履',
    # 野穗伴行的快枪手
    '快枪手的野穗毡帽',
    '快枪手的粗革手套',
    '快枪手的猎风披肩',
    '快枪手的铆钉马靴',
    # 净庭教宗的圣骑士
    '圣骑的宽恕盔面',
    '圣骑的沉默誓环',
    '圣骑的肃穆胸甲',
    '圣骑的秩序铁靴',
    # 密林卧雪的猎人
    '雪猎的荒神兜帽',
    '雪猎的巨蜥手套',
    '雪猎的冰龙披风',
    '雪猎的鹿皮软靴',
    # 街头出身的拳王
    '拳王的冠军护头',
    '拳王的重炮拳套',
    '拳王的贴身护胸',
    '拳王的弧步战靴',
    # 戍卫风雪的铁卫
    '铁卫的铸铁面盔',
    '铁卫的银鳞手甲',
    '铁卫的旧制军服',
    '铁卫的白银护胫',
    # 熔岩锻铸的火匠
    '火匠的黑曜目镜',
    '火匠的御火戒指',
    '火匠的阻燃围裙',
    '火匠的合金义肢',
    # 繁星璀璨的天才
    '天才的超距遥感',
    '天才的频变捕手',
    '天才的元域深潜',
    '天才的引力漫步',
    # 激奏雷电的乐队
    '乐队的偏光墨镜',
    '乐队的巡演手绳',
    '乐队的钉刺皮衣',
    '乐队的铆钉短靴',
    # 晨昏交界的翔鹰
    '翔鹰的长喙头盔',
    '翔鹰的鹰击指环',
    '翔鹰的翼装束带',
    '翔鹰的绒羽绑带',
    # 流星追迹的怪盗
    '怪盗的千人假面',
    '怪盗的绘纹手套',
    '怪盗的纤钢爪钩',
    '怪盗的流星快靴',
    # 盗匪荒漠的废土客
    '废土客的呼吸面罩',
    '废土客的荒漠终端',
    '废土客的修士长袍',
    '废土客的动力腿甲',
    # 宝命长存的莳者
    '莳者的复明义眼',
    '莳者的机巧木手',
    '莳者的承露羽衣',
    '莳者的天人丝履',
    # 骇域漫游的信使
    '信使的全息目镜',
    '信使的百变义手',
    '信使的密信挎包',
    '信使的酷跑板鞋',
    # 毁烬焚骨的大公
    '大公的冥焰冠冕',
    '大公的绒火指套',
    '大公的蒙恩长袍',
    '大公的绅雅礼靴',
    # 幽锁深牢的系囚
    '系囚的合啮拘笼',
    '系囚的铅石梏铐',
    '系囚的幽闭缚束',
    '系囚的绝足锁桎',
    # 死水深潜的先驱
    '先驱的绝热围壳',
    '先驱的虚极罗盘',
    '先驱的密合铅衣',
    '先驱的泊星桩锚',
    # 机心戏梦的钟表匠
    '钟表匠的极目透镜',
    '钟表匠的交运腕表',
    '钟表匠的空幻礼服',
    '钟表匠的隐梦革履',
    # 荡除蠹灾的铁骑
    '铁骑的索敌战盔',
    '铁骑的摧坚铁腕',
    '铁骑的银影装甲',
    '铁骑的行空护胫',
    # 风举云飞的勇烈
    '勇烈的玄枵面甲',
    '勇烈的钩爪腕甲',
    '勇烈的飞翎瓷甲',
    '勇烈的逐猎腿甲',
    # 太空封印站
    '「黑塔」的空间站点',
    '「黑塔」的漫历轨迹',
    # 不老者的仙舟
    '罗浮仙舟的天外楼船',
    '罗浮仙舟的建木枝蔓',
    # 泛银河商业公司
    '公司的巨构总部',
    '公司的贸易航道',
    # 筑城者的贝洛伯格
    '贝洛伯格的存护堡垒',
    '贝洛伯格的铁卫防线',
    # 星体差分机
    '螺丝星的机械烈阳',
    '螺丝星的环星孔带',
    # 停转的萨尔索图
    '萨尔索图的移动城市',
    '萨尔索图的晨昏界线',
    # 盗贼公国塔利亚
    '塔利亚的钉壳小镇',
    '塔利亚的裸皮电线',
    # 生命的翁瓦克
    '翁瓦克的诞生之岛',
    '翁瓦克的环岛海岸',
    # 繁星竞技场
    '泰科铵的镭射球场',
    '泰科铵的弧光赛道',
    # 折断的龙骨
    '伊须磨洲的残船鲸落',
    '伊须磨洲的坼裂缆索',
    # 苍穹战线格拉默
    '格拉默的铁骑兵团',
    '格拉默的寂静坟碑',
    # 梦想之地匹诺康尼
    '匹诺康尼的堂皇酒店',
    '匹诺康尼的逐梦轨道',
    # 无主荒星茨冈尼亚
    '茨冈尼亚的母神卧榻',
    '茨冈尼亚的轮回纽结',
    # 出云显世与高天神国
    '出云的祸津众神',
    '出云的终始一刀',
    # 奔狼的都蓝王朝
    '都蓝的穹窿金帐',
    '都蓝的器兽缰辔',
    # 劫火莲灯铸炼宫
    '铸炼宫的莲华灯芯',
    '铸炼宫的焰轮天绸',
    # 沉陆海域露莎卡
    '露莎卡的水朽苍都',
    '露莎卡的双生航道',
    # 奇想蕉乐园
    '蕉乐园的蕉芯广场',
    '蕉乐园的模因线缆',
]

class StarrailRelicNameGenerator(TextGenerator):
    def __init__(self):
        super(StarrailRelicNameGenerator, self).__init__("Starrail Relic Name")

    def generate_text(self):
        return random.choice(relic_name)

    def get_lexicon(self):
        ret = set()
        for name in relic_name:
            for c in name:
                ret.add(c)
        return ret
