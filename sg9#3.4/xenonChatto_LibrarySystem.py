class Publication:
    def __init__(self, title: str, author: str):
        self.__title = title
        self.__author = author

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def set_author(self, author: str):
        self.__author = author

    def display_info(self):
        print(f"Title: {self.__title}, Author: {self.__author}")

class Book(Publication):
    def __init__(self, title: str, author: str, num_of_pages: int):
        super().__init__(title, author)
        self.__num_of_pages = num_of_pages

    def set_num_of_pages(self, num_of_pages: int):
        if num_of_pages>0:
            self.__num_of_pages = num_of_pages

        else:
            print("Number of pages must be positive.")

    def get_num_of_pages(self):
        return self.__num_of_pages

class Magazine(Publication):
    def __init__(self, title: str, author: str, issue_num: int):
        super().__init__(title, author)
        self.__issue_num = issue_num

    def set_issue_num(self, issue_num: int):
        if issue_num > 0:
            self.__issue_num = issue_num
        else:
            print("Issue number must be positive.")

    def get_issue_num(self):
        return self.__issue_num

    def get_num_of_pages(self):
        return self.__num_of_pages


pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongon, H.)")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)

print("Publication information:")
pub1.display_info()

print("\nBook Information:")
book1.display_info()
print(book1.get_num_of_pages())

print("\nMagazine Information:")
mag1.display_info()
print(mag1.get_issue_num())