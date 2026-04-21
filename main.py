import sys
from app.cli import ingest, data, total, category, date_filter

if len(sys.argv) < 2:
    print("Usage:")
    print("python main.py ingest")
    print("python main.py data")
    print ("python main.py total")
    print("python main.py category")
    print("python main.py date YYYY-MM-DD")
    sys.exit()

command = sys.argv[1] 

if command == "ingest":
    ingest()

elif command == "data":
    data()

elif command == "total":
     total()

elif command == "category":
    category()

elif command == "date":
    date_filter(sys.argv[2])

else:
    print("Invalid command")