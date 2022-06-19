1:安装依赖-(python3.8-其他版本也可以)
    pip install selenium -i https://pypi.douban.com/simple/
    pip install PyQt5 -i https://pypi.douban.com/simple/
    pip install scrapy -i https://pypi.douban.com/simple/

2：下载Chrome驱动：(不推荐其他浏览器驱动，慢，不稳定)
    ①：查看自己Chrome的版本
    ②：下载对应自己版本的驱动, 替换项目中的chromedriver
        科学上网：https://sites.google.com/chromium.org/driver/

        如果打不卡上面的网址，从下面入口进入
        ⑴ https://selenium-python.readthedocs.io/installation.html
        ⑵ 找到1.5 Drivers， 点击(科学上网) Chrome：后面的地址

3：可能遇到的问题
    1：MacOS 无法打开“chromedriver”，因为无法验证开发者
        xattr -d com.apple.quarantine chromedriver
        # 以上命令绕开苹果公证，需要切换到chromedriver目录下执行

支持Windows，Mac，Ubuntu，CentOS