from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
	"""
	Displays the stocks screen dashboard / homepage
	"""
	return templates.TemplateResponse("home.html", {
		"request": request
	})


@app.post("/stock")
def create_stock():
	"""
	Creates a stock and save it in database
	"""
	return {
		"code": "success",
		"message": "stock created"
	}
