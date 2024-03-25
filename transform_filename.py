from os import rename, listdir
def changename(filedir):
    for i in listdir(filedir):
        temp = i
        tmp = ""
        cnt = 0
        for j in temp.split("|"):
            tmp += j
            if cnt != 1:
                tmp += "_"
            cnt += 1
        print(tmp)
        rename(filedir+i,filedir+tmp)

def recovername(filedir):
    for i in listdir(filedir):
        temp = i
        tmp = ""
        cnt = 0
        status = False
        if i =="buff_items_AWP _ _嘣_ _.json":
            rename(filedir+i,"buff_items_AWP | *嘣* _.json")
        elif i == "items_AWP _ _嘣_ _.json":
            rename(filedir+i,"items_AWP | *嘣* _.json")
        elif i == "deep_partitions_AWP _ _嘣_ _.json":
            rename(filedir+i,"deep_partitions_AWP | *嘣* _.json")

        for j in temp.split("_"):
            if temp.split("_")[0][0] != 'b' or temp.split("_")[0][0] != 'd':
                tmp += j
                if cnt ==2:
                    tmp += "|"
                else:
                    tmp += "_"
            else: break
            cnt += 1
        tmp = tmp[:-2]
        # print(tmp)
        rename(filedir+i,filedir+tmp)

if __name__ == "__main__":
    recovername("/users/huoxingwangyou/downloads/buff163_tool-main/json/")
