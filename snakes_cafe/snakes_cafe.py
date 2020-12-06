menu_items = ['A Literal Garden', 'Cake', 'Coffee', 'Cookies', 'Ice Cream', 'Meat Tornado',
'Pie', 'Salmon', 'Spring Rolls', 'Steak', 'Tea', 'Unicorn Tears', 'Wings']

appetizers = ['Appetizers', '--------------------', { 'Wings': 0, 'Cookies': 0, 'Spring Rolls': 0 }, '\n']
entrees = ['Entrees', '--------------------', { 'Salmon': 0,  'Steak': 0, 'Meat Tornado': 0, 'A Literal Garden': 0,}, '\n']
desserts = ['Desserts', '--------------------', { 'Ice Cream': 0, 'Cake': 0, 'Pie': 0 }, '\n']
drinks = ['Drinks', '--------------------', { 'Coffee': 0, 'Tea': 0, 'Unicorn Tears': 0 }, '\n']
off_menu = {}

menu = [appetizers, entrees, desserts, drinks]

class IO:

  @staticmethod
  def menu_display():
    print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**                                  **
** To quit at any time, type "quit" **
**************************************

""")

    for section in menu:
      for part in section:
        if part != section[2]:
          print(part)
        else:
          for item in part:
            print(item)

    print("""
***********************************
** What would you like to order? **
***********************************
""")

  @staticmethod
  def menu_input():
    while True:
      order_selection = input('> ').title()

      if order_selection == 'Quit':
        break
      elif menu_items.count(order_selection) != 0:
        for section in menu:
          for item in section[2]:
            if order_selection == item:
              section[2][item] += 1
              order_selection_count = section[2][item]
        
        if order_selection_count == 1:
          print(f'** {order_selection_count} order of {order_selection} has been added to your meal **')
        else:
          print(f'** {order_selection_count} orders of {order_selection} have been added to your meal **')
      else:
        # print('Sorry, that\'s not on the menu.')
        off_menu_order_selection = order_selection
        off_menu_order_selection_count = int(input('That\'s not on the menu, but I\'ll see what I can do. How many order of that did you want?\n> '))
        if off_menu_order_selection_count == 1:
          print(f'** {off_menu_order_selection_count} order of {off_menu_order_selection} has been added to your meal **')
        else:
          print(f'** {off_menu_order_selection_count} orders of {off_menu_order_selection} have been added to your meal **')
        continue

IO.menu_display()
IO.menu_input()