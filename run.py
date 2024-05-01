from app import create_app
print(30*"Debugando\n")
app = create_app()

if __name__ == '__main__':
    app.run(debug=False)