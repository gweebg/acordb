from django.conf import settings

def getManyRecords(query):
    return list(settings.MONGO_DB['records'].find(query))

def getOneRecord(id):
    return settings.MONGO_DB['records'].find_one({'_id':id})

def updateRecord(id,data):
    return settings.MONGO_DB['records'].find_one_and_update({'_id': id}, {'$set': data},return_document=True)

def createRecord(data):
    result = settings.MONGO_DB['records'].insert_one(data)
    if result.inserted_id:
        return getOneRecord(result.inserted_id)
    else:
        return None
    
def deleteRecord(id):
    #Returns True on Success
    result = settings.MONGO_DB['records'].delete_one({'_id': id})
    return result.deleted_count > 0
    
    
