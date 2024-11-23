import sys
movies = int(input())

lowest_rating_movie_name = ''
lowest_rating = sys.maxsize
top_rating_movie_name = ''
top_rating = -sys.maxsize
current_rating = 0
total_rating = 0

for idx in range(movies):
    movie_name = input()
    rating = float(input())
    total_rating += rating

    if rating > top_rating:
        top_rating_movie_name = movie_name
        top_rating = rating

    elif rating < lowest_rating:
        lowest_rating_movie_name = movie_name
        lowest_rating = rating

print(f'{top_rating_movie_name} is with highest rating: {top_rating :.1f}')
print(f'{lowest_rating_movie_name} is with lowest rating: {lowest_rating :.1f}')
print(f'Average rating: {total_rating / movies :.1f}')
