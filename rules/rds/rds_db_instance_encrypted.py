
import pytest


def is_rds_db_instance_encrypted(rds_db_instance):
    """
    Checks the RDS instance 'StorageEncrypted' value.

    >>> is_rds_db_instance_encrypted({'StorageEncrypted': True})
    True
    >>> is_rds_db_instance_encrypted({'StorageEncrypted': False})
    False
    >>> is_rds_db_instance_encrypted({})
    Traceback (most recent call last):
    ...
    KeyError: 'StorageEncrypted'
    >>> is_rds_db_instance_encrypted(0)
    Traceback (most recent call last):
    ...
    TypeError: 'int' object is not subscriptable
    >>> is_rds_db_instance_encrypted(None)
    Traceback (most recent call last):
    ...
    TypeError: 'NoneType' object is not subscriptable
    """
    return bool(rds_db_instance['StorageEncrypted'])


@pytest.mark.rds
def test_rds_db_instance_encrypted(rds_db_instance):
    assert is_rds_db_instance_encrypted(rds_db_instance)
