
# 实体类
# 新建pojo持久对象
class Book:#默认继承objject
    drugsid: int
    name: str
    Specification: str
    unit: str
    description: str
    state: int
    purchase: float
    retail: float

    def __init__(self, drugsid: int = None, name: str = None, Specification: str = None, unit: str = None,
                 description: str = None, state: int = None, purchase: str = None, retail: str = None):
        self.drugsid = drugsid
        self.name = name
        self.Specification = Specification
        self.unit = unit
        self.description = description
        self.state = state
        self.purchase = purchase
        self.retail = retail


    def __str__(self):
        return f"{self.drugsid},{self.name},{self.Specification},{self.unit},{self.description},{self.state},{self.purchase},{self.retail}"
