import gspread
import numpy as np


# multiplication of 2 matrices
def matmul(A: list, B: list):
    A = np.array(A)
    B = np.array(B)
    Output = np.dot(A, B)
    return Output


def create_matrix_from_sheet(sheet: gspread.worksheet.Worksheet):
    matrix = []
    val_dict = sheet.get_all_values()
    for row in val_dict:
        mat_row = []
        for val in row:
            mat_row.append(int(val))
        matrix.append(mat_row)
    return matrix


def output_to_sheet(output_sheet_name, spreadsheet: gspread.spreadsheet.Spreadsheet, output: np.ndarray):
    output_sheet = spreadsheet.worksheet(output_sheet_name)
    end_cell = ord('A') + (output.shape[1] - 1)
    end_cell = chr(end_cell)
    end_cell += str(output.shape[0])
    update_str = "A1:" + end_cell
    output_sheet.update(update_str, output.tolist())


def spread_sheet(A_sheet_name, B_sheet_name, output_sheet_name):
    # opening sheet
    account = gspread.service_account("research-algorithms-3a674a7a5271.json")
    spreadsheet = account.open("research-algo-ex8")
    A_sheet = spreadsheet.worksheet(A_sheet_name)
    B_sheet = spreadsheet.worksheet(B_sheet_name)
    # getting values as lists
    A = create_matrix_from_sheet(A_sheet)
    B = create_matrix_from_sheet(B_sheet)
    Output = matmul(A, B)
    # creating output sheet in the given name and the output matrix dimensions
    spreadsheet.add_worksheet(title=output_sheet_name, rows=Output.shape[0], cols=Output.shape[1])
    # feed output data to output sheet
    output_to_sheet(output_sheet_name, spreadsheet, Output)


if __name__ == '__main__':
    # these running examples are shown in the "running examples" file
    spread_sheet("A1", "B1", "A1mulB1")
    spread_sheet("A2", "B2", "A2mulB2")
    spread_sheet("A3", "B3", "A3mulB3")
    spread_sheet("B3", "A3", "B3mulA3")
