###Modules and Packages

#Writing modules
# Modules in Python are simply Python files with a .py extension.
#  The name of the module will be the name of the file.
#  A Python module can have a set of functions, classes or variables defined
#  and implemented.


#Import a module:
    # game.py
    # import the draw module
    import draw

    def play_game():
        ...

    def main():
        result = play_game()
        draw.draw_game(result)

    # this means that if this script is executed, then
    # main() will be executed
    if __name__ == '__main__':
        main()




## Custom import name
    import pandas as pd
    #^ if you import like this, you will not need to type in pandas.function(variable)
    #, you can just type: pd,function(variable) Best way to be lazy

##Import all from a module:
    from exampleModule import *
# ^Lasiest way to impoer all object from a module.

#Module initialization
    # The first time a module is loaded into a running Python script, it is
    # initialized by executing the code in the module once. If another module in
    # your code imports the same module again, it will not be loaded twice but
    #  once only - so local variables inside the module act as a "singleton" -
    #   they are initialized only once.
    # draw.py

    def draw_game():
        # when clearing the screen we can use the main screen object initialized in this module
        clear_screen(main_screen)
        ...

    def clear_screen(screen):
        ...

    class Screen():
        ...

    # initialize main_screen as a singleton
    main_screen = Screen()
###Exercise
# In this exercise, you will need to print an alphabetically sorted list of
# all functions in the re module, which contain the word find.
find_members = []
# initialize list
for member in dir(re):
    #iteration every member in the re module
    if "find" in member:
        #if contain the word find.
        find_members.append(member)


print(sorted(find_members))
