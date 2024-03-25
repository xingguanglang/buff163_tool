from item import tradeupitem,item
from utils_storage import read_wear_list,read_buff_item_from_json,read_item_from_json,read_itemset_from_json
def calculate_itemset_and_wear(item_list:list[item]): 
    output = [[],"",0]
    wear_list = read_wear_list()
    for i in item_list:
        bf_filepath = "json/buff_items" + "_" + i.name +"_.json"
        current_buffitem = read_buff_item_from_json(bf_filepath)
        output[1] = current_buffitem[0].rarity
        #找磨损
        output[2] += i.wear
        output[0].append(i.itemset)
    output[2] /= len(item_list)
    #[0]: 所有材料上级集合, [1]:材料等级, [2]:材料平均磨损
    return output

def calculate_uplevel_items(itemset_list,rarity,filedir="json/"):
    output_item = []
    for i in itemset_list:
        filepath = filedir + "sets" + "_" + i +"_.json"

        current_itemset = read_itemset_from_json(filepath)
        # print("rarity:",rarity)
        if rarity == "隐蔽":
            for j in current_itemset.coverts:
                output_item.append([j])
            print("材料为隐蔽等级,无法炼金")
        elif rarity == "保密":
            for j in current_itemset.coverts:
                output_item.append([j])
        elif rarity == "受限":
            for j in current_itemset.classified:
                output_item.append([j])
        elif rarity == "军规级":
            for j in current_itemset.restricted:
                output_item.append([j])
        elif rarity == "工业级":
            for j in current_itemset.mil_specs:
                output_item.append([j])
        elif i.rarity == "消费级":
            for j in current_itemset.industrials:
                output_item.append([j])

    return output_item 

def calculate_relative_wear(name,avgwear):
    wear_list = read_wear_list()
    for i in wear_list:
        if name == i.name:
            minwear = float(i.min_wear)
            maxwear = float(i.max_wear)
            break
    output_wear = avgwear * (maxwear-minwear) +minwear
    return output_wear

def calculate_output_possibility(item_avgwear,uplevel_items):
    output_dic = {}
    base_possibility = 1/len(uplevel_items)
    for i in uplevel_items:
        #possibility, wear
        for j in i:
            tmp =  calculate_relative_wear(j,item_avgwear)
            output_dic[j] = [0,tmp]

    # base_possibility = 1/len(output_dic.keys())

    for i in uplevel_items:
        for j in i:
            output_dic[j][0] += base_possibility
            

    return output_dic


def tradeup(itemlist:list[item]):
    temp = calculate_itemset_and_wear(itemlist)
    temp2 = calculate_uplevel_items(temp[0],temp[1])
    result = calculate_output_possibility(temp[2],temp2)
    return result

a = read_item_from_json("json/items_法玛斯 | 奈芙蒂斯之河 _.json")

a = [a[0]]*5
a2 = read_item_from_json("json/items_AUG | 湖怪鸟 _.json")
a2 = [a2[2]]*5
print(a[0].wear)
print(a2[0].wear)
result = tradeup(a+a2)
print(result)