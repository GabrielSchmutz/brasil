setup:
	@python -m pip install --upgrade pip
	@pip install -r requirements.txt

run:
	@uvicorn app.main:app --reload --loop asyncio --host 0.0.0.0
