from .add import AddOperation
from faker import Faker

fake = Faker()

def test_some():
    addOperation = AddOperation()
    number1 = fake.random_number()
    number2 = fake.random_number()
    expect = number1 + number2

    result = addOperation.sum(number1, number2)

    assert result == expect