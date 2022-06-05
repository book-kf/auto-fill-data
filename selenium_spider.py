from time import sleep

from selenium import webdriver
from scrapy.selector import Selector
from data import data
from testP import getOpenFlatformData
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome(executable_path="/Users/wangchangyu/PycharmProjects/article_open_flatform/chromedriver")

# browser.get("https://open.gwm.cn/")

# browser.find_element_by_css_selector("button.ant-btn").click()
# print(browser.page_source)

def main():

    """
    页面操作
    """
    # 打开页面
    page = browser.get('https://open.gwm.cn/')

    sleep(2) #进去登录页面
    browser.find_element_by_css_selector("button.ant-btn").click()

    sleep(2) # 点击域账号登录
    browser.find_element_by_css_selector("#userLayout > div.login-block > div.main > div > div.ant-tabs-bar.ant-tabs-top-bar > div > div > div > div > div:nth-child(1) > div:nth-child(2)").click()
    sleep(3) # 账号名输入
    browser.find_element_by_css_selector("#account").send_keys("GW00183542")

    sleep(50)  # TODO 需要手动输入密码
    # browser.find_element_by_css_selector("#password").send_keys("fly123456@")
    # 进入控制台
    # browser.find_element_by_css_selector("#app > div > div.header-animat.user-client > header > div > div.right-wapper > div.block.rightAction > span").click()

    # sleep(40)
    # TODO 手动进入到自己要录入参数的领域，详情→修改

    """
    开始增加参数
    """
    browser.find_element_by_css_selector("#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div:nth-child(3) > button.ant-btn.ant-btn-primary.ant-btn-sm").click()

    sleep(3)
    # 解析参数，得到填入开放平台的数据
    try:
        dataOpenFlatform: list = getOpenFlatformData(data)
    except:
        print("解析参数错误")

    browser.find_element_by_css_selector("#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div:nth-child(3) > div > div > div > div > div > div > table > tbody > tr.ant-table-row.ant-table-row-level-0 > td:nth-child(1) > input").send_keys("root")
    #app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div:nth-child(3) > div > div > div > div > div > div > table > tbody > tr:nth-child(12) > td:nth-child(1) > input
    browser.find_element_by_css_selector("#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div:nth-child(3) > div > div > div > div > div > div > table > tbody > tr.ant-table-row.ant-table-row-level-0 > td:nth-child(2) > button").click()
    #app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div:nth-child(3) > div > div > div > div > div > div > table > tbody > tr:nth-child(2) > td:nth-child(2) > button
    browser.find_element_by_css_selector("#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div:nth-child(3) > div > div > div > div > div > div > table > tbody > tr.ant-table-row.ant-table-row-level-0 > td:nth-child(4) > input").send_keys(88)
    #app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div:nth-child(3) > div > div > div > div > div > div > table > tbody > tr:nth-child(2) > td:nth-child(4) > input
    browser.find_element_by_css_selector("#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div:nth-child(3) > div > div > div > div > div > div > table > tbody > tr.ant-table-row.ant-table-row-level-0 > td:nth-child(6) > input").send_keys(99)

    sleep(10) #选择下拉框
    # browser.find_element_by_css_selector("#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div:nth-child(3) > div > div > div > div > div > div > table > tbody > tr.ant-table-row.ant-table-row-level-0 > td:nth-child(3) > div.ant-select.ant-select-enabled > div").click()
    # browser.find_element_by_css_selector("#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div:nth-child(3) > div > div > div > div > div > div > table > tbody > tr.ant-table-row.ant-table-row-level-0 > td:nth-child(3) > div.ant-select.ant-select-enabled > div").click()
    #app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div:nth-child(3) > div > div > div > div > div > div > table > tbody > tr.ant-table-row.ant-table-row-level-0 > td:nth-child(3) > div.ant-select.ant-select-open.ant-select-focused.ant-select-enabled > div > div > div.ant-select-selection__placeholder
    # sleep(3)
    # browser.find_element_by_css_selector("#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div:nth-child(3) > div > div > div > div > div > div > table > tbody > tr.ant-table-row.ant-table-row-level-0 > td:nth-child(3) > div.ant-select.ant-select-open.ant-select-focused.ant-select-enabled > div > div > div.ant-select-selection__placeholder").send_keys(Keys.DOWN)

    # select= Select(sel)
    # select.select_by_visible_text('object')
    sleep(5)
    i = 0
    while i < len(dataOpenFlatform):
        browser.find_element_by_css_selector("#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div:nth-child(3) > div > div > div > div > div > div > table > tbody > tr.ant-table-row.ant-table-row-level-0 > td:nth-child(7) > span > a:nth-child(1)").click()
        i += 1
    ie = 2
    sleep(10)
    for dat in dataOpenFlatform:
        browser.find_element_by_css_selector(f"#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div:nth-child(3) > div > div > div > div > div > div > table > tbody > tr:nth-child({ie}) > td:nth-child(1) > input").send_keys(dat['name'])
        if dat['click']:
            browser.find_element_by_css_selector(f"#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div:nth-child(3) > div > div > div > div > div > div > table > tbody > tr:nth-child({ie}) > td:nth-child(2) > button").click()
        browser.find_element_by_css_selector(f"#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div:nth-child(3) > div > div > div > div > div > div > table > tbody > tr:nth-child({ie}) > td:nth-child(4) > input").send_keys(dat.get('max_length',""))
        browser.find_element_by_css_selector(f"#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div:nth-child(3) > div > div > div > div > div > div > table > tbody > tr:nth-child({ie}) > td:nth-child(6) > input").send_keys(dat.get('desc',""))
        ie+=1

if __name__ == "__main__":
    main()
