# CEVI Ghent Open Space Seating System
[![forthebadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)


## 🏢 Description

Our company has recently moved to a new office at CEVI Ghent, featuring an open space layout with shared tables.Its an openspace with 6 tables of 4 seats. To encourage collaboration and help colleagues get to know each other better, we reshuffle seating arrangements every day.

This Python script automatically assigns employees to different seats each day in a random and fair way.


![coworking_img](https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDd8fGRpdmVyc2UlMjB0ZWFtfGVufDB8fDB8fHwy)

## 📦 Repo structure

```
├── challenge-openspace-classifier-1/.
├── utils
│   ├── file_utils.py
│   ├── openspace.py
│   └── table.py
├── .gitignore
├── main.py
├── new_colleagues.csv
├──notebook_guide.ipynb
├── output.csv
└── README.md
```

## 🛎️ Usage

1. Clone the repository "challenge-openspace-classifier" to your local machine.

    This program is used to randomly assign colleagues to seats in the CEVI Ghent openspace.


2. To run the script, you can execute the `main.py` file from your command line:
 

```
   python main.py
```

3. The script reads your input file, and organizes your colleagues to random seat assignments. The resulting seating plan is displayed in your console and also saved to an "output.csv" file in your root directory. 

```python
def main():
    input_filepath = "new_colleagues.csv"
    output_filename = "output.csv"

    # Creates a list that contains all the colleagues names
    names = utils.read_names_from_csv(input_filepath)

    # create an OpenSpace()
    open_space = OpenSpace()

    # assign a colleague randomly to a table
    open_space.organize(names)

    # save the seat assigments to a new file
    open_space.store(output_filename)

    # display assignments in the terminal
    open_space.display()

if __name__ == "__main__":
    main()
```
This is the main file that runs the program.

  

## 📌 Workflow
    Read names from new_colleagues.csv
                    ↓
    Create Openspace
                    ↓
    Randomly assign seats
                    ↓
    Save results to output.csv
                    ↓
    Display seating arrangement


## ⏱️ Timeline

This project took two days for completion.

## 📌 Personal Situation
This project was done as part of the AI Boocamp at BeCode.org. 

## 📌 My Linkedin
https://www.linkedin.com/in/sitara-sachidanandan/

