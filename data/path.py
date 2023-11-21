import os
import pathlib

ROOT_PATH = pathlib.Path(__file__).parent.parent
FILE_PATH_CSV = ROOT_PATH.joinpath("data", "transactions.csv")
FILE_PATH_EXCEL = ROOT_PATH.joinpath("data", "transactions_excel.")
FILE_PATH_JSON = ROOT_PATH.joinpath("data", "operations.json")

file_path_csv = os.path.join(ROOT_PATH, "data", "transactions.csv")
file_path_xlsx = os.path.join(ROOT_PATH, "data", "transactions_excel.xlsx")
file_path_json = os.path.join(ROOT_PATH, "data", "operations.json")
