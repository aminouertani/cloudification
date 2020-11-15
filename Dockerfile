FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python -m spacy download en
ENTRYPOINT ["python"]
CMD ["app.py"]
