from datetime import datetime

class StatusCode:
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NO_CONTENT = 204
    MOVED_PERMANENTLY = 301
    FOUND = 302
    NOT_MODIFIED = 304
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404

class StatusMessage:
    OK = 'OK'
    CREATED = 'CREATED'
    ACCEPTED = 'ACCEPTED'
    NO_CONTENT = 'NO CONTENT'
    MOVED_PERMANENTLY = 'MOVED PERMANENTLY'
    FOUND = 'FOUND'
    NOT_MODIFIED = 'NOT MODIFIED'
    BAD_REQUEST = 'BAD REQUEST'
    UNAUTHORIZED = 'UNAUTHORIZED'
    FORBIDDEN = 'FORBIDDEN'
    NOT_FOUND = 'NOT FOUND'


class MetadataType:
    RESERVED = 'RESERVED'
    CUSTOM = 'CUSTOM'
    MESSAGE = 'MESSAGE'
    NEW_USER = 'NEW_USER'

class Pagination:
    def __init__(self, page, per_page, total_count, items):
        self.page = page
        self.per_page = per_page
        self.total_count = total_count
        self.items = items

    def to_dict(self):
        return {
            'page': self.page,
            'per_page': self.per_page,
            'total_count': self.total_count,
            'items': self.items
        }


class Metadata:
    def __init__(self, type=MetadataType.RESERVED):
        self.type = type
        
    def to_dict(self):
        return {
            'timestamp': datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            'type': self.type,
            'version': 0.1
        }
    
class ResponseHelper:
    def __init__(self, status, message, data, pagination={}, metadata=Metadata()):
        self.status = status
        self.message = message
        self.data = data
        self.pagination = pagination
        self.metadata = metadata.to_dict()

    def to_dict(self):
        return  {
            'status': self.status,
            'message': self.message,
            'data': self.data,
            'pagination': self.pagination,
            'metadata': self.metadata
        }