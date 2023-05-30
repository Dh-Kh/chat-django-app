FROM python:3.10
ENV PYTHONUNBUFFERED 1
WORKDIR /chat_app
COPY requirements.txt /chat_app/
RUN grep -v twisted-iocpsupport requirements.txt | xargs -n 1 pip install --no-cache-dir
COPY . /chat_app/
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]