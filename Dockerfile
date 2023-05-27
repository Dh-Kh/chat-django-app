FROM python:3.11

WORKDIR /app/chat_folder

COPY requirements.txt .

RUN grep -v twisted-iocpsupport requirements.txt | xargs -n 1 pip install --no-cache-dir

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]