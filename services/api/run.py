# from services.api.app.app import create_app

# app = create_app()

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=3080, debug=True)


import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.app:app", port=3080, reload=True)