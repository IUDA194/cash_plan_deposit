from db import (
    connect_to_postgres, update_user_balances
    )

cursor = connect_to_postgres()

update_user_balances(cursor=cursor)