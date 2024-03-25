from item import buff_item,itemset,create_itemset_by_listing
from utils_storage import read_buff_item_from_json,write_itemset_to_json,read_deep_partition_from_all_json,read_deep_partition_from_json
# from item_filter import create_item_main,generate_item_list_from_deep_partition,generate_item_list_from_buff_item,create_item_lists_from_deep_partition_list
from itemfilter import create_item_lists_from_buff_item_list
def create_itemset_class(buff_items:list[buff_item],namelist:list[str]):
    result = [] 
    for name in namelist:
        result.append(itemset(name,buff_items))
    write_itemset_to_json(result)
    return result
def generate_itemset_item(itemset:itemset):
    tmp = [itemset.coverts,itemset.classified,itemset.restricted,itemset.mil_specs,itemset.industrials,itemset.consummers]
    for a in tmp:
        for i in a:
            filepath = "json/buff_items_"+i+"_.json"
            create_item_lists_from_buff_item_list(read_buff_item_from_json(filepath))
    return 

if __name__ == "__main__":
    a = read_deep_partition_from_all_json()
    create_itemset_class()