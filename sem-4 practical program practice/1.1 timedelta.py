#timedelta

from datetime import datetime, timedelta
today = datetime.now()
future = today + timedelta(days=5)
print(future) 