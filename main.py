from item_filter import create_item_lists_from_deep_partition_list,create_item_lists_from_buff_item_list
from market_filter import create_buff_item_main
from deep_partition import create_deep_partition_from_buff_item_list
#type 1

a = create_buff_item_main()

b = create_deep_partition_from_buff_item_list(a)

c = create_item_lists_from_deep_partition_list(b)

#type 2

# a = create_buff_item_main()

# b = create_item_lists_from_buff_item_list(a)