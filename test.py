from find_url import generate_goods_url_list
from item import buff_item,deep_partition
from utils_storage import read_buff_item_from_json
from item_filter import generate_item_list_from_deep_partition
a = read_buff_item_from_json()[0]
b = deep_partition(a,0.01)

# print(a)
# print(a.max_wear)
c = generate_item_list_from_deep_partition(b)
# for i in c:
#     print(i)
    