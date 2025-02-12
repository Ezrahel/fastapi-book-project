FROM python:3.12.6

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt 

EXPOSE 8000

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0","--port", "8000" ]