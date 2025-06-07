from flask import Flask, render_template, request

app = Flask(__name__)

# these are global variables
orders = []
total_revenue = 0


menu_prices = {
    "Chicken Fajita": 12.99,
    "Beef Tacos": 10.99,
    "Pork Tacos": 10.99,
    "Shrimp Tacos": 13.99,
    "Cheese Fries": 7.99,
    "Pupusas": 9.99
}

drink_prices = {
    "Small": 0,
    "Medium": 1.00,
    "Large": 2.00
}

dessert_prices = {
    "Cake": 4.99,
    "Cookies": 3.99,
    "Ice Cream": 4.99,
    "Cookies and Cream": 5.99,
    "Brownies": 4.99,
    "Creme Brulee": 6.99
}

@app.route('/order', methods=['GET', 'POST'])
def hello_world():
    editMeal = request.args.get('meal')
    editDrink = request.args.get('drink')
    editDrinkSize = request.args.get('drinkSize')
    editDessert = request.args.get('dessert')
    editName = request.args.get('name')

    editDetails = {
        'meal': editMeal,
        'drink': editDrink,
        'drinkSize': editDrinkSize,
        'dessert': editDessert,
        'name': editName
    }
    # -------------------
    mealChoices = ["Chicken Fajita", "Beef Tacos", "Pork Tacos", "Shrimp Tacos", "Cheese Fries", "Pupusas"]
    drinkChoices = ["Water", "Soda", "Fanta", "Coke", "Sprite", "Lemonade", "Ginger Ale", "Mountain Dew"]
    dessertChoices = ["Cake", "Cookies", "Ice Cream", "Cookies and Cream", "Brownies", "Creme Brulee"]
    return render_template('index.html', mealChoices=mealChoices, drinkChoices=drinkChoices, dessertChoices=dessertChoices, editDetails=editDetails)

@app.route('/confirm-order', methods=['GET', 'POST'])
def submit_order():
    meal = request.args.get('meal')
    drink = request.args.get('drink')
    drinkSize = request.args.get('drinkSize')
    dessert = request.args.get('dessert')
    name = request.args.get('name')
    
    # Calculate price
    meal_price = menu_prices.get(meal, 10.99)  
    drink_price = drink_prices.get(drinkSize, 0)
    dessert_price = dessert_prices.get(dessert, 4.99)  
    
    total_price = meal_price + drink_price + dessert_price
    
    
    order = {
        "id": len(orders) + 1,
        "meal": meal,
        "drink": drink,
        "drinkSize": drinkSize,
        "dessert": dessert,
        "name": name,
        "total": total_price
    }
    
    
    orders.append(order)
    global total_revenue
    total_revenue += total_price
    
    return render_template('confirm-order.html', meal=meal, drink=drink, drinkSize=drinkSize, dessert=dessert, total=total_price, name=name)

@app.route('/kitchen')
def kitchen_dashboard():
    return render_template('kitchen.html', orders=orders, total_revenue=total_revenue, order_count=len(orders))

app.debug=True
if __name__ == '__main__':
    app.run()