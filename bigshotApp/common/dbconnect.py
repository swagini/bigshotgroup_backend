from django.db import connection

class query_executer(object):

    def get(functionname, params):
        cursor = connection.cursor()
        if params=={}:
            cursor.callproc(functionname)
        else:
            cursor.callproc(functionname, params)
        result = cursor.fetchall()
        connection.close()
        cursor.close()
        if(len(result) ==0):
            return []
        else:
            if result is None:
                return []
            else:
                return result[0][0]
            
    def post(functionname, params):
        cursor = connection.cursor()
        cursor.callproc(functionname, params)
        result = cursor.fetchall()
        connection.close()
        cursor.close()
        if(len(result)==0):
            return []
        else:
            if result is None:
                return []
            else:
                return result[0][0]
            
        
