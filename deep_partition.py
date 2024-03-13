from item import buff_item,deep_partition
from utils_storage import read_buff_item_from_json


if __name__ == "__main__":
    buff_item_list = read_buff_item_from_json()
    a = deep_partition(buff_item_list[0],0.01)
    print(a.wear_check_list)