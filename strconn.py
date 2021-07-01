def GetConnectionString():
    driver = "{ODBC Driver 17 for SQL Server}"
    server = "DESKTOP-FGG3T35"
    database = "MSSQLTipsDb"
    username = "blak"
    password = "blak"
    connectionString = "DRIVER=" + driver + ";SERVER=" + server + ";DATABASE=" + database + ";UID=" + username + ";PWD=" + password
    return connectionString
