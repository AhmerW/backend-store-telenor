if __name__ == "__main__":
    import uvicorn

    from core.settings import DEV_SETTINGS
    from server import app

    uvicorn.run(
        "server:app",
        host=DEV_SETTINGS.HOST,
        port=DEV_SETTINGS.PORT,
        reload=True,
    )
