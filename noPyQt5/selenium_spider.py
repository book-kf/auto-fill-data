from time import sleep

from selenium import webdriver
from noPyQt5.data import data
from testP import getOpenFlatformData
from selenium.webdriver.common.by import By
browser = webdriver.Chrome(executable_path="/chromedriver")


def main():

    """
    页面操作
    """
    # 打开页面
    page = browser.get('https://open.gwm.cn/')

    sleep(2) #进去登录页面
    browser.find_element(by=By.CSS_SELECTOR, value="button.ant-btn").click()

    sleep(2) # 点击域账号登录
    browser.find_element(by=By.CSS_SELECTOR, value="#userLayout > div.login-block > div.main > div > div.ant-tabs-bar.ant-tabs-top-bar > div > div > div > div > div:nth-child(1) > div:nth-child(2)").click()
    sleep(3) # 账号名输入
    browser.find_element(by=By.CSS_SELECTOR, value="#account").send_keys("GW00183542")
    # browser.find_element_by_css_selector("#account").send_keys("GW00183542")
    input("请输入密码，并进入到要录入参数的api页面, 准备好输入1,继续向下执行:")

    """
    增加参数
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
    input("给root选择一个object对象:")
    # browser.find_element_by_css_selector("#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div:nth-child(3) > div > div > div > div > div > div > table > tbody > tr.ant-table-row.ant-table-row-level-0 > td:nth-child(3) > div.ant-select.ant-select-enabled > div").click()

    i = 0

    while i < len(dataOpenFlatform):
        # browser.find_element_by_css_selector("#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div:nth-child(3) > div > div > div > div > div > div > table > tbody > tr.ant-table-row.ant-table-row-level-0 > td:nth-child(7) > span > a:nth-child(1)").click()
        browser.find_element(by=By.CSS_SELECTOR, value="#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div:nth-child(3) > div > div > div > div > div > div > table > tbody > tr.ant-table-row.ant-table-row-level-0 > td:nth-child(7) > span > a:nth-child(1)").click()
        i += 1

    ie = 2
    sleep(10)
    for dat in dataOpenFlatform:
        browser.find_element_by_css_selector(f"#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div:nth-child(3) > div > div > div > div > div > div > table > tbody > tr:nth-child({ie}) > td:nth-child(1) > input").send_keys(dat['name'])
        if dat['click']:
            browser.find_element_by_css_selector(f"#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div:nth-child(3) > div > div > div > div > div > div > table > tbody > tr:nth-child({ie}) > td:nth-child(2) > button").click()
        browser.find_element_by_css_selector(f"#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div:nth-child(3) > div > div > div > div > div > div > table > tbody > tr:nth-child({ie}) > td:nth-child(4) > input").send_keys(dat.get('max_length',""))
        browser.find_element_by_css_selector(f"#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div:nth-child(3) > div > div > div > div > div > div > table > tbody > tr:nth-child({ie}) > td:nth-child(6) > input").send_keys(dat.get('desc',""))
        ie += 1

if __name__ == "__main__":
    main()
