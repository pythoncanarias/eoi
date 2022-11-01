import wikipedia


if __name__ == '__main__':

    page_content= wikipedia.page( "Carols Shaw" )  # .content

    # outputs the text content of the page on wikipedia
    print(page_content)