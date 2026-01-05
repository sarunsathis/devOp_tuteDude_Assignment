FROM python:3.8-alpine
WORKDIR /app
ADD . .
RUN pip install -r requirement.txt
ENTRYPOINT ["python"]
CMD ["app.py"]