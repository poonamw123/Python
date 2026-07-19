class BookStore:
    # Class Variable
    NoOfBooks = 0
    
    # Constructor
    def __init__(self, Name, Author):
        self.Name = Name
        self.Author = Author
        BookStore.NoOfBooks += 1
        
    # Instance method
    def Display(self):
        print(f"{self.Name} by {self.Author}. No of Books : {BookStore.NoOfBooks}")
        
# Creating objects
obj1 = BookStore("Linux System Programming", "Robert Love")
obj1.Display()

obj2 = BookStore("C Programming", "Dennis Ritchie")
obj2.Display()

