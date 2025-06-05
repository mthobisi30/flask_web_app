# Flask Web App

This is a simple Flask-based web application for managing tasks.
It features user registration, login, task creation, editing, deletion, pagination, and a REST API — all built using the MVC pattern and styled with Tailwind CSS. 
The app is deployable for free using Render.

________________________________________________________________

## Features

- User authentication (Register, Login, Logout)
- Task CRUD (Create, Read, Update, Delete)
- Pagination and task filtering/search
- REST API endpoint (JSON responses)
- Modern UI with Tailwind CSS
- MVC architecture (Models, Views, Controllers)
- Deployed for free on [Render](https://render.com)

________________________________________________________________

## Default Login Credentials

- username: admin
- Password: password123

________________________________________________________________

## Tech Stack

| Layer          | Technology        |
|----------------|-------------------|
| Backend        | Python, Flask     |
| Frontend       | HTML, Tailwind CSS|
| Deployment     | Gunicorn, Render  |
| API            | Flask JSON (REST) |

________________________________________________________________

## Folder Structure

```
project/
├── app.py                 # Main app file
├── controllers/           # Route controllers (e.g., auth, tasks)
├── models/                # Database models (e.g., User, Task)
├── templates/             # HTML templates 
├── static/                # CSS, JS, assets
├── requirements.txt       # Python dependencies
├── Procfile               # Deployment config for Render
├── runtime.txt            # Python version (optional)
├── README.md              # You're reading it!
```

________________________________________________________________

## Local Development

### 1. Clone the Repository

```bash
git clone https://github.com/mthobisi30/flask_web_app.git
cd flask_web_app
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate      # macOS/Linux
.venv\Scripts\activate       # Windows
```

### 3. Install the Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

Now open your browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

________________________________________________________________

## Deployed Application Link

The Application was deployed using render:

[Flask Web App](https://flask-web-app-eato.onrender.com)

________________________________________________________________

## Author

**Mthobisi Nxumalo**  
South Africa  
mthobosinx@icloud.com

[GitHub](https://github.com/mthobisi30)

________________________________________________________________

## License

This project is licensed under the **MIT License**.  
Feel free to use, modify, and share. See the [LICENSE](LICENSE) file for more details.



