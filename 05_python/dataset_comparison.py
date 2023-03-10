######
#  Q: Write a function / code snippet that does the following:
#
#  Match up dessert dataset items with appropriate ingredient_dataset items
#  according to closest-match of the embedding_values.
#  Once matched, display the list results in the following manner:
#  "Dessert" requires "Ingredient"
#
#  For example:  "Doughnut requires Flour"
#########

import numpy as np

dessert_dataset = [
    {"key": "Apple Pie", "embedding_value": np.array([4, 6, 8, 2])},
    {"key": "Cheesecake", "embedding_value": np.array([1, 4, 3, 0])},
    {"key": "Chocolate Cake", "embedding_value": np.array([9, 2, 10, 4])},
    {"key": "Chocolate Mousse", "embedding_value": np.array([1, 4, 1, 0])},
]

ingredient_dataset = [
    {"key": "Philo Dough", "embedding_value": np.array([4, 6, 6, 2])},
    {"key": "Cream Cheese", "embedding_value": np.array([2, 5, 3, 2])},
    {"key": "Flour", "embedding_value": np.array([9, 1, 9, 4])},
    {"key": "Heavy Cream", "embedding_value": np.array([1, 2, 1, 0])},
]

# Write your code here using the above datasets
