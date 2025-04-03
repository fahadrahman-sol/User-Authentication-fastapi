import os

# Define the directory structure
project_structure = {
    "app": [
        "main.py",
        "database.py",
        "models.py",
        "schemas.py",
        "auth.py",
        "utils.py",
        "middleware.py",
    ],
    "app/routes": ["__init__.py", "users.py"],
    "tests": ["test_users.py"],
}

# Create directories and files
for folder, files in project_structure.items():
    os.makedirs(folder, exist_ok=True)
    for file in files:
        file_path = os.path.join(folder, file)
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write("# " + file)  # Write a comment in each file
            print(f"Created: {file_path}")

# Create project-level files
project_files = [".env", "requirements.txt", "Dockerfile", "README.md"]
for file in project_files:
    if not os.path.exists(file):
        with open(file, "w") as f:
            f.write("# " + file)  # Write a comment in each file
        print(f"Created: {file}")

print("Project structure created successfully!")
