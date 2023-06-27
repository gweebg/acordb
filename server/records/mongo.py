from django.conf import settings

def getManyRecords(query):
    limit = query.pop("limit", None)
    skip = query.pop("skip", None)
    r = settings.MONGO_DB['records'].find(query)
    if skip is not None:
        r = r.skip(int(skip))
    if limit is not None:
        r = r.limit(int(limit))
    return list(r)

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
    def split_list(lst, size):
        return [lst[i:i+size] for i in range(0, len(lst), size)]
    for i in split_list(data,100):
        settings.MONGO_DB['records'].insert_many(i)

def getMostRecentRecords(query):
    limit = query.pop('limit',None)
    skip = query.pop('skip',None)
    sort = query.pop('sort',None)
    if limit:
        if not limit.isdigit():
            return None
        limit=int(limit)
    if skip:
        if not skip.isdigit():
            return None
        skip=int(skip)
    if sort:
        if sort not in ['asc','desc']:
            return None
        sort = 1 if sort == 'asc' else -1
    
    
    settings.MONGO_DB['records'].create_index([('id_acordao', 1), ('record_added_at', -1)])

    # Define the aggregation pipeline
    pipeline = [
        {'$match':query},
        # Sort by id_acordao and record_added_at in descending order
        {'$sort': {'id_acordao': 1, 'record_added_at': -1}},
        # Group by id_acordao and take the first document for each group
        {'$group': {
            '_id': '$id_acordao',
            'most_recent': {'$first': '$record_added_at'},
            'doc': {'$first': '$$ROOT'}
        }},
        # Replace the document with the nested doc field
        {'$replaceRoot': {'newRoot': '$doc'}}
    ]
    if sort is not None:
        pipeline.append({'$sort':{'record_added_at':sort}})
    if skip is not None:
        pipeline.append({'$skip':skip})
    if limit is not None:
        pipeline.append({'$limit':limit})
    # Execute the aggregation query
    result = settings.MONGO_DB['records'].aggregate(pipeline)
    return list(result)

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