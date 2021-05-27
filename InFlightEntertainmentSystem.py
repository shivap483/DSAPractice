def can_two_movies_fill_flight(movie_lengths, flight_length):
    movie_lengths_seen = set()

    for first_movie_length in movie_lengths:
        matching_second_movie_length = flight_length - first_movie_length
        if matching_second_movie_length in movie_lengths_seen:
            return True
        movie_lengths_seen.add(first_movie_length)
    return False


flight_length = 6
movie_lengths = [2.2, 3.8, 2, 4]
var = can_two_movies_fill_flight(movie_lengths, flight_length)
print(var)
