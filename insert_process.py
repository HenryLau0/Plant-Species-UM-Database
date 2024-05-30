#!/usr/bin/python

import cgi
import MySQLdb

# Connect to MySQL database
db = MySQLdb.connect(host="localhost", user="root", db="plant_cwjh2")

# Create a cursor object to execute queries
cur = db.cursor()

# Get form data
form = cgi.FieldStorage()

# Check if form is submitted
if form.getvalue('selectForm') and form.getvalue('submit'):
    # Get the selected table and form inputs
    table = form.getvalue('selectForm')

    if table == 'collectors':
        collectorName = form.getvalue('collectorName')
        organisation = form.getvalue('organisation')
        query = "INSERT INTO collectors (collectorName, collectorOrganisation) VALUES ('%s', '%s')" % (co$
    elif table == 'species':
        spName = form.getvalue('spName')
        authorship = form.getvalue('authorship')
        year = form.getvalue('year')
        query = "INSERT INTO species (spAuthors, spYear, spName) VALUES ('%s', '%s', '%s')" % (authorship$
    elif table == 'samples':
        spID = form.getvalue('spID')
        collectorID = form.getvalue('collectorID')
        locality = form.getvalue('locality')
        query = "INSERT INTO samples (spID, collectorID, locality) VALUES ('%s', '%s', '%s')"% (spID, col$

    # Execute
    cur.execute(query)
    # Commit the changes to the database
    db.commit()

    # Display success message
    print "Content-type: text/html\r\n\r\n"
    print "<html><head><title>Success</title></head>"
    print "<body>"
    print "<h1>Data inserted successfully</h1><br><br>"
    print "<p><button onclick='window.location.href=\"insertPage.cgi\"'><<< Insert Page</button>"
    print "<button onclick='window.location.href=\"listCollectors.cgi\"'>>>> List of <b>Collectors</b></b$
    print "<button onclick='window.location.href=\"listofSpecies.cgi\"'>>>> List of <b>Species</b></butto$
    print "<button onclick='window.location.href=\"listSamples.cgi\"'>>>> List of <b>Samples</b></button>$
    print "</body></html>"

else:
    # Display error message
    print "Content-type: text/html\r\n\r\n"
    print "<h1>Error: Form not submitted.</h1>"

# Close the database connection
db.close()