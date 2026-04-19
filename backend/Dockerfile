FROM python:3.12

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8081

COPY . /app
RUN chmod +x /app/entrypoint.sh

CMD ["/app/entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8081"]
