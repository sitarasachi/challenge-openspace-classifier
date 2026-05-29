# CEVI Ghent Open Space Seating System
[![forthebadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)


## 🏢 Description

Your company moved to a new office at CEVI Ghent. Its an openspace with 6 tables of 4 seats. As many of you are new colleagues, you come up with the idea of changing seats everyday and get to know each other better by working side by side with your new colleagues. 

This script runs everyday to re-assign everybody to a new seat.

![coworking_img](https://www.magnific.com/free-photo/view-from-business-startup-teamwork-concept-startup-partners-sitting-coworking-space-talking-about-future-project-looking-through-examples-work-laptop-digital-tablet_8357226.htm#fromView=keyword&page=1&position=0&uuid=9d2c9a41-fe2f-4e84-ad52-e57c4034971d&query=Team+table)

## 📦 Repo structure

```
├── challenge-openspace-classifier-1/.
├── utils
│   ├── file_utils.py
│   ├── openspace.py
│   └── table.py
|
├── main.py
├── new_colleagues.csv
├──notebook_guide.ipynb
├── output.csv
└── README.md
```

## 🛎️ Usage

1. Clone the repository to your local machine.

2 .To run the script, you can execute the `main.py` file from your command line:

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
## ⏱️ Timeline

This project took two days for completion.

## 📌 Personal Situation
This project was done as part of the AI Boocamp at BeCode.org. 