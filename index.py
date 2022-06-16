import re
from time import sleep

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence
from selenium import webdriver
from selenium.webdriver.common.by import By


def getOpenFlatformData(data: str) -> list:
    """
    正则解析pydantic参数，
    解析出来的数据放到列表allParameters中返回
    :param data:pydantic 参数
    :return:
    """

    data = data.splitlines()

    # 要返回的数据
    allParameters: list = []

    # s = '    field05: Optional[str] = Field(title="字段5",max_length=18, description="预留字段5", default=\'\')'
    for s in data:
        s = s.strip()  # 删除字符转两端空格

        # 判断是否是class数据行
        match = re.match("class", s)
        if match:
            continue

        elif s.find("=") >= 0:
            dic = {}
            match = re.search("(.*):", s)  # 字段名称
            dic['name'] = match.group(1)

            match = re.search("Optional\[(.*?)\]", s)  # 是否必填，匹配到可选，没匹配到必填

            if match:
                # 不点击必填按钮
                dic['click'] = 0
                # 字段类型
                dic['type'] = match.group(1)

            elif not match:
                # 点击必填按钮
                dic['click'] = 1

                # 字段名
                match = re.search(":\s" + "(.*)" + "\s=", s)
                dic['type'] = match.group(1)

            match = re.search("max_length=(\d+),", s)  # 匹配最大长度， 没匹配到就不操作
            if match:
                dic['max_length'] = match.group(1)

            match = re.search("description=\"(.*)\"", s)  # 描述
            if match:
                dic['desc'] = match.group(1)
            allParameters.append(dic)
            continue

        else:
            dic = {}
            match = re.search("(.*):", s)  # 字段名称
            dic['name'] = match.group(1)
            dic['click'] = 1
            dic['type'] = "object"
            dic['desc'] = "入参"
            allParameters.append(dic)
            continue

    return allParameters


class MyRobot(QMainWindow):
    pass


app = QApplication([])
app.setApplicationName("长城机器人")

text = QPlainTextEdit()
window = MyRobot()
window.setMinimumSize(800, 600)
window.setCentralWidget(text)  # 把文本放进框里

menu = window.menuBar().addMenu("输入数据")
test_action = QAction("test-action")


def open_file():
    msg_box = QMessageBox(QMessageBox.Critical, '错误', '出现错误')
    msg_box.exec_()


test_action.triggered.connect(open_file)
menu.addAction(test_action)

open_action = QAction("打开文件")
file_path = None


def open_file():
    path = QFileDialog.getOpenFileName(window, "open")[0]
    if path:
        global input_data
        text.setPlainText(open(path).read())
        file_path = path


open_action.triggered.connect(open_file)
menu.addAction(open_action)

save_input_action = QAction("保存-入参数据")
input_data = None


def save_input_data():
    if text.toPlainText().isspace() or text.toPlainText() == "":
        msg_box = QMessageBox(QMessageBox.Critical, '错误', '保存失败，内容不能为空')
        msg_box.exec_()
    else:
        global input_data
        input_data = text.toPlainText()
        msg_box = QMessageBox(QMessageBox.Critical, '成功', '保存成功，入参数据已保存')
        msg_box.exec_()


save_input_action.triggered.connect(save_input_data)
menu.addAction(save_input_action)

save_out_data = QAction("保存-出参数据")
out_data = None


def save_out_file():
    if text.toPlainText().isspace() or text.toPlainText() == "":
        msg_box = QMessageBox(QMessageBox.Critical, '错误', '保存失败，内容不能为空')
        msg_box.exec_()
    else:
        global out_data
        out_data = text.toPlainText()
        msg_box = QMessageBox(QMessageBox.Critical, '成功', '保存成功，出参数据已保存')
        msg_box.exec_()

save_out_data.triggered.connect(save_out_file)
menu.addAction(save_out_data)

# 入参填充
open_robot = QAction("激活机器人")


