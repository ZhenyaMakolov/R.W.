{'Омлет': [{'ngredient', 'quantity', 'measure'}]}

with open('recept.txt', 'rt', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        dish = line.strip()
        ingredients_count = int(f.readline())
        ingredients = []
        for i in range(ingredients_count):
            emp = f.readline().strip()
            ingredient, quantity, measure = emp.split(' | ')
            ingredients.append({
                'ingredient_name': ingredient,
                'quantity': quantity,
                'measure': measure
            })
        f.readline()
        cook_book[dish] = ingredients
print(cook_book)
