FROM apache/airflow

WORKDIR /opt/airflow

RUN pip install pyarrow
RUN pip install sqlalchemy
RUN pip install pandas

