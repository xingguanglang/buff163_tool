from find_url import generate_goods_url_list
from item import buff_item,deep_partition
from utils_storage import read_buff_item_from_json
from item_filter import generate_item_list_from_buff_item
a = read_buff_item_from_json()[0]
b = deep_partition(a,0.01)
c = generate_goods_url_list(b)
# print(a)
# print(a.max_wear)
for i in b.wear_check_list:
    print(i)
    c = generate_item_list_from_buff_item(i)
    