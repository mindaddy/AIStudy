import uuid
from uuid import UUID
from datetime import datetime
import csv

class Movie:
    id : UUID
    title: str

    def __init__(self, title: str):
        self.id = uuid.uuid4()
        self.title = title

class Ticket:
    id: UUID
    movie_id: UUID
    time: datetime 
    
    def __init__(self, movie: Movie, time: datetime):
        self.id = uuid.uuid4()
        self.movie_id = movie.id
        self.time = time

if __name__ == "__main__":
    # Create a movie instance
    movie = Movie("Inception")
    
    # Print movie details
    print(f"Movie ID: {movie.id}")
    print(f"Movie Title: {movie.title}")
    
    # Create a ticket instance
    ticket = Ticket(movie, datetime.now())
    
    # Print ticket details
    print(f"Ticket ID: {ticket.id}")
    print(f"Movie ID: {ticket.movie_id}")
    print(f"Time: {ticket.time}")
    
    # Save movie details to CSV
    with open('movie.csv', mode='w', newline='') as movie_file:
        movie_writer = csv.writer(movie_file)
        movie_writer.writerow(['Movie ID', 'Movie Title'])
        movie_writer.writerow([movie.id, movie.title])
    
    # Save ticket details to CSV
    with open('ticket.csv', mode='w', newline='') as ticket_file:
        ticket_writer = csv.writer(ticket_file)
        ticket_writer.writerow(['Ticket ID', 'Ticket Movie ID', 'Ticket Time'])
        ticket_writer.writerow([ticket.id, ticket.movie_id, ticket.time])
