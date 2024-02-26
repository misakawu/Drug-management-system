# 导入界面模块
from tkinter import *
# 导入表格模具
from tkinter.ttk import Treeview
# 导入dao层
from dao.bookdao import BookDao
# 导入弹框
from tkinter.simpledialog import *
# 导入提示框
from tkinter.messagebox import *

from pojo.book import Book

bd = BookDao()
# 新建界面
window = Tk()
window.title('药材数据库管理系统')
# 调整页面的大小 widthxheight+x+y
window.geometry('800x500')

# 新建一个表格
table = Treeview(columns=('drugsid', 'name', 'Specification', 'unit', 'description', 'state', 'purchase', 'retail'),
                 show="headings")
table.column('drugsid', width=100)
table.column('name', width=100)
table.column('Specification', width=100)
table.column('unit', width=100)
table.column('description', width=100)
table.column('state', width=100)
table.column('purchase', width=100)
table.column('retail', width=100)
table.heading('drugsid', text='药品编号')
table.heading('name', text='药品名称(a)')
table.heading('Specification', text='单位(b)')
table.heading('unit', text='药品单位(c)')
table.heading('description', text='主治功能(d)')
table.heading('state', text='库存状态(e)')
table.heading('purchase', text='进价(f)')
table.heading('retail', text='售价(g)')

def load():
    # 清除表格的数据
    for i in table.get_children():
        table.delete(i)
    # 先读出数据库的数据
    for i in bd.list_book():
        # 将数据加入到表格中
        table.insert('', END, value=i)


def add():
    name = askstring('提示', '请输入药品名称')
    Specification = askstring('提示', '请输入单位')
    unit = askstring('提示', '请输入药品单位')
    description = askstring('提示', '请输入主治功能')
    state = askinteger('提示', '请输入库存状态（0/1）')
    purchase = askfloat('提示', '请输入进货单价')
    retail = askfloat('提示', '请输入零售单价')
    if name is not None:
        r = bd.add_book(Book(name=name,Specification=Specification,unit=unit,description=description,state=state,purchase=purchase,retail=retail))
        if r == '操作失败':
            messagebox.showerror(r)
        else:
            messagebox.askyesno('提示',r)
    load()


def delete():
    if messagebox.askyesno('提示','是否删除'):
        ids = []
        # 制作多选删除
        for i in table.selection():
            # i是元素的id
            # item 根据id拿对应的数据
            ids.append(table.item(i)['values'][0])
        if len(table.selection()) == 0:
            drugsid = askinteger('提示', '请输入药品编号')
            if not bd.search_book(Book(drugsid=drugsid)):
                messagebox.showerror('错误', '不存在该条记录')
            ids.append(drugsid)
        for i in ids:
            bd.del_book(Book(drugsid=i))
        load()


def search():

    drugsid = askinteger('提示', '请输入药品编号')
    for i in table.get_children():
        table.delete(i)
    for i in bd.search_book(Book(drugsid=drugsid)):
        table.insert('', END, value=i)


def update():

    drugsid = askinteger('提示', '请输入药品编号')
    if not bd.search_book(Book(drugsid=drugsid)):
        load()
        messagebox.showerror('错误','不存在该条记录')
        return
    for i in table.get_children():
        table.delete(i)
    for i in bd.search_book(Book(drugsid=drugsid)):
        table.insert('', END, value=i)

    ask = askstring('修改操作','请输入你要改变的属性值（格式为：属性代号/修改值）')
    name, value = ask.split('/')
    bd.update_book(name, value, Book(drugsid=drugsid))
    for i in table.get_children():
        table.delete(i)
    for i in bd.search_book(Book(drugsid=drugsid)):
        table.insert('', END, value=i)



Button(text='刷新', command=load, height=4, width=8, font=(15)).place(x=100, y=350)
Button(text='增加', command=add,height=4, width=8, font=(15)).place(x=225, y=350)
Button(text='删除', command=delete, height=4, width=8, font=(15), bg='red').place(x=350, y=350)
Button(text='搜索', command=search, height=4, width=8, font=(15)).place(x=475, y=350)
Button(text='修改', command=update, height=4, width=8, font=(15)).place(x=600, y=350)
# 让表格显示
table.place(width=800, height=300)
# 让界面显示
window.mainloop()