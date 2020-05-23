import pyrebase

}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

# db.child('books').push({'author': 'Test Author', 'book': 'Test Book', 'bookid':2, 'cover':'https://google.com'})
books = db.child('books').get().each()
# posts = db.child('posts').get().each()
posts = db.child('posts').get().each()
# posts = db.child('posts').order_by_child('book_id').equal_to(1).get().each()
# db.child('posts').push({'book_id':1,'post_author': 'Admin', 'post': 'Lorem Ipsum Dolor'})
# db.child('posts').push({'book_id':1,'post_author': 'Admin2', 'post': 'Very nice book'})

# posts = [x for x in posts if posts.val()['book_id']==1]
# for x in posts:
#     print(x.val())
book_posts = []
for x in posts:
    if x.val()['book_id']==1:
        book_posts.append(x)

# print(book_posts)

all_books = db.child('books').get().each()
# def get_book(id):
#     for x in all_books:
#         if x.val()['book_id'] == id:
#             selected_book = x
#     return selected_book
#
# print(get_book(3))