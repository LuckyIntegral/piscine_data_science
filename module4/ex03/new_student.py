import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    '''Generate a random id of 15 characters.'''
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    '''Class to represent a student.'''
    name: str = field()
    surname: str = field()
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        '''Sets the login only. Works once the object is created.'''
        self.login = self.name[0].lower() + self.surname.lower()
