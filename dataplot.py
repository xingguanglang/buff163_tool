from matplotlib import pyplot as plt
from item import item
from math import log10
def plot_graphsets_of(items:list[item]):
    wears = [i.wear for i in items]
    prices = [i.price for i in items]
    slopes = [[i.price/i.wear for i in items]]
    logs = [log10(i.price/i.wear) for i in items]
    fig, axs = plt.subplots(1, 3, figsize=(15, 5)) # 1行2列

    # 第一个散点图
    axs[0].scatter(wears, prices)
    axs[0].set_xlabel('wear')
    axs[0].set_ylabel('price')

    # 第二个散点图
    axs[1].scatter(wears, slopes)
    axs[1].set_xlabel('wear')
    axs[1].set_ylabel('price per wear')

    axs[2].scatter(wears, logs)
    axs[2].set_xlabel('wear')
    axs[2].set_ylabel('price per wear(log)')
    plt.show()

if __name__ == "__main__":
    print()