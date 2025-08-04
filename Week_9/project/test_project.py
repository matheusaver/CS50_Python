from project import convert_xlsx
import pytest


def test_convert_xlsx():
    assert convert_xlsx("final_list.xlsx")
    with pytest.raises(SystemExit) as excinfo:
        convert_xlsx("notfile.xlsx")
    assert excinfo.type == SystemExit
    assert str(excinfo.value) == "Error: File not found at notfile.xlsx"
