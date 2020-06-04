from scraps import gsheets

books, posts = gsheets.main()
books, posts = books[1:], posts[1:]

book_dicts = []
post_dicts = []
for x in books:
    book_dicts.append({
    'book_id': x[0],
    'book': x[1],
    'author': x[2],
    'book_cover': x[3],
    })

for y in posts:
    post_dicts.append({
    'book_id': x[0],
    'post_author': x[1],
    'post': x[2],
    })

print(book_dicts)
print(post_dicts)
