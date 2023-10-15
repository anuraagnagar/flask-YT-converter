## YouTube video converter to MP3.

A Simple Converter and download YouTube videos to MP3 audio format using this simple web application built using Flask/Python.

## Prerequisites

Before you can run this application, make sure you have the following prerequisites installed on your system:

- [Python](https://www.python.org/downloads/) (>= 3.6)
- [pip](https://pip.pypa.io/en/stable/installation/)

## Library & Extension

- ![Flask](https://flask.palletsprojects.com/)
- ![pytube](https://pytube.io/en/latest/)

## Installation & Set up locally.

### 1. Clone the git repository.

```bash
git clone https://github.com/anuraagnagar/flask-YT-converter.git
```

### 2. Go to the project directory.

```bash
cd flask-YT-converter
```

### 3. Create virtual environment.

```bash
python3 -m venv venv
```

### 4. Activate the environment.

On Windows

```bash
venv\scripts\activate
```

On MacOS/Linux

```bash
source venv/bin/activate
```

### 5. Install the requirement package.

```bash
pip install -r requirements.txt
```

Before running the server, you will need to set `SECRET_KEY=your_app_secret_key_here` environment variable to .env file in your base directory. And change `.env.example` file to `.env` file in base directory of this application and set the secret key.

### 6. Run the application.

```bash
flask run
```

To access this application you need to open `http://127.0.0.1:5000` in your web browser.

## Contributing

Contributions are welcome! If you find a bug or want to add a new feature, please open an issue or submit a pull request.
For more information checkout ![CONTRIBUTING.md](https://github.com/anuraagnagar/flask-YT-converter/blob/main/CONTRIBUTING.md)

## Licence

By contributing to this project, you agree that your contributions will be licensed under the ![MIT License](https://github.com/anuraagnagar/flask-YT-converter/blob/main/LICENSE).
