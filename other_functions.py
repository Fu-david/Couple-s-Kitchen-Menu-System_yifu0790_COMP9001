import tkinter as tk
import json
import re           
import webbrowser
import os
import sys
import webbrowser
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt


# show window
def show_order_window(message: str,
                      title: str = "Order Message",
                      size: tuple[int, int] = (520, 360)):
    """
    固定大小的弹窗，文本左对齐；当文字过多时出现上下滚动条。
    - 无按钮（只有窗口标题栏可关闭）
    - 文本不可编辑
    - message 中的 http(s) 链接自动识别为可点击超链接
    """
    root = tk.Tk()
    root.title(title)
    root.resizable(False, False)
    width, height = size

    # 置顶
    root.attributes("-topmost", True)
    root.lift()
    root.focus_force()

    # 居中
    sw, sh = root.winfo_screenwidth(), root.winfo_screenheight()
    x, y = (sw - width) // 2, (sh - height) // 2
    root.geometry(f"{width}x{height}+{x}+{y}")

    # 容器框架
    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True)

    # 滚动条（垂直）
    scrollbar = tk.Scrollbar(frame, orient="vertical")
    scrollbar.pack(side="right", fill="y")

    # 文本区：左对齐，按单词换行
    text = tk.Text(
        frame,
        wrap="word",            # 单词换行
        font=("Segoe UI", 12),
        padx=10, pady=10
    )
    text.pack(side="left", fill="both", expand=True)

    # 连接滚动条
    text.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=text.yview)

    # 先以可编辑状态插入文本
    text.insert("1.0", message)

    # 将 message 中的 URL 识别为可点击的超链接 
    # 说明：使用正则匹配 http(s) 开头的链接，然后给每个链接打上唯一 tag，
    # 设置为蓝色+下划线，并绑定点击打开默认浏览器。
    url_pattern = re.compile(r"https?://[^\s]+")
    i = 0
    for m in url_pattern.finditer(message):
        url = m.group(0)

        # 在 Text 中查找该 URL 的位置（可能有多处，逐一打 tag）
        start = text.search(url, "1.0", stopindex="end")
        while start:
            end = f"{start}+{len(url)}c"
            tag_name = f"link_{i}"
            i += 1

            # 添加 tag、设置样式
            text.tag_add(tag_name, start, end)
            text.tag_config(tag_name, foreground="blue", underline=True)

            # 鼠标进入/离开时改变指针形状
            text.tag_bind(tag_name, "<Enter>", lambda e: e.widget.config(cursor="hand2"))
            text.tag_bind(tag_name, "<Leave>", lambda e: e.widget.config(cursor="xterm"))

            # 点击事件：打开浏览器
            def open_url(event, _url=url):
                webbrowser.open(_url)

            text.tag_bind(tag_name, "<Button-1>", open_url)

            # 查找同一 URL 的下一处出现位置（避免死循环）
            start = text.search(url, end, stopindex="end")

    # 设为只读（禁用编辑；tag 的点击绑定仍然生效）
    text.config(state="disabled")

    root.mainloop()

#check order 
def show_order(teammate, username , teamname):

    try:
        filename_order_dish = f"{teammate}_ordered_dish.json"
        with open(filename_order_dish, 'r', encoding='utf-8') as f:
            teammate_order = json.load(f)
 
    except FileNotFoundError:
        return False,""
    
    file_name_menu_user = f"{teamname}_{username}_menu.json" 
    file_name_refrigerator = f"{teamname}_refrigerator.json"
    with open(file_name_menu_user, 'r', encoding='utf-8') as f:
        menu_user = json.load(f)
    with open(file_name_refrigerator, 'r', encoding='utf-8') as f:
        refrigerator = json.load(f)

    def missing_ingredients(dish_name: str, recipes=menu_user, fridge=refrigerator) -> list:
        """
        根据菜名返回缺少的原材料列表。
        
        参数：
            dish_name: 菜名（字符串）
            recipes: {菜名: [原材料列表]}
            fridge: 冰箱已有材料列表
        
        返回：
            缺少的原材料列表（如果菜不存在，返回空列表）
        """
        if dish_name not in recipes:
            return []  # 菜名不存在
        
        ingredients = recipes[dish_name]
        missing = [item for item in ingredients if item not in fridge]
        return missing

    title_message = f"💗💗💗 {teammate} ORDER 🌹🌹🌹\n"
    message = ""
    n = 0
    for dish in teammate_order['dish_ordered_in']:
        n += 1
        missing = missing_ingredients(dish)
        if missing:
            message += f"{n}. {dish} LACK❌: {', '.join(missing)}\n"
        else:
            message += f"{n}. {dish} lack nothing.\n"
    if len(teammate_order) == 2:
        ordered_other_count = len(teammate_order['dish_ordered_other'])
        message += f"\nYour teammate ordered {ordered_other_count} dishes that are not in your menu.\n"
        i = 0
        for dish in teammate_order['dish_ordered_other']:
            i += 1
            dish_name = dish.replace(" ", "+")
            link = f"https://www.allrecipes.com/search?q={dish_name}"
            message += f"{i}. {dish}  cooking recipe link 🖥️ : {link}\n"
    full_message = title_message + message
    os.remove(filename_order_dish)
    return True , full_message

