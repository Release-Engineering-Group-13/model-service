FROM python:3.10
WORKDIR /root
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src src 
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["src/serve_model.py"]