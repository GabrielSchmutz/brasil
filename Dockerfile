FROM python:3.12-bookworm

COPY . /brasil
WORKDIR /brasil

RUN make setup

CMD uvicorn app.main:app --reload --loop asyncio --host 0.0.0.0

