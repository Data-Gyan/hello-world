from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def hello():
    return "(Hello-World..!  Welcome to first fastapi app.)"

@app.get("/greetme/{name}")
async def greet(name):
    return "Dear {0}, You are very welcome here !".format(name)

@app.get("/test/")
async def test():
    return "Testing Passed...!"


