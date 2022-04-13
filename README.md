# Random objects generator
A web application for generating random objects with Python Django framework

# Application flowchart
```mermaid
flowchart TD
B[Alphabetical String] --> A[Random Objects]
C[Integer Numbers] --> A[Random Objects]
DB[Real Numbers] --> A[Random Objects]
E[Alphanumerics String] --> A[Random Objects]
A[Random Objects] --> F[Generate text file within 2MB]
F[Generate text file within 2MB] --> H[Download Text file]
A[Random Objects] --> G[View report]
G[View report] --> I[Display count report]
```

# Prerequisite

- [x] Need to have Python's latest version - 3.9.7
- [x] Need to have Django - 4.0.4

# Installations

- Clone this repository in your preferable directory
- Active virtual environment
```
python -m venv env
env\Scripts\activate
```
- Install ` requirements.txt ` file

```
pip install -r requirements.txt
```
# Run Server

```
python manage.py runserver
```

# Test Application

- Click the `Generate ` button to generate four types of random objects
- After appearing the `Download random objects file...` click it to download a text file consisting of these four types of random objects within ~2MB
- Click the `View Report` button to show the stats of random objects. There will be a count stats of these each object 