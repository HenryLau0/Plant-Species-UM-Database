#!/usr/bin/python
import MySQLdb
import cgi
import cgitb
cgitb.enable()

db = MySQLdb.connect(host='localhost',
                     user='root',
                     db='sdps_wj')

cur = db.cursor()

form = cgi.FieldStorage()

selected_action = form.getvalue('manAction')
selected_table = form.getvalue('opt')
selected_record = form.getvalue('radio1')
collector_name = form.getvalue('collectorName')
collector_organisation = form.getvalue('collectorOrganisation')

print 'Content-type:text/html\r\n\r\n';
print '<html><head><title>Update Result</title></head><body>';
print '<h1 align=center style="color:3EAC41">Samples Database for Plant Species</h1>';
print '<h2 align=center style="color:3EAC41">Update / Delete Data in the Database</h2>';
print '</header>';

print '<h4 align=center>Selected Action: ' + selected_action + '</h4>';
print '<h4 align=center>Selected Table: ' + selected_table + '</h4>';
print '<h4 align=center>Selected Record: ' + selected_record + '</h4>';
print '<h4 align=center>Collector Name: ' + collector_name + '</h4>'
print '<h4 align=center>Collector Organisation: ' + collector_organisation + '</h4>';

update_query = "UPDATE collectors SET collectorName = %s, collectorOrganisation = %s WHERE collectorID = %s"

try:
    # Execute the UPDATE query
    cur.execute(update_query, (collector_name, collector_organisation, selected_record))

    # Commit the changes
    db.commit()

    print('<h2 align=center> Data successfully updated</h2>')
    print('<p align=center>Collector Name: ' + collector_name + '</p>')
    print('<p align=center>Collector Organisation: ' + collector_organisation + '</p>')
except Exception as e:
    # Print or log the error message
    print('An error occurred:', str(e))

print '<button onclick=window.location.href="manPage2.cgi";><<< Back</button></p>';
print '</body></html>';

# Close the cursor and database connection
cur.close()
db.close()