def get_data():
    if not input_data and not out_data:
        msg_box = QMessageBox(QMessageBox.Critical, '错误', '没有输入数据')
        msg_box.exec_()

    else:
        browser = webdriver.Chrome(
            executable_path="/Users/wangchangyu/PycharmProjects/article_open_flatform/chromedriver")

        # 打开页面
        page = browser.get('https://open.gwm.cn/')

        sleep(2)  # 进去登录页面
        browser.find_element(by=By.CSS_SELECTOR, value="button.ant-btn").click()

        sleep(2)  # 点击域账号登录
        browser.find_element(by=By.CSS_SELECTOR,
                             value="#userLayout > div.login-block > div.main > div > div.ant-tabs-bar.ant-tabs-top-bar > div > div > div > div > div:nth-child(1) > div:nth-child(2)").click()
        sleep(3)  # 账号名输入
        browser.find_element(by=By.CSS_SELECTOR, value="#account").send_keys("GW00183542")

        msg_box = QMessageBox(QMessageBox.Question, '确认按钮',
                              '点击ok前，确保你已输入密码并进入到要修改的API页面')  # 退出表示弹出框标题，"你确定退出吗？"表示弹出框的内容
        msg_box.exec_()

        """录入入参"""
        if input_data:

            browser.find_element_by_css_selector(
                "#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div:nth-child(3) > button.ant-btn.ant-btn-primary.ant-btn-sm").click()
            sleep(2)

            # 点击参数类型
            browser.find_element(by=By.CSS_SELECTOR,
                                 value="#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div:nth-child(3) > div > div > div > div > div > div > table > tbody > tr > td:nth-child(3) > div.ant-select.ant-select-enabled > div").click()
            # app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div > div > div > div > div > div > table > tbody > tr > td:nth-child(3) > div > div > div > div
            sleep(2)
            browser.find_element(by=By.CSS_SELECTOR,
                                 value="#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div:nth-child(3) > div > div > div > div > div > div > table > tbody > tr > td:nth-child(3) > div:nth-child(2) > div > div > div > ul > li:nth-child(9)").click()
            # browser.find_element(by=By.CSS_SELECTOR, value="#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div:nth-child(3) > div > div > div > div > div > div > table > tbody > tr > td:nth-child(3) > div.ant-select.ant-select-enabled > div").click()
            # browser.find_element(by=By.CSS_SELECTOR, value="#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div:nth-child(3) > div > div > div > div > div > div > table > tbody > tr:nth-child(3) > td:nth-child(3) > div.ant-select.ant-select-enabled > div > div").click()
            # browser.find_element(by=By.CSS_SELECTOR, value="#9b4d762a-acda-409a-ca7b-dad26c8e24ce > ul > li:nth-child(9)").click()

            sleep(2)

            browser.find_element_by_css_selector(
                "#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div:nth-child(3) > div > div > div > div > div > div > table > tbody > tr.ant-table-row.ant-table-row-level-0 > td:nth-child(1) > input").send_keys(
                "root")

            browser.find_element_by_css_selector(
                "#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div:nth-child(3) > div > div > div > div > div > div > table > tbody > tr.ant-table-row.ant-table-row-level-0 > td:nth-child(2) > button").click()

            browser.find_element_by_css_selector(
                "#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div:nth-child(3) > div > div > div > div > div > div > table > tbody > tr.ant-table-row.ant-table-row-level-0 > td:nth-child(4) > input").send_keys(
                100)

            browser.find_element_by_css_selector(
                "#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div:nth-child(3) > div > div > div > div > div > div > table > tbody > tr.ant-table-row.ant-table-row-level-0 > td:nth-child(6) > input").send_keys(
                100)

            sleep(2)

            i = 0
            dataOpenFlatform: list = getOpenFlatformData(input_data)

            while i < len(dataOpenFlatform):
                # browser.find_element_by_css_selector("#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div:nth-child(3) > div > div > div > div > div > div > table > tbody > tr.ant-table-row.ant-table-row-level-0 > td:nth-child(7) > span > a:nth-child(1)").click()
                browser.find_element(by=By.CSS_SELECTOR,
                                     value="#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div:nth-child(3) > div > div > div > div > div > div > table > tbody > tr.ant-table-row.ant-table-row-level-0 > td:nth-child(7) > span > a:nth-child(1)").click()
                i += 1

            ie = 2
            sleep(5)
            browser.find_element(by=By.CSS_SELECTOR,
                                 value="#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div:nth-child(3) > div > div > div > div > div > div > table > tbody > tr > td:nth-child(1) > div").click()
            sleep(1)
            for dat in dataOpenFlatform:
                browser.find_element_by_css_selector(
                    f"#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div:nth-child(3) > div > div > div > div > div > div > table > tbody > tr:nth-child({ie}) > td:nth-child(1) > input").send_keys(
                    dat['name'])
                if dat['click']:
                    browser.find_element_by_css_selector(
                        f"#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div:nth-child(3) > div > div > div > div > div > div > table > tbody > tr:nth-child({ie}) > td:nth-child(2) > button").click()

                # 选择参数类型
                browser.find_element(by=By.CSS_SELECTOR,
                                     value=f"#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div:nth-child(3) > div > div > div > div > div > div > table > tbody > tr:nth-child({ie}) > td:nth-child(3) > div.ant-select.ant-select-enabled > div").click()
                sleep(0.15)
                type_p = dat["type"]
                dic = {"int": 1, "str": 2, "date": 3, "float": 4, "double": 5, "long": 6, "boolean": 7, "array": 8,
                       "object": 9}

                if isinstance(type_int := dic.get(type_p, ""), int):
                    browser.find_element(by=By.CSS_SELECTOR,
                                         value=f"#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div:nth-child(3) > div > div > div > div > div > div > table > tbody > tr:nth-child({ie}) > td:nth-child(3) > div:nth-child(2) > div > div > div > ul > li:nth-child({type_int})").click()

                browser.find_element_by_css_selector(
                    f"#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div:nth-child(3) > div > div > div > div > div > div > table > tbody > tr:nth-child({ie}) > td:nth-child(4) > input").send_keys(
                    dat.get('max_length', ""))
                browser.find_element_by_css_selector(
                    f"#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div:nth-child(3) > div > div > div > div > div > div > table > tbody > tr:nth-child({ie}) > td:nth-child(6) > input").send_keys(
                    dat.get('desc', ""))
                ie += 1

            print("完事")

        """录入出参"""
        if out_data:
            browser.find_element(by=By.CSS_SELECTOR,
                                 value="#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(7) > button.ant-btn.ant-btn-primary.ant-btn-sm").click()

            # 选择参数类型
            browser.find_element(by=By.CSS_SELECTOR,
                                 value="#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(7) > div > div > div > div > div > div > table > tbody > tr > td:nth-child(3) > div.ant-select.ant-select-enabled > div > div").click()
            sleep(0.15)

            browser.find_element(by=By.CSS_SELECTOR,
                                 value="#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(7) > div > div > div > div > div > div > table > tbody > tr > td:nth-child(3) > div:nth-child(2) > div > div > div > ul > li:nth-child(9)").click()

            browser.find_element_by_css_selector(
                "#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(7) > div > div > div > div > div > div > table > tbody > tr > td:nth-child(1) > input").send_keys(
                "root")
            browser.find_element_by_css_selector(
                "#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(7) > div > div > div > div > div > div > table > tbody > tr > td:nth-child(2) > button").click()

            browser.find_element_by_css_selector(
                "#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(7) > div > div > div > div > div > div > table > tbody > tr > td:nth-child(4) > input").send_keys(
                100)

            # app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div:nth-child(3) > div > div > div > div > div > div > table > tbody > tr:nth-child(2) > td:nth-child(4) > input
            browser.find_element_by_css_selector(
                "#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(7) > div > div > div > div > div > div > table > tbody > tr > td:nth-child(6) > input").send_keys(
                100)

            sleep(2)

            i = 0
            # try:
            dataOpenFlatform: list = getOpenFlatformData(out_data)
            # except:
            #     print("解析参数错误")

            while i < len(dataOpenFlatform):
                # browser.find_element_by_css_selector("#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(6) > div:nth-child(3) > div > div > div > div > div > div > table > tbody > tr.ant-table-row.ant-table-row-level-0 > td:nth-child(7) > span > a:nth-child(1)").click()
                browser.find_element(by=By.CSS_SELECTOR,
                                     value="#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(7) > div > div > div > div > div > div > table > tbody > tr > td:nth-child(7) > span > a:nth-child(1)").click()
                i += 1

            ie = 2
            sleep(5)

            browser.find_element(by=By.CSS_SELECTOR,
                                 value="#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(7) > div > div > div > div > div > div > table > tbody > tr.ant-table-row.ant-table-row-level-0 > td:nth-child(1) > div").click()

            sleep(1)

            for dat in dataOpenFlatform:
                browser.find_element_by_css_selector(
                    f"#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(7) > div > div > div > div > div > div > table > tbody > tr:nth-child({ie}) > td:nth-child(1) > input").send_keys(
                    dat['name'])

                if dat['click']:
                    browser.find_element_by_css_selector(
                        f"#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(7) > div > div > div > div > div > div > table > tbody > tr:nth-child({ie}) > td:nth-child(2) > button").click()

                # 选择参数类型
                browser.find_element(by=By.CSS_SELECTOR,
                                     value=f"#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(7) > div > div > div > div > div > div > table > tbody > tr:nth-child({ie}) > td:nth-child(3) > div.ant-select.ant-select-enabled > div > div").click()

                sleep(0.15)

                type_p = dat["type"]

                dic = {"int": 1, "str": 2, "date": 3, "float": 4, "double": 5, "long": 6, "boolean": 7, "array": 8,
                       "object": 9}

                if isinstance(type_int := dic.get(type_p, ""), int):
                    browser.find_element(by=By.CSS_SELECTOR,
                  value=f"#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(7) > div > div > div > div > div > div > table > tbody > tr:nth-child({ie}) > td:nth-child(3) > div:nth-child(2) > div > div > div > ul > li:nth-child({type_int})").click()

                browser.find_element_by_css_selector(
                    f"#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(7) > div > div > div > div > div > div > table > tbody > tr:nth-child({ie}) > td:nth-child(4) > input").send_keys(
                    dat.get('max_length', ""))
                browser.find_element_by_css_selector(
                    f"#app > section > section > main > div > div.mainbody > div.content > div > div.tabs-wapper > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.homenew > div.divRight > div:nth-child(7) > div > div > div > div > div > div > table > tbody > tr:nth-child({ie}) > td:nth-child(6) > input").send_keys(
                    dat.get('desc', ""))
                ie += 1

        msg_box = QMessageBox(QMessageBox.Question, '确认按钮', '确认已经保存后，再关闭程序')  # 退出表示弹出框标题，"你确定退出吗？"表示弹出框的内容
        msg_box.exec_()
        open_robot.triggered.connect(window.close)


open_robot.setShortcut(QKeySequence.Save)
open_robot.triggered.connect(get_data)
menu.addAction(open_robot)

menu.addSeparator()  # 横线
# 退出程序
exit = QAction("退出")
exit.setShortcut(QKeySequence.Close)
exit.triggered.connect(window.close)
menu.addAction(exit)

# 说明
help_menu = window.menuBar().addMenu("帮助")
help_action = QAction('使用说明')


def show_about_dialog():
    about_text = """<center>自己研究吧</center>
    """
    QMessageBox.about(window, "使用说明", about_text)


help_action.triggered.connect(show_about_dialog)
help_menu.addAction(help_action)

window.show()
app.exec_()
