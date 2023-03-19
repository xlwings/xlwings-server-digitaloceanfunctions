import xlwings as xw


def main(args):
    # Instantiate a Book object with the deserialized request body
    book = xw.Book(json=args)

    # Use xlwings as usual
    sheet = book.sheets[0]
    cell = sheet["A1"]
    if cell.value == "Hello xlwings!":
        cell.value = "Bye xlwings!"
    else:
        cell.value = "Hello xlwings!"

    # Pass the following back as the response
    return {"body": book.json()}
