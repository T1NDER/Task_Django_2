from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },

}

def recipe_view(request, recipe_name):

    """Отображает рецепт блюда. Возвращает HTML-список ингредиентов,
    умноженных на 'servings' (если есть), или ошибку 404/400."""

    if recipe_name not in DATA:
        return HttpResponse('Такого рецепта не существует', status='404')

    recipe = DATA[recipe_name]
    servings = request.GET.get('servings')
    multiplier = 1.0

    if servings and servings.isdigit():
        multiplier = float(servings)
    elif servings:
        return HttpResponse('Некорректный параметр servings', status='400')

    context = {

        'recipe': {}
    }

    for ingredient, quantity in recipe.items():
        context['recipe'][ingredient] = float(quantity) * multiplier

    return render(request, 'calculator/index.html', context)





