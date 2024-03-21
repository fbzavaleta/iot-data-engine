import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.pool import QueuePool
from sqlalchemy import select, column
from sqlalchemy.exc import SQLAlchemyError
from typing import Dict, Any

from engine.core.enums.common import DatabaseParameters, DbPoolParameters
"""
Author: Francis Benjamin Zavaleta, Eng
Copyright © fbzavaleta. All rights reserved.
"""

mysql_credencials = {
    'username' : DatabaseParameters.db_user,
    'password' : DatabaseParameters.db_password,
    'endpoint' : DatabaseParameters.db_host,
    'db_name'  : DatabaseParameters.db_name,
    'port'     : DatabaseParameters.db_port 
}


class DBConnectionPoolSingleton:
    __instance = None
    @staticmethod
    def get_instance():
        if DBConnectionPoolSingleton.__instance is None:
            DBConnectionPoolSingleton()
        return DBConnectionPoolSingleton.__instance

    def __init__(self):
        if DBConnectionPoolSingleton.__instance is not None:
            raise Exception("You cannot create more than one instance of DBConnectionPoolSingleton.")
        else:
            # Create the connection pool with a maximum of 10 connections
            conn_string = "mysql+mysqlconnector://{username}:{password}@{endpoint}:{port}/{db_name}".format(**mysql_credencials)
            engine = create_engine(conn_string, poolclass=QueuePool, pool_size=DbPoolParameters.pool_size, 
                                   max_overflow=DbPoolParameters.max_overflow, pool_recycle=DbPoolParameters.pool_recycle, pool_timeout=DbPoolParameters.pool_timeout)
            self.Session = scoped_session(sessionmaker(bind=engine))
            DBConnectionPoolSingleton.__instance = self


class MysqlEngine():
    def __init__(self):
        db_connection_pool = DBConnectionPoolSingleton.get_instance()
        Session = db_connection_pool.Session
        self.current_session = Session()

    def insert_row(self, table_cls , data: Dict[str, Any]) -> bool:
        new_row = table_cls(**data)
        try:
            self.current_session.add(new_row)
            self.current_session.commit()
            return True
        except SQLAlchemyError as e:
            print(e)
            self.current_session.rollback()
            return False

    def select_one(self, objecttable, colselected_list, colfilter, targetvalue, fetch_all:bool=False):
        columns_selected = [column(col) for col in colselected_list]
        column_filter = column(colfilter)

        query = select(*columns_selected).where(column_filter == targetvalue).select_from(objecttable)
        result = self.current_session.execute(query)

        if fetch_all:
            return result.fetchall()
        
        return result.fetchone()
    
    def group_by(self, objecttable, colselected_list, colfilter, targetvalue):
        columns_selected = [column(col) for col in colselected_list]
        column_filter = column(colfilter)

        query = select(*columns_selected).where(column_filter == targetvalue).select_from(objecttable)
        result = self.current_session.execute(query)
    
        return result.fetchone()
    
    def update_table(self, object_table, key_value, values:dict):
        row = self.current_session.query(object_table).filter(object_table.id == key_value).first()
        for key, values in values.items():
            setattr(row, key, values)
        self.current_session.commit()    
        self.current_session.close()

    def execute_query(self, filepath: str) -> bool:
        if not os.path.isfile(filepath):
            raise FileNotFoundError(f"File '{filepath}' not found.")
        try:
            with open(filepath, 'r') as file:
                queries = file.read().split(';')
                for query in queries:
                    if query.strip():
                        self.current_session.execute(query)
            self.current_session.commit()
            return True
        except SQLAlchemyError as e:
            self.current_session.rollback()
            return False

