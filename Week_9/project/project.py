import argparse
import pandas as pd
import sys
from fpdf import FPDF


def main():
    parser = argparse.ArgumentParser(description="Convert a .xlsx sheet into JSON and PDF")
    parser.add_argument("-f", help="name of .xlsx file to open", required=True)
    parser.add_argument("-s", help="name to save the JSON and PDF outputs", required=True)
    args = parser.parse_args()
    data = convert_xlsx(args.f)
    clean_data = group_sort_data(data)
    export_json(clean_data, args.s)
    export_pdf(clean_data, args.s)


def convert_xlsx(file_path):
    try:
        list = pd.read_excel(file_path)
        list_of_dicts = list.to_dict(orient="records")
        return list_of_dicts
    except FileNotFoundError:
        sys.exit(f"Error: File not found at {file_path}")
    except Exception as e:
        sys.exit(f"An error occurred: {e}")


def group_sort_data(list_dict):
    df = pd.DataFrame(list_dict)
    grouped = df.groupby(list(df.columns)).size().reset_index(name="Total")
    result = grouped.to_dict(orient="records")
    sort = sorted(result, key=lambda k: k["Manufacturer"])
    return sort


def export_json(data, name):
    df = pd.DataFrame(data)
    df.to_json(path_or_buf=f"{name}.json", orient="records", indent=4)


def export_pdf(data, name):
    manuf = []
    for mf in data:
        if mf["Manufacturer"] not in manuf:
            manuf.append(mf["Manufacturer"])
    df = pd.DataFrame(data).map(str)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", "B", 18)
    pdf.set_font(style="U")
    pdf.cell(0, 15, text="####  PICKING LIST BY MANUFACTURER  ####", align="C")
    pdf.set_font_size(10)
    pdf.set_xy(0, 30)
    for mf in manuf:
        filtered_df = df[df["Manufacturer"] == mf]
        COLUMNS = [list(filtered_df)]  # Get list of dataframe columns
        ROWS = filtered_df.values.tolist()  # Get list of dataframe rows
        DATA = COLUMNS + ROWS  # Combine columns and rows in one list
        with pdf.table() as table:
            mf_row = table.row()
            mf_row.cell(mf)
        with pdf.table(col_widths=(15, 42, 15, 8)) as table:
            for data_row in DATA:
                row = table.row()
                for datum in data_row:
                    row.cell(datum)
        with pdf.table(borders_layout="NONE") as table:
            mf_row = table.row()
            mf_row.cell(" ")
    pdf.output(f"{name}.pdf")


if __name__ == "__main__":
    main()
