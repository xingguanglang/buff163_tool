from item import buff_item,itemset,create_itemset_by_listing
from utils_storage import write_itemset_to_json,read_deep_partition_from_json
from item_filter import create_item_main,generate_item_list_from_deep_partition,generate_item_list_from_buff_item,create_item_lists_from_deep_partition_list
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
            filepath = "json/deep_partitions_"+i+"_.json"
            create_item_main(read_deep_partition_from_json(filepath))
    return 

if __name__ == "__main__":
    create_item_lists_from_deep_partition_list