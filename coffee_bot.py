# Define your functions
def coffee_bot():
  print("Welcome to the cafe!")
  name = input("Can I get your name please?")
  size = get_size()
  drink_type = get_drink_type()
  drink_preference = get_drink_preference()
  location = get_location()
  print("Alright, that's a " + str(drink_preference) + ", " + str(size) + " "+ str(drink_type) + "!")
  print("You wil be " + str(location))
  print("Thanks, " + name + "! Your drink will be ready shortly.")

def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n>')
  if res == 'a' or res == 'A':
    return 'small '
  elif res == 'b' or res == 'B':
    return 'medium'
  elif res == 'c' or res == 'C':
    return 'large'
  else:
    print_message()
    return get_size()

def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

def order_latte():
    res = input("And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk>")
    if res == 'a' or res == 'A':
      return 'latte'
    elif res == 'b' or res == 'B':
      return 'non-fat latte'
    elif res == 'c' or res == 'C':
      return 'soy latte'
    else:
      print_message()
      return order_latte

def get_drink_type():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte>')
  if res == 'a' or res == 'A':
    return "brewed coffee"
  elif res == 'b' or res == 'B':
    return "mocha"
  elif res == 'c' or res == 'C':
    return order_latte()
  else:
    print_message()
    return get_drink_type()

def get_drink_preference():
  res = input("How would you like your drink: \n[a] Hot \n[b] Iced>")
  if res == 'a' or res == 'A':
    return 'hot'
  elif res == 'b' or res == 'B':
    return 'iced'
  else:
    print_message()
    return get_drink_type()

def get_location():
  res = input("Would you like to: \n[a] Eat-in \n[b] Take away>")
  if res == 'a' or res == 'A':
    return 'eating in'
  elif res == 'b' or res == 'B':
    return eco_friendly()
  else:
    print_message()
    return location()

def eco_friendly():
  res = input("I can see that you are having your drink as a take away. Would you like to use your own reusable cup? \n[a] Yes \n[b] No>")
  if res == 'a' or res == 'A':
    return 'using your own reusable cup.'
  elif res == 'b' or res == 'B':
    return 'using our single-use cup.'
  else:
    print_message()
    return eco_friendly()

# Call coffee_bot()!
coffee_bot()
