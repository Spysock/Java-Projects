#Programmer: Abody Majeed, 101227327

from T053_P1_load_data import load_dataset

book_dictionary = load_dataset("Google_Books_Dataset.csv")

def book_list(dictionary:dict)->list:
    """
    #Programmer: Jessica Richardson, 101236121
    
    Returns a list of books as dictionaries. Takes a dictionary as it's parameter
    >>>book_list(book_dictionary)
    
    """
    lst=[]
    for category in dictionary:
        book_l=dictionary[category]
        for book in book_l:
            book['category'] = category
            lst.append(book)
    return lst 
book_list(book_dictionary)


def sort_books_pageCount(dictionary: dict) -> list:
    """
    Programmer: Abody Majeed, 101227327
    
    This function takes a dictionary as it's parameter and returns a list where the books are sorted by
    page count in descending order
    
    >>>sort_books_pageCount(book_dictionary)
    [{'title': 'Summary: Think and Grow Rich', 'author': 'Nine99 Innovation Lab', 'rating': 0.0, 'publisher': 'Nine99 Innovation Lab (OPC) Pvt Ltd', 'page_count': 14, 'language': 'English', 'category': 'Economics'}, {'title': 'Summary: Think and Grow Rich', 'author': 'Nine99 Innovation Lab', 'rating': 0.0, 'publisher': 'Nine99 Innovation Lab (OPC) Pvt Ltd', 'page_count': 14, 'language': 'English', 'category': 'Business'}, {'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Alvin Hall', 'rating': 3.7, 'publisher': 'Hachette UK', 'page_count': 30, 'language': 'English', 'category': 'Economics'}

    """
    book_dict_to_list=[]
    for category in dictionary:
        book_l=dictionary[category]
        for book in book_l:
            book['category'] = category
            book_dict_to_list.append(book)
            
    book_x = len(lst)
    for i in range(book_x-1):
        for j in range(0, book_x-i-1):
            if book_dict_to_list[j]["title"] > book_dict_to_list[j+1]["title"]:
                book_dict_to_list[j], book_list[j+1] = book_dict_to_list[j+1], book_dict_to_list[j]
            if book_dict_to_list[j]['page_count'] > book_dict_to_list[j+1]['page_count']:
                book_dict_to_list[j], book_dict_to_list[j+1] = book_dict_to_list[j+1], book_dict_to_list[j]
    return book_dict_to_list, print(book_dict_to_list)
                
                
def sort_books_category(dictionary: dict)-> list:
    """
    Programmer: Abody Majeed, 101227327
    
    This function takes a dictionary as it's parameter and returns a list where the books are sorted by
    page count in descending order
    
    >>>sort_books_category(book_dictionary)
    [{'title': 'A Feast for Crows (A Song of Ice and Fire, Book 4)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'page_count': 864, 'language': 'English', 'category': 'Adventure'}, {'title': 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'page_count': 4544, 'language': 'English', 'category': 'Adventure'}, {'title': 'After Anna', 'author': 'Alex Lake', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'page_count': 416, 'language': 'English', 'category': 'Adventure'}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'rating': 4.8, 'publisher': 'Tor Books', 'page_count': 226, 'language': 'English', 'category': 'Adventure'}

    """
    book_dict_to_list=[]
    for category in dictionary:
        book_l=dictionary[category]
        for book in book_l:
            book['category'] = category
            book_dict_to_list.append(book)      
    book_x = len(lst)
    for i in range(book_x-1):
        for j in range(0, book_x-i-1):
            if book_dict_to_list[j]["title"] > book_dict_to_list[j+1]["title"]:
                book_dict_to_list[j], book_dict_to_list[j+1] = book_dict_to_list[j+1], book_dict_to_list[j]
            if book_dict_to_list[j]['category'] > book_dict_to_list[j+1]['category']:
                book_dict_to_list[j], book_dict_to_list[j+1] = book_dict_to_list[j+1],book_dict_to_list[j]  
    return book_dict_to_list, print(book_dict_to_list)
    



