from item_filter import create_item_lists_from_deep_partition_list,create_item_lists_from_buff_item_list
from market_filter import create_buff_item_main
from deep_partition import create_deep_partition_from_buff_item_list
from utils_storage import read_buff_item_from_all_json, write_itemset_to_json,read_itemset_from_json
from item import buff_item,itemset
from itemset_operation import create_itemset_class,generate_itemset_item
from utils_storage import read_itemset_from_all_json

buff_item_lists = read_buff_item_from_all_json()

itemset_lists = [("set_community_33","千瓦"),("set_community_32","变革"),
                ("set_community_31","反冲"),("set_community_30","梦魇"),
                ("set_community_29","激流大行动"),("set_community_28","蛇噬"),
                ("set_community_27","狂牙大行动"),("set_community_26","裂空"),
                ("set_community_25","棱彩2号"),("set_community_24","裂网大行动"),
                ("set_community_23","反恐精英20周年"),("set_community_22","棱彩"),
                ("set_community_21","头号特训"),("set_community_20","地平线"),
                ("set_community_19","命悬一线"),("set_community_18","光谱2号"),
                ("set_community_17","九头蛇大行动"),("set_community_16","光谱"),
                ("set_community_15","手套武器箱"),("set_community_14","伽马2号"),
                ("set_community_13","伽马"),("set_community_12","幻彩3号"),
                ("set_community_11","野火大行动"),("set_community_10","左轮武器箱"),
                ("set_community_9","暗影"),("set_community_8","弯曲猎手"),
                ("set_community_7","幻彩2号"),("set_community_6","幻彩"),
                ("set_community_5","先锋"),("set_community_4","突围"),
                ("set_community_3","猎杀者"),("set_community_2","凤凰"),
                ("set_community_1","冬季攻势"),
                ("set_esports","电竞2013"),("set_esports_ii","电竞2013冬季"),("set_esports_iii","电竞2014夏季"),
                ("set_weapons_i","反恐精英武器箱"),("set_weapons_ii","反恐精英2号武器箱"),("set_weapons_iii","反恐精英3号武器箱"),
                ("set_bravo_i","英勇武器箱"),
                ("set_anubis","阿努比斯"),("set_vertigo_2021","2021殒命大厦"),("set_mirage_2021","2021荒漠迷城"),
            ("set_dust_2_2021","2021炽热沙城"),("set_train_2021","2021列车停放站"),("set_op10_ancient","远古遗迹"),
            ("set_op10_ct","控制收藏品"),("set_op10_t","浩劫收藏品"),("set_norse","挪威人收藏品"),
            ("set_canals","运河水城"),("set_stmarc","圣马克镇"),("set_inferno_2","2018炼狱小镇"),
            ("set_nuke_2","2018核子危机"),("set_gods_and_monsters","神魔收藏品"),("set_chopshop","解体厂收藏品"),
            ("set_kimono","旭日收藏品"),("set_cache","死城之谜"),("set_overpass","死亡游乐园"),
            ("set_cobblestone","古堡激战"),("set_baggage","行李仓库"),("set_bank","金库危机"),
            ("set_dust_2","炽热沙城2"),("set_train","列车停放站"),("set_mirage","荒漠迷城"),
            ("set_italy","意大利小镇"),("set_lake","湖畔激战"),("set_safehouse","安全处所"),
            ("set_bravo_ii","无畏收藏品"),("set_dust","炽热沙城"),("set_aztec","雨林遗迹"),
            ("set_vertigo","殒命大厦"),("set_inferno","炼狱小镇"),("set_militia","佣兵训练营"),
            ("set_nuke","核子危机"),("set_office","办公室"),("set_assault","仓库突击"),
                ]
if __name__ =="__main__":
    result = []
    name = [x[1] for x in itemset_lists]
    create_itemset_class(buff_item_lists,name)
    a= read_itemset_from_json("json/sets_光谱_.json")
    print(a)
    # generate_itemset_item(a)
    a = read_itemset_from_all_json()
    for i in a:
        generate_itemset_item(i)
