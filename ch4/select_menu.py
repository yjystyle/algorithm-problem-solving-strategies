

# 책에서는 모두가 식사할 수 있는 메뉴는 없었다.
def can_everybody_eat(menu):
    return False

# 아주 큰 값
INF = 987654321

# 요리할 수 있는 음식의 종류 수
M = 2

def select_menu(menu, food):
    if food == M:
        if can_everybody_eat(menu):
            return menu.size
        return INF
    ret = select_menu(menu, food+1)
    menu.append(food)
    ret = min(ret, select_menu(menu, food+1))
    menu.pop()
    return ret

a = select_menu([1,2,3,4,5], 2)
print(a)


   
