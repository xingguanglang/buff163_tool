from item import item,buff_item
#1:崭新 2:略磨 3:酒精 4:破损 5:战痕
from utils_storage import read_buff_item_from_json

def retrieve_buff_id_from_name(name,type):
    name_dic = read_name_dic()
    result:buff_item = name_dic[(name,type)]
    return result

def read_name_dic():
    buff_item_list = list[buff_item](read_buff_item_from_json())
    name_dic = {}
    for i in buff_item_list:
        name_dic[(i.name,i.exterior)] = i
    return name_dic

def generate_goods_url(buff_item:buff_item,tab:str="selling",page_num:int=1,sort_by:str="price.asc"):
    buff_id = buff_item.buff_id
    min_wear = buff_item.min_wear
    max_wear = buff_item.max_wear
    url = f'https://buff.163.com/goods/{buff_id}#={tab}&page_num={page_num}&sort_by={sort_by}&min_paintwear={min_wear}&max_paintwear={max_wear}'
    return url





if __name__ == "__main__":
    name_dic = read_name_dic()
    print(name_dic)
