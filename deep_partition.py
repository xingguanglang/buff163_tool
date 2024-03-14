from item import buff_item,deep_partition
from utils_storage import write_deep_partition_to_json,read_buff_item_from_json

def create_deep_partition_from_buff_item_list(buff_item_list:list[buff_item],interval = -1):
    result = []
    for i in buff_item_list:
        print(interval)
        if interval == -1:
            if i.exterior == "崭新出厂":
                result.append(deep_partition(i,0.01))
            elif i.exterior == "略有磨损":
                result.append(deep_partition(i,0.01))
            elif i.exterior == "久经沙场":
                result.append(deep_partition(i,0.03))
            elif i.exterior == "破损不堪":
                result.append(deep_partition(i,0.02))
            elif i.exterior == "战痕累累":
                result.append(deep_partition(i,0.11))
    write_deep_partition_to_json(result)
    return result

if __name__ == "__main__":
    a = read_buff_item_from_json("json/buff_items_SSG 08 | 炎龙之焰 _.json")
    print(a)
    b = create_deep_partition_from_buff_item_list(a)
    print(b[0].interval,b[1].interval,b[1].exterior)