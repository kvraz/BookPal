import requests

class Book:

    @staticmethod
    def find_book(given_name):

        url = 'https://www.googleapis.com/books/v1/volumes'
        params = {'q': given_name}
        response = requests.get(url, params=params)
        data = response.json()

        if 'items' in data:
            book = data['items'][0] if data['items'] else None
        else:
            book = None

        if book:
            title = book['volumeInfo']['title']
            authors = ', '.join(book['volumeInfo']['authors']) if 'authors' in book['volumeInfo'] else 'Unknown'
            published_date = book['volumeInfo']['publishedDate'] if 'publishedDate' in book['volumeInfo'] else 'Unknown'
            publisher = book['volumeInfo']['publisher'] if 'publisher' in book['volumeInfo'] else 'Unknown'
            language = "'"+book['volumeInfo']['language']+"'" if 'language' in book['volumeInfo']  else 'Unknown' 
            description = book['volumeInfo']['description'] if 'description' in book['volumeInfo'] else 'Description not available'
            buy_link = book['saleInfo']['buyLink'] if 'saleInfo' in book and 'buyLink' in book['saleInfo'] else "not available"
            details = "Found it! "+title+", by "+authors+". What would you like to know about this book?"
            publish_info = published_date+" by publisher "+publisher

            #the book info table is designed to correspond to a specific question, according to its index (ex. book_info[1] refers to question 2 regarding publishing information)
            book_info =  [
                details,
                publish_info,
                language,
                description,
                buy_link,
            ]
            return book_info
        else:
            return None
