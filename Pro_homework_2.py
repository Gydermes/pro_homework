import module_3
import module_4


class Person:

    def __init__(self, surname, name):
        if not isinstance(surname, str):
            raise TypeError()
        if not isinstance(name, str):
            raise TypeError()
        self.surname = surname
        self.name = name

    def __str__(self):
        return f'{self.surname} {self.name}'


st_1 = module_3.Student('Ivanov', 'Ivan', '12-12-12')
st_2 = module_3.Student('Ivanov1', 'Ivan1', '12-12-12')
st_3 = module_3.Student('Ivanov1', 'Ivan2', '12-12-12')
st_4 = module_3.Student('Ivanov', 'Ivan3', '12-12-12')
st_5 = module_3.Student('Ivanov', 'Ivan3', '12-12-12')

gr = module_4.Group('234234')
gr.add_student(st_1)
gr.add_student(st_2)
gr.add_student(st_3)
gr.add_student(st_4)

print(gr)
print("search = ", gr.search("Ivan"))