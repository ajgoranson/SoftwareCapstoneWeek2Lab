#Create the Author class

class Author:
    # define the variables needed
    def __init__ (self, name):
        self.name = name
        # set the books object to be a set so no duplicate data could be added
        self.books = set()
        


    def publish(self, title):
        #Had to change the append method to an add method because sets dont take the append method
        self.books.add(title)
        


    # this is createing a print statement if the author has books or doesnt have books it will print a different message
    def __str__(self):
        if self.books:
            book_list = ', '.join(self.books)
        else:
            book_list = 'no books'    


        return f'Name: {self.name} has published {book_list}' 


# adding data in the main method
def main():

    shakespeare = Author('William Shakespeare')
    shakespeare.publish('Hamlet')
    shakespeare.publish('Richard III')

    print(shakespeare)

    george_rr_martin = Author('George R. R. Martin')
    george_rr_martin.publish('A Game of Thrones')
    george_rr_martin.publish('The Winds of Winter')
    george_rr_martin.publish('A Dance with Dragons')
    george_rr_martin.publish('Fire and Blood')
    george_rr_martin.publish('A Clash of kings')
    george_rr_martin.publish('A Strom of Swords')

    #this will print all his work
    print(george_rr_martin)

#call the main method
main()