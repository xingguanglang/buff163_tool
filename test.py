from matplotlib import pyplot as plt
from find_url import generate_goods_url_list
from item import buff_item,deep_partition
from utils_storage import read_buff_item_from_json,write_item_to_json,read_item_from_json
from item_filter import generate_item_list_from_deep_partition
# a = read_buff_item_from_json()[10]
# b = deep_partition(a,0.005)

# c = generate_item_list_from_deep_partition(b)
# write_item_to_json(c)
c = read_item_from_json()
wears = [x.wear for x in c]
prices = [x.price for x in c]
slopes = [x.price/x.wear for x in c]

fig, axs = plt.subplots(1, 2, figsize=(10, 5)) # 1行2列

# 第一个散点图
axs[0].scatter(wears, prices)
axs[0].set_title('第一幅散点图')
axs[0].set_xlabel('list a1')
axs[0].set_ylabel('list b1')

# 第二个散点图
axs[1].scatter(wears, slopes)
axs[1].set_title('第二幅散点图')
axs[1].set_xlabel('list a2')
axs[1].set_ylabel('list b2')
plt.show()