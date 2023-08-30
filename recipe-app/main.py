import requests

def recipe_search(main_ingred, meal_type, time, excluded):
    app_id = 'e140c287'
    app_key = 'a742a0a57d8b22b5adc391f5014ee34b'
    result = requests.get(
        'https://api.edamam.com/search?q={}&app_id={}&app_key={}&mealType={}&time={}&excluded={}'.format(
            main_ingred, app_id, app_key, meal_type, time, excluded))
    data = result.json()
    return data['hits']

def save_results(results):
    with open('recipe_results.txt', 'w+') as text_file:
        text_file.write(str(results))

def go():
    main_ingred = input('Enter main ingredient: ')
    time = int(input('Max time for recipe (in minutes):'))
    meal_type = input('What meal type are you looking for?: ')
    excluded = input('What ingredients should be excluded? ')

    results = recipe_search(main_ingred, meal_type, time, excluded)

    for result in results:
        recipe = result['recipe']
        print(recipe['label'])
        print(recipe['url'])
        print('\n')
    print('The total number of recipes is {}'.format(len(results)))
    print('\n')
    save_choice = input('Would you like to save your results? (yes/no)')

    if save_choice == 'yes':
        save_results(results)

go()




















