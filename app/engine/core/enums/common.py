from dataclasses import dataclass
"""
Author: Francis Benjamin Zavaleta, Eng
Copyright © fbzavaleta. All rights reserved.
"""

@dataclass(frozen=True)
class DatabaseParameters:
    db_name: str = 'tks_engine'
    db_user: str = 'root'
    db_password: str = 'root'
    db_host: str = '172.17.0.1' #default gateway for docker
    db_port: str = '3306' #default port for mysql


@dataclass(frozen=True)
class DbPoolParameters:
    pool_size: int = 10
    max_overflow: int = 20
    pool_recycle: int = 300
    pool_timeout: int = 2
    pool_pre_ping: bool = True
    pool_use_lifo: bool = True

@dataclass(frozen=True)
class ApiNotes:
    developer: str = '@fbzavaleta'
    email: str = 'benjamin.zavaleta@grieletlabs.com'
    source: str = 'https://thingspeak.com'