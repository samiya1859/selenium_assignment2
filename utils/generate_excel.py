import xlsxwriter

def generate_excel(key, page, url, test_results, filename="test_results.xlsx"):
    """
    Generates an Excel file summarizing the test results.

    Args:
    key (str): The test key, typically the domain name.
    page (str): The type of page being tested.
    url (str): The base URL used for the test.
    test_results (list): A list of test results with comparison data.
    filename (str): The name of the output Excel file.
    """
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()

    # Define headers
    headers = ["Key", "URL", "Page", "Test Case", "Passed", "Comments"]
    for col, header in enumerate(headers):
        worksheet.write(0, col, header)

    # Write data rows
    for row_idx, result in enumerate(test_results, start=1):
        worksheet.write(row_idx, 0, key)
        worksheet.write(row_idx, 1, url)
        worksheet.write(row_idx, 2, page)
        worksheet.write(row_idx, 3, result.get("test_case", "N/A"))
        worksheet.write(row_idx, 4, "Pass" if result.get("passed") else "Fail")
        worksheet.write(row_idx, 5, ', '.join(result.get("comments", [])))

    workbook.close()
