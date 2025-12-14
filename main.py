from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/blog")
def index():
    return

@app.post('/blog')
def create_blog():
    return

@app.get("blog/unpublished")
def unpublished():
    return

@app.get("blog/{id}")
def show(id: int):
    return


@app.get("blog/{id}/comments")
def comments(id):
    return


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)

# uvicorn Blog.main:app --reload

3