#  In the second file (main.py), import the
#  format_name function using both of the
#  following:
#  import tools
#  from tools import format_name
#  Use both import styles correctly in two
#  separate sections of the code.

import tools
from tools import format_name

# Add the if __name__ == "__main__": check in
#  main.py and run the function only when the
#  file is executed directly.

if __name__ == "__main__":
    name = input("Enter your name: ")
    newName = format_name(name)
    print(newName)