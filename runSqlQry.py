
import re
import pyodbc
import strconn

#Open New Database Connection With Cursor
def newDbConCursor():
    connectionString = strconn.GetConnectionString()
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    return cursor


#Execute Any NonQuery
def runQry(qry2exec, qryparam):
    cursor = newDbConCursor()
    cursor.execute(qry2exec, qryparam)
    qryresult = cursor.fetchone()
    return qryresult


#Method to Execute Save/Update/Delete queries with Commit
def runQryWithCommit(qry2exec, qryparam):
    cursor = newDbConCursor()
    cursor.execute(qry2exec, qryparam)
    cursor.commit()
   