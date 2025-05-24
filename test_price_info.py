import Lab3.price_info as price 


def test_total_cost_shopping():
    price.price_list={'apple' : 1.20, 'orange':1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear' : 0.90, 'papaya': 2.95, 'pomegranate': 4.95 }
    price.quantity_list= {'apple': 10, 'orange':10, 'watermelon': 3, 'pineapple': 2, 'pear' : 10, 'papaya': 10, 'pomegranate': 20}
    expected=188.4
    result=price.total_cost_shopping()
    
    assert(result==expected)

def test_cost_of_fruit():
    price.price_list={'apple' : 1.20, 'orange':1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear' : 0.90, 'papaya': 2.95, 'pomegranate': 4.95 }
    price.quantity_list= {'apple': 10, 'orange':10, 'watermelon': 3, 'pineapple': 2, 'pear' : 10, 'papaya': 10, 'pomegranate': 20}
    fruit='orange'
    quantity=100
    result=price.cost_of_fruits(fruit, quantity)
    expected=140

    assert(result==expected)