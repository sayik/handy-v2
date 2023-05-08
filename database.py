# download dependencies
from sqlalchemy import create_engine
from sqlalchemy import text

db_connection_string = "mysql+pymysql://p6vs105f0uc1wdwxthoi:pscale_pw_hPG4GN6T7UeDYLoaREMZml6yBTNfV17seWdlB5fGfKP@aws.connect.psdb.cloud/handyheros?charset=utf8mb4"

# creating an engine and conneting it to a remote server
engine = create_engine(db_connection_string, connect_args={"ssl": {"ssl_ca": "/etc/ssl/cert.pem"}})

# with engine.connect() as conn:
#     result = conn.execute(text("select * from talents"))
    
#     result_dicts = []
#     for row in result.all():
#         result_dicts.append(dict(zip(result.keys(), row)))

# loads data from database using several objects
def load_talents_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from talents"))
        talents = []
        for row in result.all():
            talents.append(dict(zip(result.keys(), row)))
        return talents

    
    
    # print(type(result))
    # #print(result.all())
    # result_all = result.all()
    # first_dict = dict(zip(result.keys(), result_all[0]))
    # print(type(first_dict))
    # print(first_dict)



