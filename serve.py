import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "server:app",
        host=str("0.0.0.0"),
        port=int(19003),
        reload=False,
        log_level="info",
        workers=1
    )