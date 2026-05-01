from functions import pivoting
import ast
import csv
from pathlib import Path

def save_matrix_csv(matrix, path):
    path = Path(path)

    if path.suffix == "":
        path = path.with_suffix(".csv")

    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(matrix)

    print(f"Matrix saved in: {path.resolve()}")
    


while True:
    print("\n--- MENU ---")
    print("1. Pivoting matrix")
    print("2. Exit")

    option = input("Choose an option: ")

    
    if option == "1":

        matrix = input("Enter your matrix in simple array form\n\n")
        matrix_mod=pivoting(ast.literal_eval(matrix))
        print("Result\n\n")
        print(matrix_mod)
        
        save = input("\nDo you want to save the modified matrix as a .csv file? (y/n): ")

        if save.lower() == "y":
            path = input("Where do you want to save it? Write the path and the file name:\n")
            save_matrix_csv(matrix_mod, path)
        
    elif option == "2":
        print("Closed.")
        break

    else:
        print("Invalid option.")

    again = input("\nDo you want to do another operation? (y/n): \n\n")

    if again.lower() != "y":
        print("Invalid option")
        break

