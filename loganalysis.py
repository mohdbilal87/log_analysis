#! /usr/bin/env python

# importing package to connect to postgre database
import psycopg2

DBNAME = "news"

query1 = '''
select articles.title AS TITLE, count(*) as VIEWS
   from articles,log
   where log.path like
   concat('%', articles.slug, '%') AND
   log.status like '%200%'
   group by articles.title
   order by VIEWS desc
   limit 3;
'''

query2 = '''
select authors.name AS AUTHOR, count(*) as VIEWS
   from authors,articles,log
   where authors.id=articles.author AND
   log.path like concat('%', articles.slug, '%') AND
   log.status like '%200%'
   group by authors.name
   order by VIEWS desc;
'''

# before running the 3rd query
# please run the two queries as mentioned in README file
# to create required VIEWS status_counts and total_requests
query3 = '''
select status_counts.date as DATE,
ROUND((100*status_counts.total/total_requests.total::NUMERIC),2)
as percentage
   from total_requests,status_counts
   where total_requests.date=status_counts.date AND
   status_counts.status LIKE ('%404%') AND
   ROUND((100*status_counts.total/total_requests.total::NUMERIC),2)>1;
'''

print("Log Analysis Results:")


def main():
    # connecting to DB and running Queries.
    try:
        db = psycopg2.connect(database=DBNAME)
        cursor = db.cursor()

        print("Query 1:")
        print("What are the most popular three articles of all time?")
        cursor.execute(query1)
        for articles in cursor.fetchall():
            print("{} - {}".format(articles[0], articles[1]))

        print("Query 2:")
        print("Who are the most popular article authors of all time?")
        cursor.execute(query2)
        for authors in cursor.fetchall():
            print("{} - {}".format(authors[0], authors[1]))

        print("Query 3:")
        print("On which days did more than 1% of requests lead to errors?")
        cursor.execute(query3)
        for errors_404 in cursor.fetchall():
            print("{} - {}".format(errors_404[0], errors_404[1]))

        # closing connection with DB
        cursor.close()
        db.close()

    except:
        print("Database can't be reached")


if __name__ == "__main__":
    main()
