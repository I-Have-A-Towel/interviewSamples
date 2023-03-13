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
    {"key": "Apple Pie", "embedding_value": 1},
    {"key": "Cheesecake", "embedding_value": 4},
    {"key": "Chocolate Cake", "embedding_value": 8},
    {"key": "Chocolate Mousse", "embedding_value": 5},
]

ingredient_dataset = [
    {"key": "Philo Dough", "embedding_value": 2},
    {"key": "Cream Cheese", "embedding_value": 5},
    {"key": "Flour", "embedding_value": 9},
    {"key": "Heavy Cream", "embedding_value": 6},
]

# Write your code here using the above datasets
