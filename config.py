from dotenv import load_dotenv
import os

load_dotenv()

user=os.environ["POSTGRESQL_USER"]
password=os.environ["POSTGRESQL_PASSWORD"]
host=os.environ["POSTGRESQL_HOST"]
database=os.environ["POSTGRESQL_DATABASE"]
server=os.environ["POSTGRESQL_SERVER"]

DATABASE_CONNECTION_URI=f'{server}://{user}:{password}@{host}/{database}'

