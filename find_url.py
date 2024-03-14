from item import buff_item,deep_partition
#1:崭新 2:略磨 3:酒精 4:破损 5:战痕


def generate_goods_url(buff_item:buff_item,tab:str="selling",page_num:int=1,sort_by:str="price.asc"):
    buff_id = buff_item.buff_id
    min_wear = buff_item.min_wear
    max_wear = buff_item.max_wear
    url = f'https://buff.163.com/goods/{buff_id}#={tab}&page_num={page_num}&sort_by={sort_by}&min_paintwear={min_wear}&max_paintwear={max_wear}'
    return url

def generate_goods_url_list(deep_partition:deep_partition,tab:str="selling",page_num:int=1,sort_by:str="price.asc"):
    buff_id = deep_partition.buff_item.buff_id
    result = []
    for i in range(len(deep_partition.wear_check_list)-1):
        min_wear = deep_partition.wear_check_list[i] 
        max_wear = deep_partition.wear_check_list[i+1]
        result.append(f'https://buff.163.com/goods/{buff_id}#={tab}&page_num={page_num}&sort_by={sort_by}&min_paintwear={min_wear}&max_paintwear={max_wear}')
    return result