#search missing ingredients
def missing_ingredients(dish_name: str, teamname:str, username:str) -> list:
    """
    根据菜名返回缺少的原材料列表。
    
    参数：
        dish_name: 菜名（字符串）
        recipes: {菜名: [原材料列表]}
        fridge: 冰箱已有材料列表
    
    返回：
        缺少的原材料列表（如果菜不存在，返回空列表）
    """
    file_name_menu_user = f"{teamname}_{username}_menu.json"         
    file_name_refrigerator = f"{teamname}_refrigerator.json"
    #print(file_name_menu_user)
    #print(file_name_menu_teammate)
    #print(file_name_refrigerator)
    try:  
        with open(file_name_menu_user, 'r', encoding='utf-8') as f:
            recipes = json.load(f)
    except FileNotFoundError:
        recipes = {}

    try:
        with open(file_name_refrigerator, 'r', encoding='utf-8') as f:
            fridge = json.load(f)
    except FileNotFoundError:
        fridge= {}

    if dish_name not in recipes:
        return []  # 菜名不存在
    
    ingredients = recipes[dish_name]
    missing = [item for item in ingredients if item not in fridge]
    return missing


class RecommendDialog(QDialog):
    def __init__(self, recipes: dict[str, list[str]]):
        super().__init__()
        self.setWindowTitle('Recommended Dishes')
        self.resize(560, 320)

        # —— 总在最前 —— 
        self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
        self.setModal(True)

        self.items = list(recipes.items())
        self.idx = 0
        self.showing_ing = False

        # ====== UI ======
        self.lbl = QLabel('', alignment=Qt.AlignCenter)

        # 关键：强制按富文本解析 + 允许鼠标点击链接 + 不让 QLabel 自己打开（我们手动打开）
        self.lbl.setTextFormat(Qt.RichText)
        self.lbl.setTextInteractionFlags(Qt.LinksAccessibleByMouse | Qt.TextSelectableByMouse)
        self.lbl.setOpenExternalLinks(False)
        self.lbl.linkActivated.connect(lambda url: webbrowser.open(url))  # 手动打开默认浏览器

        self.lbl.setStyleSheet('font-size:14px;')

        self.btn_box = QHBoxLayout()
        self.btn_box.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout(self)
        layout.addWidget(self.lbl)
        layout.addLayout(self.btn_box)

        self.refresh()

    def clear_buttons(self):
        while self.btn_box.count():
            item = self.btn_box.takeAt(0)
            w = item.widget()
            if w:
                w.deleteLater()

    def refresh(self):
        if self.idx >= len(self.items):
            self.lbl.setText('All recommendations have been shown.')
            self.clear_buttons()
            ok = QPushButton('OK')
            ok.clicked.connect(self.accept)
            self.btn_box.addWidget(ok)
            return

        dish, ingredients = self.items[self.idx]

        if not self.showing_ing:
            self.lbl.setText(f'Recommend dish name:<br><br>{dish}')
            self.clear_buttons()
            yes = QPushButton('Yes')
            no = QPushButton('No')
            yes.clicked.connect(self.on_yes)
            no.clicked.connect(self.on_no)
            self.btn_box.addWidget(yes)
            self.btn_box.addWidget(no)
        else:
            ing_text = ', '.join(ingredients) if ingredients else '(You do not need to buy any ingredient!)'
            url = f'https://www.allrecipes.com/search?q={dish.replace(" ", "+")}'

            html = (
                f'[{dish}]<br>need you to buy ingredients : <br>{ing_text}'
                #f'Cooking Tutorial：<br>' 
                #f'<a href>{url}</a>'
            )
            self.lbl.setText(html)

            self.clear_buttons()
            ok = QPushButton('OK')
            ok.clicked.connect(self.accept)
            self.btn_box.addWidget(ok)

    def on_yes(self):
        self.showing_ing = True
        self.refresh()

    def on_no(self):
        self.idx += 1
        self.showing_ing = False
        self.refresh()



def show_recommend_window(recommend_dict: dict[str, list[str]]):
    app = QApplication.instance() or QApplication(sys.argv)

    dlg = RecommendDialog(recommend_dict)
    dlg.setWindowFlag(Qt.WindowStaysOnTopHint, True)
    dlg.show()
    dlg.raise_()
    dlg.activateWindow()
    app.setActiveWindow(dlg)
    dlg.exec_()


# test
if __name__ == "__main__":
    while True:
        user_command = input("do you want to display recommend window?")
        if user_command.lower() == "y":
            recipes_demo = {
                "番茄炒蛋": ["鸡蛋", "番茄", "盐", "油"],
                "青椒牛肉": ["牛肉", "青椒", "酱油", "蒜", "姜"],
                "清蒸鱼": ["鱼", "姜", "葱", "蒸鱼豉油"],
                "凉拌黄瓜": ["黄瓜", "蒜", "盐", "香油"]
            }
            show_recommend_window(recipes_demo)

    """    message_T_F , content = show_order("sam","david","loveFamily")
    if message_T_F:
        show_order_window(content)"""



    