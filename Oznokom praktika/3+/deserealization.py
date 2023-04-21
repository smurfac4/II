
from Menu import Menu,Drink,Food
import pickle 
with open('data.pkl', 'rb') as f:
    food1 = pickle.load(f)
    food2 = pickle.load(f)
    drink1 = pickle.load(f)
    drink2 = pickle.load(f)
    restaurant_menu = pickle.load(f)

print(drink1)
print(food2)
print(food1)


print(food1.preparation_time)

print(restaurant_menu)
