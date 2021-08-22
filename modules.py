from utilities.utils import find_max

numbers = [50, 2, 34, 5, 1]
max_num = find_max(numbers)
print(max_num)


# or
from utilities import utils

numbers = [50, 2, 55, 5, 1]
max_num = utils.find_max(numbers)
print(max_num)

#or
import utilities.utils

numbers = [50, 2, 34, 5, 1]
max_num = utilities.utils.find_max(numbers)
print(max_num)