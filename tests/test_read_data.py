import unittest.mock

import pandas as pd
import pytest

from data.path import file_path_csv, file_path_xlsx
from src.read_data import read_csv, read_xlsx


def test_read_csv_with_mock():
    with unittest.mock.patch("src.read_data.csv.DictReader") as mock_csv_reader:
        mock_csv_reader.return_value = [{"id": "1", "name": "Evgeniy"}]
        result = read_csv(file_path_csv)
    assert result == [{"id": "1", "name": "Evgeniy"}]


def test_read_xlsx_with_patch():
    with unittest.mock.patch("src.read_data.pd.read_excel") as mock_read_excel:
        mock_read_excel.return_value = pd.DataFrame({"id": [1], "name": ["Evgeniy"]})
        result = read_xlsx(file_path_xlsx)
    assert result == [{"id": 1, "name": "Evgeniy"}]


if __name__ == "__main__":
    pytest.main()
