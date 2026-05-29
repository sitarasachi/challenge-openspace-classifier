from utils.openspace import Openspace
from utils.file_utils import read_names_from_csv

def main():
    """Main function that orchestrates the seating arrangement process. 
    It reads names from a CSV file, creates an Openspace instance, 
    organizes the seating, stores the arrangement in a new file, 
    and displays the assignments in the terminal. The input and output file paths
    are defined at the beginning of the function."""
    
    input_filepath = "new_colleagues.csv"
    output_filename = "output.csv"

    # Creates a list that contains all the colleagues names
    names = read_names_from_csv(input_filepath)

    # create an OpenSpace()
    open_space = Openspace()

    # assign a colleague randomly to a table
    open_space.organize(names)

    # save the seat assigments to a new file
    open_space.store(output_filename)

    # display assignments in the terminal
    open_space.display()

if __name__ == "__main__":
    main()