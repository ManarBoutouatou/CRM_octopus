import pandas as pd
from django.core.management.base import BaseCommand 
from contact.models import Employee 
from sqlalchemy import create_engine
from django.conf import settings

class Command (BaseCommand): 
    help="A command to add data from an excel file to the databse" 
    
    def handle(self, *args, **options):
        excel_file = 'clients.xlsx'
        df = pd.read_excel(excel_file)
        engine = create_engine('sqlite:///:db.sqlite3')
        df.to_sql(Employee._meta.db_table, if_exists='replace', con=engine, index=False) 

