from src.registry import app

def main():
    print("Starting Docker Registry on port 5000...")
    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    main()
