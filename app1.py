import db
import sys
import logging
import rds_config
import pymysql
from registers import regType0, regType1, regType2, regType3, regType4, regType5, regType9
import scanner
import os
import boto3
import botocore

#rds settings
rds_host  = "thefelpsmysql1.cvxtfgxwsweb.us-east-1.rds.amazonaws.com"
# rds_host  = "localhost"
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name

logger = logging.getLogger()
logger.setLevel(logging.INFO)


i=0
def handler(event, context):
    """
    Bucket connect and config
    """
    BUCKET_NAME = 'thefelpsbucket01'
    file_obj = event['Records'][0]
    logger.info("FILE_OBJ: "+str(file_obj))
    mykey = str(file_obj['s3']['object']['key'])
    logger.info("MYKEY: "+mykey)
    s3 = boto3.resource('s3')
    try:
        s3.Bucket(BUCKET_NAME).download_file(mykey, '/tmp/' + mykey)
        logger.info("File downloaded from bucket to /tmp/")
        BASE_DIR = '/tmp/'
        txtfiles=[]
        for file in os.listdir(BASE_DIR):
            if file.endswith(".TXT"):
                txtfiles.append(file)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            logger.info("The object does not exist.")
        else:
            raise
        
    
    """
    DB connect and config
    """
    try:
        conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
    except:
        logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
        sys.exit()
    logger.info("SUCCESS: Connection to RDS mysql instance succeeded")

    txtfiles=scanner.scan()
    
    """
    Loop through all files within '/tmp/'
    """
    for txtfile in txtfiles:    
        filename=txtfile
        with open(os.path.join(BASE_DIR,filename), encoding ='latin1') as file:
            data=file.readlines()
            tipo0=tipo1=tipo2=tipo3=tipo4=tipo5=tipo9=0
            """
            This function fetches content from mysql RDS instance
            """
            item_count = 0
            with conn.cursor() as cur:
                try:
                    cur.execute(db.create_type_0())
                except:
                    logger.info("Skipping creation of table Type 1")
                try:
                    cur.execute(db.create_type_1())
                except:
                    logger.info("Skipping creation of table Type 1")
                try:
                    cur.execute(db.create_type_2())
                except:
                    logger.info("Skipping creation of table Type 2")
                try:
                    cur.execute(db.create_type_3())
                except:
                    logger.info("Skipping creation of table Type 3")
                try:
                    cur.execute(db.create_type_4())
                except:
                    logger.info("Skipping creation of table Type 4")
                try:
                    cur.execute(db.create_type_5())
                except:
                    logger.info("Skipping creation of table Type 5")
                try:
                    cur.execute(db.create_type_9())
                except:
                    logger.info("Skipping creation of table Type 9")
                for i in range(len(data)):
                    if data[i][0:1]== '0':
                        tipo0 += 1
                        regType0(data[i], cur)
                        conn.commit()
                    elif data[i][0:1]== '1':
                        tipo1 += 1
                        regType1(data[i], cur)
                        conn.commit()            
                    elif data[i][0:1]== '2':
                        tipo2 += 1
                        regType2(data[i], cur)
                        conn.commit()   
                    elif data[i][0:1]== '3':
                        tipo3 += 1
                        regType3(data[i], cur)
                        
                    elif data[i][0:1]== '4':
                        tipo4 += 1
                        regType4(data[i], cur)
                        
                    elif data[i][0:1]== '5':
                        tipo5 += 1
                        regType5(data[i], cur)

                    elif data[i][0:1]== '9':
                        tipo9 += 1
                        regType9(data[i], cur)
                logger.info("\n**Register Counter**")
                logger.info("tipo_0: " + str(tipo0))
                logger.info("tipo_1: " + str(tipo1))
                logger.info("tipo_2: " + str(tipo2))
                logger.info("tipo_3: " + str(tipo3))
                logger.info("tipo_4: " + str(tipo4))
                logger.info("tipo_5: " + str(tipo5))
                logger.info("tipo_9: " + str(tipo9))
                logger.info("*******************")
            conn.commit()
    os.remove(os.path.join(BASE_DIR,filename))