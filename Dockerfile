FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.douban.com/simple

COPY . .

CMD [ "flask", "run", "--host=0.0.0.0" ]