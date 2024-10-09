class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def __setattr__(self, key, value):
        if key == 'name':
            if not (isinstance(value, str) and value[0].isupper()):
                raise ValueError('ФИО должно состоять из букв и начинаться с заглавной')
        elif key == 'age':
            if not (isinstance(value, int) and 0 <= value <= 120):
                raise ValueError('Возраст должен быть числом от 0 до 120')
        elif key == 'email':
            if not isinstance(value, str) and '@' in value:
                raise ValueError('Email должен соджержать символ "@"')
        super(Person, self).__setattr__(key, value)

    def __str__(self):
        return f'{self.name = }, {self.age = }, {self.email = }'


if __name__ == '__main__':
    p1 = Person('Влад', 23, 'vlad07407@gmail.com')
    print(p1)
