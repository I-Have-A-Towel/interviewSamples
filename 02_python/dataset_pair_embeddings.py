import numpy as np

dessert_dataset = [
    {"key": "Apple Pie", "embedding": np.array([4, 6, 8, 2])},
    {"key": "Cheesecake", "embedding": np.array([1, 4, 3, 0])},
    {"key": "Chocolate Cake", "embedding": np.array([9, 2, 10, 4])},
    {"key": "Chocolate Mousse", "embedding": np.array([1, 4, 1, 0])},
]

ingredient_dataset = [
    {"key": "Philo Dough", "embedding": np.array([4, 6, 6, 2])},
    {"key": "Cream Cheese", "embedding": np.array([2, 5, 3, 2])},
    {"key": "Flour", "embedding": np.array([9, 1, 9, 4])},
    {"key": "Heavy Cream", "embedding": np.array([1, 2, 1, 0])},
]

######
# Given two datasets containing dessert and ingredient information,
# your task is to write a function or code snippet to match each
# dessert with the most suitable ingredient based on the similarity
# of their embedding values. Each dessert and ingredient has an
# associated embedding value represented as a NumPy array.
#########
