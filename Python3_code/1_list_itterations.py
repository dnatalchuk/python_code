#!/usr/bin/python3
movies = ["Holy Grail","The life of brain","The meaning of life"]
for i in movies:
    y = movies.index(i)
    years = ['1975', '1979', '1983']
    years_index = y + 1
    movies.insert(years_index, years[y]);
    print(movies);
