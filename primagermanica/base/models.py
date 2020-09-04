import uuid

from pynamodb.attributes import UnicodeAttribute
from pynamodb.models import Model


class UUIDAttribute(UnicodeAttribute):

    def serialize(self, value):
        return super().serialize(str(value))

    def deserialize(self, value):
        return uuid.UUID(super().deserialize(value))


# Create your models here.
class Transaction(Model):
    """
    A DynamoDB Transaction Model
    """

    class Meta:
        table_name = "transaction"
        # todo why it's not accessing from docker network?
        host = "http://localhost:8000"
        aws_access_key_id = "developmentid"
        aws_secret_access_key = "developmentaccess"

    id = UUIDAttribute(default=uuid.uuid4)
    artist_name = UnicodeAttribute(hash_key=True)

    def __str__(self):
        return f'uuid:{self.id}, artist_name:{self.artist_name}'

    @classmethod
    def search_transaction(cls, name: str):
        try:
            return Transaction.get(name)
        except:
            return None


if not Transaction.exists():
    Transaction.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
