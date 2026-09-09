class Model:
    def __init__(self) -> None:
        pass

    def all(self):
   		# select * from users
        pass

    def find(self, id: str):
    	# select * from users where id = {id} limit 1
        pass

    def first(self):
    	# select * from users order by id asc limit 1
        pass

    def last(self):
    	# select * from users order by id desc limit 1
        pass

    def findBy(self, field: str, value: str):
   		# select * from users where {field} = {value}
        pass

    def update(self, data: dict):
    	# update users
     	# 	set {data}
      	# where id = id
        pass

    def delete(self):
    	# delete from users where id = {id}
        pass
