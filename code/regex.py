import re
from book import Book

# Predefined sentence templates and their corresponding responses
patterns_responses = [
    (r'hello|hi|hey', 'Hello there! I am BookPal, your virtual book assistant! What book would you like to know about?'),
    (r'(.*)(thank you|thanks|(good)?bye)', 'Have a nice day end enjoy reading!'),
    (r'(.*)when(.*)published|(.*)publish date','It was published in '),    
    (r'(.*)(what|which)?(.*)language', 'It is written in '),
    (r'(.*)(give|provide|tell)(.*)(description|info|details|summary)', 'Sure! Here is what I found on Google:\n\n'),
    (r'(.*)(buy|purchase) (link|it)', 'Based on my knowledge, the buy link is '),
    (r'(.*?)(know about|know|tell me about)( the| a)?( book named| book called)? (.*)', 'Sure, I can look \'%s\' up!\n\n')   
]

def chatbot(input_sentence):
    global book_info
    for index, (pattern, response) in enumerate(patterns_responses):
        
        match = re.match(pattern, input_sentence.lower())
        
        if match:
            if index == 6:    #meaning it is the question that searches for the book
                book_info = Book.find_book(match.group(5))  #initialize all book data
                if book_info:
                    return response % match.group(5) + book_info[0] #returns the response text, followed by a copy of the title the user gave and the first row of the book info table, which refers to title and author that was found by the api, using the user input
                else: return "Sorry, I couldn't find information about that book."  #alternative message in case the api does not find a book
            else:   #the rest of the questions
                if index > 1 and book_info: return response + book_info[index-1]  #checks if the index is greater than 1, because the first 2 questions do not require data from the book info table. if they do, it retrieves the info from the corresponding row of the table
                else: return response   #simple response for the first two questions
    else: return "I'm sorry, I didn't understand that." #default answer