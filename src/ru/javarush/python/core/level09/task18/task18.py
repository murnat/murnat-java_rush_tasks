# Переопределение метода

# Создайте классы M, N, и O, где N и O наследуют от M.
# В каждом классе определите метод action, который выводит имя класса
# и вызывает метод родительского класса с помощью super().
# Проверьте порядок вызова методов, создав экземпляр класса N и вызвав метод action.

class M:
    def action(self):
        print(f'M')

class N(M):
    def action(self):
        print(f'N')
        super().action()

class O(M):
    def action(self):
        print(f'O')
        super().action()

n = N()
n.action()
