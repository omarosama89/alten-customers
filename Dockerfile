FROM python:3
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
RUN mkdir /customers_code
WORKDIR /customers_code
COPY . /customers_code/
RUN chmod +x entry-point.sh
#COPY requirements.txt /customers_code/
RUN pip install -r requirements.txt
#CMD ["python", "manage.py", "migrate"]
#CMD python ./manage.py migrate
