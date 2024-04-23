FROM python:3

WORKDIR /app

COPY requirements1.txt ./

RUN pip install --upgrade pip

RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

RUN pip install --no-cache-dir -r requirements1.txt

COPY . .

EXPOSE 8010

CMD ["python", "chat.py"]