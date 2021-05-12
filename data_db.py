import pymongo
import csv
#Replace your URL here. Don't forget to replace the password.
connection_url = "mongodb+srv://harsha:harsha@testcluster.aoaa1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = pymongo.MongoClient(connection_url)
Database = client.get_database('Articlesdb')
collection = Database.Articles
collection.delete_many({})
count=collection.count_documents({})
print(count)
with open("articles.csv","r") as csv_file:
    reader=csv.reader(csv_file)
    next(reader)
    Articles=[]
    for row in reader:
        Articles.append({'Article_Link':row[0],'Title':row[1],'Date':row[2],'Author':row[3],'Description':row[4],'Topic':row[5]})
collection.insert_many(Articles)
count=collection.count_documents({})
print(count)

    


