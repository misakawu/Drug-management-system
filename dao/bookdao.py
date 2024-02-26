from util.DBUtil import DbUtil
from pojo.book import Book


class BookDao:
    bu: DbUtil

    def __init__(self):
        self.bu = DbUtil()

    def add_book(self, b: Book):
        try:
            assert isinstance(self.bu, DbUtil)
            # 只支持 %s 占位符
            # %s 支持任意类型
            self.bu.execute('insert into t_medical_drugs_info values(null,%s,%s,%s,%s,%s,%s,%s)',
                            (b.name, b.Specification, b.unit, b.description, b.state, b.purchase, b.retail))
            return '操作成功'
        except Exception as e:
            print(e)
            return '操作失败'

    def del_book(self, b: Book):
        try:
            assert isinstance(self.bu, DbUtil)
            # 只支持 %s 占位符
            # %s 支持任意类型
            self.bu.execute('delete from t_medical_drugs_info where drugsid=%s',(b.drugsid))
            return '操作成功'
        except Exception as e:
            print('操作失败',e)
            return '操作失败'

    def list_book(self, page: int = 1, rows: int = 10):
        try:
            assert isinstance(self.bu, DbUtil)
            #start = (page - 1) * rows + 1
            #return self.bu.execute_list('select * from t_medical_drugs_info limit %d,%d' % (start, rows))
            return self.bu.execute_list('select * from t_medical_drugs_info')
        except Exception as e:
            print(e)
            return '操作失败'

    def search_book(self,b:Book):
        try:
            assert isinstance(self.bu, DbUtil)
            return self.bu.execute_list('select * from t_medical_drugs_info where drugsid=%d' % (b.drugsid))

        except Exception as e:
            print(e)
            return '操作失败'

    def update_book(self,name,value,b:Book):
        try:
            assert isinstance(self.bu, DbUtil)
            if name == "a":
                self.bu.execute_list("update t_medical_drugs_info set name='%s' where drugsid=%d" % (value,b.drugsid))
            elif name == "b":
                self.bu.execute_list("update t_medical_drugs_info set Specification='%s' where drugsid=%d" % (value,b.drugsid))
            elif name == "c":
                self.bu.execute_list("update t_medical_drugs_info set unit='%s' where drugsid=%d" % (value,b.drugsid))
            elif name == "d":
                self.bu.execute_list("update t_medical_drugs_info set description='%s' where drugsid=%d" % (value,b.drugsid))
            elif name == "e":
                self.bu.execute_list("update t_medical_drugs_info set state='%d' where drugsid=%d" % (int(value),b.drugsid))
            elif name == "f":
                self.bu.execute_list("update t_medical_drugs_info set purchase='%d' where drugsid=%d" % (int(value),b.drugsid))
            elif name == "g":
                self.bu.execute_list("update t_medical_drugs_info set retail='%d' where drugsid=%d" % (int(value),b.drugsid))
            return '操作成功'
        except Exception as e:
            print(e)
            return '操作失败'
if __name__ == "__main__":
    bd = BookDao()
    r = bd.list_book(page=3)
    print(r)