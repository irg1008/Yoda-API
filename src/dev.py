import uvicorn

if __name__ == "__main__":
    port=8000
    print(f"Executing on http://localhost:{port}")
    uvicorn.run("main:app", port=port, reload=True)
