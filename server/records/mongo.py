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
def createManyRecord(data):
    settings.MONGO_DB['records'].insert_many(data)
def getMostRecentRecords(query):
    pipeline = [
        {
            '$match': query
        },
        {
            '$group': {
                '_id': '$id_acordao',
                'most_recent_record_added_at': {'$max': '$record_added_at'}
            }
        },
        {
            '$lookup': {
                'from': 'records',
                'localField': '_id',
                'foreignField': 'id_acordao',
                'as': 'documents'
            }
        }
    ]
    result = settings.MONGO_DB['records'].aggregate(pipeline)

    return list(map(lambda x:x['documents'],result))[0]
    
def deleteRecord(id):
    #Returns True on Success
    result = settings.MONGO_DB['records'].delete_one({'_id': id})
    return result.deleted_count > 0




def getOnechangeRequest(id):
    return settings.MONGO_DB['changeRequests'].find_one({'_id':id})
  
def createchangeRequest(data):
    result = settings.MONGO_DB['changeRequests'].insert_one(data)
    if result.inserted_id:
        return getOnechangeRequest(result.inserted_id)
    else:
        return None
    pass
def deletechangeRequest(id):
    result = settings.MONGO_DB['changeRequests'].delete_one({'_id': id})
    return result.deleted_count > 0
    
