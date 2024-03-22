from item import tradeupitem
from utils_storage import read_wear_list,read_buff_item_from_json

a = (read_wear_list()[0].name,read_wear_list()[0].min_wear)

print(a)