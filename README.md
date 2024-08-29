# Clean Architecture Application in Python and Flask

## About the Application

This project is a demonstration of Clean Architecture principles applied to a Python application using the Flask framework. The application is structured around the Domain-Driven Design (DDD) methodology to ensure a modular, scalable, and maintainable codebase. It leverages Docker for containerization, making the development and deployment process straightforward and consistent across different environments.

### Key Features:
- **Clean Architecture**: Incorporates a decoupled architecture that separates core business logic from interface and infrastructure concerns. This separation enhances maintainability and allows for independent development and testing of each layer.
- **Domain-Driven Design (DDD)**: Focuses on complex domain logic centralizing the business logic in the domain layer. This approach facilitates a deeper understanding and management of the domain model which is particularly beneficial for complex applications.
- **Docker Integration**: Utilizes Docker to encapsulate the application environment, ensuring that it runs uniformly across different setups. Docker simplifies dependencies management and aligns development environments to production configurations.
- **SQL Database**: Employs a SQL database to manage application data, providing robust, reliable, and scalable data storage solutions.
- **ORM Tool**: Uses an Object-Relational Mapping (ORM) tool to abstract database interactions, simplifying data manipulation and ensuring database agnosticism. This abstraction allows developers to focus more on the domain logic rather than database specifics.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework in Python that provides tools, libraries, and technologies to build a web application.
- **SQLAlchemy**: An ORM and SQL toolkit for Python that provides a full power and flexibility of SQL.
- **MySQL/PostgreSQL**: Supported SQL databases that provide reliable backends for storing persistent data of the application.
- **Docker**: A set of platform as a service products that use OS-level virtualization to deliver software in packages called containers.

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


