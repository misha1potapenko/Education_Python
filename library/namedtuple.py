from collections import namedtuple
from datetime import datetime
User = namedtuple('User', ['first_name', 'last_name', 'birthday'])
u_1 = User('Исаак', 'Ньютон', datetime(1643, 1, 4))
print(u_1)
print(f'{type(User)}, {type(u_1)}')
