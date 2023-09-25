# 3. Django ORM & Databases

# 3.1. Given the BlogPost model above, retrieve all BlogPosts written by a User with username 'john_doe'.
# Write the query below:

# posts_by_john = ?


import sqlite3
import logging
logging.basicConfig( filemode = 'w', format='%(asctime)s - %(message)s', 
                    datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)

""" create a database connection to the SQLite database
        specified by the db_file relative to the script.
    """
class SqliteQueryHandler():
    def __init__(self):
        self.db_path = 'db.sqlite3'
        self.conn = sqlite3.connect(self.db_path)
        self.mycursor = self.conn.cursor()

    def create_connection(self):
        try:
            self.conn = sqlite3.connect(self.db_path)
            logging.info("Connection Established.....")
            self.mycursor = self.conn.cursor()
            logging.info("Cursor Established.....")
        except Exception as e:
            logging.info(e)
    
    
    def retrieve_post_by_user(self, author_name):
        self.mycursor.execute("SELECT title,content,publish_date FROM blogpost_blogpost INNER JOIN auth_user ON blogpost_blogpost.author_id = auth_user.id WHERE auth_user.username =?", (author_name,))
        rows = self.mycursor.fetchall()
        for x in rows:
            print(x)
            print("\n")

    
if __name__ == "__main__":
    query = SqliteQueryHandler()
    """To establish connection"""
    # query.create_connection()

    """Two users currently registered in the db 'baron_reed' and 'john_doe'.
        We will query only john_doe blogpostings (includes 'title', 'content', 'publish_date')"""
    
    query.retrieve_post_by_user("john_doe")


    
