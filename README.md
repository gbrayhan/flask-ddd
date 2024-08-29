# Online Library

## Description

The Online Library is a Flask application that allows users to manage a catalog of books. Users can add, delete, update, and query books in a database.

## Features

- **Add Books**: Allows users to add books to the database.
- **Delete Books**: Users can remove books from the catalog.
- **Update Books**: Facilitates updating book information.
- **Query Books**: Users can view the list of available books and search by various criteria.

## Technologies Used

- **Flask**: A microframework for Python based on Werkzeug, Jinja 2, and good intentions.
- **SQLAlchemy**: ORM used for interacting with the database.
- **MySQL**: Relational database management system.

## Environment Setup

### Prerequisites

- Python 3.8+
- pip
- virtualenv (optional)
- Docker

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/user/OnlineLibrary.git cd OnlineLibrary
 
   ```  


2. **Set Up the Virtual Environment (Optional):**
    
   ```bash
   python -m venv venv source venv/bin/activate # On Windows use venv\Scripts\activate
   ```
   
3. **Install Dependencies:**
    
    ```bash
   pip install -r requirements.txt
   ```
4. **Docker Configuration:**

- Ensure you have Docker and Docker Compose installed.
- Launch the services:

   ```bash  
   docker-compose up -d
   ```


### Usage

To start the application, run:

```bash
flask run --host=local --port=5001
```

The API will be available at `http://localhost:5001`.

### Endpoints

- **POST /books**: Adds a new book.
- **GET /books**: Lists all books.
- **PUT /books/{id}**: Updates a specific book.
- **DELETE /books/{id}**: Deletes a book.

## Contributing

To contribute to the project, please follow these steps:

1. **Fork the Repository**: Fork the project to your personal account.
2. **Create a Branch**: Create a branch for each feature or improvement.
3. **Make Your Changes**: Add or modify functionalities.
4. **Submit a Pull Request**: To merge your changes into the main project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.


