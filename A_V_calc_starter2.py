'''
TPRG 2131 Fall 202* Assignment 1
Sept, 2024
Sujan Rathnakumar 100893497 

Use this template as the start

*********
A/V calculator

(Level 0)
Enter Q/q to quit – select either will gracefully close the application and cancel the calculated view option.
Enter V/v to change the calculated view or D/d for default view.

	(Level 1)
    1.	Area of Rectangle* calulation
    2.	Area of a Circle* calculation
    3.	Volume of a Sphere* calculation
    4.	Volume of a Cylinder* calculation
    5.	Volume of a Cube* calculation

*********

The above menu style (inside the asterix's) is expected, only 2 key entries to use the calculator.

The menu Level 1 , options 1...5 should be modified from the above to reflect the
function you selected.

After selection at level 1, the calculator expects data to entered (use appropiate data types).

(The Level 0 & 1 labels are for indication purpose and are not
to be included)

'''

import math

class A_V_CALC:
    # Class to calculate areas and volumes of different shapes

    def rectangle_area(self, length, width):
        # Calculate area of a rectangle
        return length * width
    
    def circle_area(self, radius):
        # Calculate area of a circle
        return math.pi * radius ** 2
    
    def sphere_volume(self, radius):
        # Calculate volume of a sphere
        return (4/3) * math.pi * (radius ** 3)
    
    def cylinder_volume(self,radius,height):
        # Calculate volume of a cylinder
        return math.pi * (radius ** 2) * height
    
    def cube_volume(self, edge):
        # Calculate volume of cube
        return edge ** 3


class GUI:
    # Class to manage the GUI and User Interactions
    
    def __init__(self):
        # Initialize the area/volume calculator
        self.calculator = A_V_CALC()
    
    
    def menu(self):
        # Display Main menu options
        print("\n------AREA/VOLUME CALCULATOR------")
        print("--------Enter Q/q to quit---------")
        print("----Enter V/v for extended view---")
        print("----Enter D/d for default view----")
    
        
    def options(self):
        # Display Options for calculation
        print("\nExtended View")
        print("1. Area of a Rectangle")
        print("2. Area of a Circle")
        print("3. Volume of a Sphere")
        print("4. Volume of a Cylinder")
        print("5. Volume of Cube")
        print("Enter any key to return to the main menu")
        
    
    def get_option(self, option):
        # Get the user's choice and perform the corresponding calculation
        if option == '1':
            print("\n Enter values in m")                         # Inform User of measurement units
            length = float(input("Enter Length: "))               # get inputs
            width = float(input("Enter width: "))
            value = self.calculator.rectangle_area(length,width)  # Calculate area using the equation on the relevant function
            equation = ("Area = length * width" \
                        + "\nArea = " + str(length) \
                        + " x " + str(width) )                    # Prepare equation for display
        
        elif option == '2':
            print("\n Enter values in m")
            radius = float(input("Enter radius of Circle: "))
            value = self.calculator.circle_area(radius)
            equation = ("Area = \u03C0 x r" + "\u00B2"\
                        + "\nArea = \u03C0 x " \
                        + str(radius) + "\u00B2")
            
        elif option == '3':
            print("\n Enter values in m")
            radius = float(input("Enter radius of the Sphere: "))
            value = self.calculator.sphere_volume(radius)
            equation = ("Volume = 4/3 x \u03C0 x r" + "\u00B3"\
                        + "\nVolume = 4/3 x \u03C0 x " \
                        + str(radius) + "\u00B3")
            
        elif option == '4':
            print("\n Enter values in m")
            radius = float(input("Enter radius of the Cylinder: "))
            height = float(input("Enter height of the Cylinder: "))
            value = self.calculator.cylinder_volume(radius,height)
            equation = ("Volume = \u03C0 x r" \
                        + "\u00B2 x h" \
                        + "\nVolume = \u03C0 x " \
                        + str(radius) + "\u00B2 x " \
                        + str(height) )
            
        elif option == '5':
            print("\n Enter values in m")
            edge = float(input("Enter length of one of the edges of Cube: "))
            value = self.calculator.cube_volume(edge)
            equation = ("Volume = a" + "\u00B3" \
                        + "\nVolume = " + str(edge) \
                        + "\u00B3")
            
        else:
            value = -1       # Invalid Option
        
        return round(value,2), equation    # Return Calculated value and equation


    def main(self):
        # main loop for the user interface
        while True:
            
            self.menu()   #show the main menu
            
            choice = input("Select an option: ").strip().lower()  # Get user input for main menu
            
            if choice == 'q':    # check for quit option
                break
            
            elif choice in ['v','d']:   # check for view type selection
                view_type = choice      # select the view type
                while True:
                    self.options()  # show calculation options
                    option = input("Enter your Selection: ").strip()  # Get user's calculation choice
                    if option not in ['1','2','3','4','5']:    # if valid choice
                        break     # Exit options loop
                        
                    
                    
                    value, equation = self.get_option(option)    # Perform calculation based on option
                    
                    if value != -1:
                        # Display results based on selected view type
                        if view_type == 'd' and option in ['1','2']:
                            print("Area = " + str(value) + " \u33A1" )
                            
                        elif view_type == 'd' and option in ['3','4','5']:
                            print("Volume = " + str(value) + " \u33A5" )
                        
                        elif view_type == 'v' and option in ['1','2']:
                            print(equation)
                            print("Area = " + str(value) + " \u33A1" )
                            
                        elif view_type == 'v' and option in ['3','4','5']:
                            print(equation)
                            print("Volume = " + str(value) + " \u33A5" )
                    
                    else:
                        print("Invalid option. Please try again.")     # Error message for invalid option
                        
                    
                    input("Press Enter to continue......")      # wait for the user input before continuing 
                    

if __name__ == "__main__":
    
    gui = GUI()     # Create an instance of the GUI class
    gui.main()      # Start the main program loop
                    
