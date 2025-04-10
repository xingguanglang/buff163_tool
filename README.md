# 半成品, 仅供学习使用 

##### 暂时不想写说明QAQ

还是写一点吧 

1. 下载项目
2. 安装 python 3.11, chrome浏览器和对应版本的playwright库
3. 运行setting_browser.py, 登录buff账号, 登录完成退出浏览器
4. 打开market_filter.py, 修改想要的元素列表 (看不懂就不改), 运行. 该程序会在**json**文件夹中生成**buff_item.json** 文件
5. 打开main.py 并运行. 该程序会在**json**文件夹中生成**storage.json**文件

## 3.25更新

1. 解决安装项目于windows系统会出现json文件命名错误的问题, 解决方法为运行transform_filename.py


# English Version

**Here's a brief guide anyway:**

1. Download the project.

2. Install Python 3.11, Chrome browser, and the corresponding version of Playwright library.

3. Run _setting_browser.py_, log in to your BUFF account, then close the browser after logging in.

4. Open _market_filter.py_, modify the list of elements you want (leave unchanged if you don't understand), and run it. This script will generate a file named buff_item.json in the json folder.

5. Open and run _main.py_. This script will generate a file named storage.json in the json folder.

**Update on March 25**

Fixed the issue where installing the project on Windows caused incorrect JSON filenames. To apply the fix, run transform_filename.py.
