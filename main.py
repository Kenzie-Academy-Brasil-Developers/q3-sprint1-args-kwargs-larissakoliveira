def sum_numbers(*args):
    return sum(args)

numbers = [1, 2, 3, 4, 5, 6]

result = sum_numbers(*numbers)
print(result)

############################################################

def get_multiplied_amount(multiplier, *args):
    sum = sum_numbers(*numbers)
    return sum * multiplier


numbers = [1, 2, 3]
multiplier = 2

result = get_multiplied_amount(multiplier, *numbers)
print(result)

############################################################################################################################

def word_concatenator(*args):
    return " ".join(args)

words = ["Tá", "pegando", "fogo", "bicho!!!"]

concatenated_words = word_concatenator(*words)
print(concatenated_words)

############################################################################################################################

def inverted_word_factory(*args):
    reverse_whole_list = args[::-1]
    output = ''
    for index, arg in enumerate(reverse_whole_list):
        output += arg[::-1]
        if index+1 < len(arg):
            output += ' '
    return output

words = ["eae", "amigão", "belezinha?"] 

inverted_words = inverted_word_factory(*words)
print(inverted_words)   

############################################################################################################################

def dictionary_separator(**kwargs):
    output = []
    output.append(list(kwargs.keys()))
    output.append(list(kwargs.values()))
    return tuple(output)

user = {
   "name": "Naruto",
   "age": 16,
   "favorite word": "Ichiraku Ramen"
 }

items = dictionary_separator(**user)
print(items)

# #######################################################################################################################################3

def dictionary_creator(*args, **kwargs):
    if len(args) < len(kwargs):
        return None
    output = {}
    for index, key in enumerate(kwargs):
        output[args[index]] = kwargs.get(key)
    return output
    
change_keys = ["username", "password", "address"]
user = {
    "name": "Williams",
    "key": "1234"
}

modified_user = dictionary_creator(*change_keys, **user)
print(modified_user)

{
    "username": "Williams",
    "password": "1234"
}
##########################################################################################################################################################

def purchase_logger(**kwargs):
        return f"Product {kwargs['name']} costs {kwargs['price']} and was bought {kwargs['quantity']}"

purchase = {"name": "washing powder", "price": 6.7, "quantity": 4}

purchase_log = purchase_logger(**purchase)
print(purchase_log)

"Product washing powder costs 6.7 and was bought 4"
#########################################################################################################################################################

def world_cup_logger(country, *args):
    sorted_years = sorted(list(args))
    output = f'{country} - '

    for index in range(len(sorted_years)):
        if index == len(sorted_years) -1:
            output += 'e ' + str(sorted_years[index])
        elif index >= 0 and index < len(sorted_years) -2:
            output += str(sorted_years[index]) + ', '
        else:
            output += str(sorted_years[index]) + ' '
    return output

country = 'Alemanha'
year_list = [2014, 1990, 1974, 1954]

log = world_cup_logger(country, *year_list)
print(log)

