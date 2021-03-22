# Lori Vo 1852113

class FoodItem:
    def __init__(self, name='None', fat=0.00, carbs=0.00, protein=0.00):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, numb_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * numb_servings
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


if __name__ == "__main__":

    none = FoodItem()

    given = FoodItem()
    given.name = input()
    given.fat = float(input())
    given.carbs = float(input())
    given.protein = float(input())
    num_servings = float(input())

    none_calories = none.get_calories(num_servings)
    none.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings, none_calories))
    print()
    given_calories = given.get_calories(num_servings)
    given.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings, given_calories))
