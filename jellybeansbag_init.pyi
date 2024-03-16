# JellyBeansBag.pyi

new_element: str

integer_number: int
floating_number: float
string_value: str
boolean_value: bool

def add(x: int, y: int) -> int
def multiply(x: int, y: int) -> int

bag_capacity: int
bag_color: str

class JellyBean:
    color: str
    flavor: str

    def __str__(self) -> str

class JellyBeansBag:
    beans: list[JellyBean]

    def __init__(self) -> None
    def add_bean(self, bean: JellyBean) -> None
    def get_all_beans(self) -> list[JellyBean]

jelly_bean1: JellyBean
jelly_bean2: JellyBean

beans_bag: JellyBeansBag
all_beans: list[JellyBean]
bean: JellyBean
