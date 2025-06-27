import random
import matplotlib.pyplot as plt
import movie_storage_sql as storage
import requests

omdb_key = "7f721055"

# this works: https://www.omdbapi.com/?t=inception&apikey=7f721055
def get_movie_detials_by_title(title):
    """
    Fetch movie Data for a given title from the API and return it.
    """
    url = "https://www.omdbapi.com/"
    params = {
        "t": title,
        "apikey": omdb_key

    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        if data.get("Response") == "True":
            return data
        else:
            print("No movies found.")
    else:
        print("Request failed with status code:", response.status_code)


def main():
  """Main"""
  # Dictionary to store the movies and the rating
  menu_function_pointer = {"0": ("Exit", exit),
    "1": ("List movies", list_movies),
    "2": ("Add movie", add_movie),
    "3": ("Delete movie", delete_movie),
    "4": ("Update movie", update_movie),
    "5": ("Stats", stats),
    "6": ("Random movie", random_movie),
    "7": ("Search movie", search_movie),
    "8": ("Sort by rating", movies_sorted_by_rating),
    "9": ("Generate Website", generate_website)}

  running=True
  while running:
      movies = storage.list_movies()

      choice = menu(menu_function_pointer)

      try:
          result = menu_function_pointer[choice][1](movies)
          if not result:
              running = False

      except KeyError:
          print("Wrong input. Enter a digit")


def exit(movies):
    print("Bye!")
    return False

def menu(menu_function_pointer):
    """Print the menu"""
    print()
    print("Menu:")
    for key, (description,_) in menu_function_pointer.items():
        print(f'{key} : {str(description)}')


    print()
    choice = input("Enter choice (0-9): ")

    print()
    return choice

def list_movies(movies):
    """List movies in the database"""
    print(f"{len(movies)} movies in total")
    for title,movie in movies.items():
        print(f'{title}, Rating: {movie["rating"]}, Year: {movie["year"]}')

    print()
    input("Press enter to return to the menu")


def add_movie(movies):
    """Add a movie to the database"""
    title = input("Enter the title of the movie you want to add: ")
    movie_details = get_movie_detials_by_title(title)
    year = movie_details['Year']
    rating = movie_details['Ratings'][0]['Value']
    poster = movie_details['Poster']

    if title in movies:
        yes_no = input("The title is already in the dictionary do you want to update it? Enter y or n:")
        if yes_no == "y":
            storage.update_movie(title,rating)
            print(f"Movie {title} successfully updated")

        else:
            input("Press enter to return to the menu")
            return movies
    else:
        storage.add_movie(title,year,rating,poster)
        print(f"Movie {title} successfully added")

    print()
    input("Press enter to return to the menu")

    return movies

def delete_movie(movies):
    """Delete a movie from the database"""
    title = input("Enter movie title to delete: ")
    if title in movies:
        storage.delete_movie(title)
        print(f"Movie {title} successfully deleted")
    else:
        print(f"Movie {title} doesn't exist!")

    print()
    input("Press enter to return to the menu")

    return movies

def update_movie(movies):
    """Update a movie in the database"""
    title = input("Enter movie title to update: ")
    rating = float(input(f"Enter the new rating of {title}: "))
    if title in movies:
        storage.update_movie(title,rating)
        print(f"Movie {title} successfully updated")
    else:
        print(f"Movie {title} doesn't exist!")
        yes_no = input("Do you want to add it? Enter y or n: ")
        if yes_no == "y":
            year = int(input("Enter the year the movie was released: "))
            storage.add_movie(title,year,rating)
            print(f"Movie {title} successfully added")

    print()
    input("Press enter to return to the menu")

    return movies

def stats(movies):
    """Provides stats of the ratings"""
    average = 0
    best = list(movies)[0]
    worst = best
    for movie in movies.values():
        average += movie["Rating"]
        if movie["Rating"] > movies[best]["Rating"]:
            best = movie["Title"]
        elif movie["Rating"] < movies[worst]["Rating"]:
            worst = movie["Title"]
    entries = len(movies)
    average = average / entries
    ratings = sorted([movie["Rating"] for movie in movies.values()])

    if entries % 2 == 0:
        median = (ratings[entries // 2 - 1] + ratings[entries // 2]) / 2
    else:
        median = ratings[entries // 2]

    print(f"Average rating: {average}")
    print(f"Median rating: {median}")
    print(f"Best Movie: {movies[best]}")
    print(f"Worst movie: {movies[worst]}")

    print()
    input("Press enter to return to the menu")

def random_movie(movies):
    """Selects a random movie"""
    title= list(movies)[random.randrange(0,len(movies))]
    print(f"Your movie for tonight: {movies[title]}")

    print()
    input("Press enter to return to the menu")

def search_movie(movies):
    """Searches for a substring of the movie title"""
    title_part= input("Enter part of movie name:").lower()

    for title in movies:
        if title_part in title.lower():
            print(f"{movies[title]}")

    print()
    input("Press enter to return to the menu")

def movies_sorted_by_rating(movies):
    """Sorting the movies by rating"""
    sorted_movies = dict(sorted(
        movies.items(),
        key=lambda item: item[1]["Rating"],
        reverse=True
    ))

    for title, info in sorted_movies.items():
        print(f'{title}: {info["Rating"]}')

    print()
    input("Press enter to return to the menu")

def generate_website(movies):
    """Generate a website based on a template to fill with movies from the database"""
    try:
        with open("_static/index_template.html", "r", encoding="utf-8") as f:
            template = f.read()
    except FileNotFoundError:
        print(f"Error: '{"_static/index_template.html"}' not found.")
        return

        # Replace placeholders
    website_title = input("Enter a title for your website: ")
    filled_html = template.replace("__TEMPLATE_TITLE__", website_title)

    movie_grid_html = ""

    for title,movie in movies.items():
        movie_poster = movie["poster"]
        movie_title = title
        movie_year = movie["year"]

        movie_grid_html += ("<li>"
                       "<div class= 'movie'>"
                       f"<img class='movie-poster' src= {movie_poster} title>"
                       f"<div class='movie-title'>{movie_title}</div>"
                       f"<div class='movie-year'>{movie_year}</div>"
                       "</div>"
                       "</li>")


    filled_html = filled_html.replace("__TEMPLATE_MOVIE_GRID__", movie_grid_html)

    # Write to output file
    with open("_static/index.html", "w", encoding="utf-8") as f:
        f.write(filled_html)

    print("Website was generated successfully.")




if __name__ == "__main__":
  main()
