
import re
import pyodbc
import strconn

def runQry(qry2exec, qryparam):
    connectionString = strconn.GetConnectionString()
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    cursor.execute(qry2exec, qryparam)
    qryresult = cursor.fetchone()

    return qryresult
