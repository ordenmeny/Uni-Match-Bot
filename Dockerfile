FROM python:3.12-bookworm

WORKDIR /bot

COPY . .

RUN pip install --no-cache-dir -r req.txt

CMD ["python", "run.py"]