#!/usr/bin/python

import cgi
import MySQLdb

# Connect to MySQL database
db = MySQLdb.connect(host="localhost", user="root", db="plant_cwjh2")

# Create a cursor object to execute queries
cur = db.cursor()

# Get form data
form = cgi.FieldStorage()

print "Content-type: text/html\r\n\r\n"

print "<html><head><title>Process Form</title>"
print "<style>"
print "*{box-sizing: border-box;}body {margin: 2%;}.topnav {display: flexjustify-content: space-between;}"
print "#topnav::before {content: '* ';color: red;}.text-box {width: 99%;height: 25px;margin-top: 1%;border: 1.5px solid #05ac53;border-radius: 5px;}"
print ".reset {border: none;background-color: white;text-decoration: underline;}"
print ".reset:hover {cursor: pointer;}"
print ".submit {width: 10%;height: 30px;margin: 0% 2%;background-color: #00d769;border: none;border-radius: 5px;color: white;}"
print ".submit:hover {cursor: pointer;background-color: #50e79f;}"
print "</style></head>"

print "<body><div align=center style='color:#05ac53;'><h1>Samples Database for Plant Species</h1><h2>Update/Delete Data in the Database</h2></div>"

if "update" in form:
    # Update operation
    selected_row = form.getvalue('selected_row')
    table = form.getvalue('selectForm')

    if selected_row:
        #print('Selected Row: ',selected_row)

        if table == "collectors":
            collectorID = selected_row
            query = "SELECT * FROM collectors WHERE collectorID = %s" % collectorID
            cur.execute(query)
            collector_data = cur.fetchone()

            if collector_data:
                print "<h2>Update Collector Data</h2>"
                print "<p>You are currently updating collectorID: %s </p>" % selected_row
                print "<form action='collectorsUpdate.py' method='post'>"
                print "<input type='hidden' name='selected_row' value='%s'>" % selected_row
                print "<input type='hidden' name='selectForm' value='%s'>" % table
                print "Collector Name: <input type='text' name='collector_name' value='%s'><br><br>" % collector_data[1]
                print "Organisation: <input type='text' name='organisation' value='%s'><br><br>" % collector_data[2]
                print "<input class='submit' type='submit' name='update' value='Update'>"
                print "</form>"
            else:
                print "<h2>Error: Collector ID not found.</h2>"
        elif table == "species":
            spID = selected_row
            query = "SELECT * FROM species WHERE spID = %s" % spID
            cur.execute(query)
            species_data = cur.fetchone()

            if species_data:
                print "<h2>Update Species Data</h2>"
                print "<p>You are currently updating spID: %s </p>" % selected_row
                print "<form action='speciesUpdate.py' method='post'>"
                print "<input type='hidden' name='selected_row' value='%s'>" % selected_row
                print "<input type='hidden' name='selectForm' value='%s'>" % table
                print "Species Name: <input type='text' name='species_name' value='%s'><br><br>" % species_data[3]
                print "Author: <input type='text' name='author' value='%s'><br><br>" % species_data[1]
                print "Year: <input type='text' name='year' value='%s'><br><br>" % species_data[2]
                print "<input class='submit' type='submit' name='update' value='Update'>"
                print "</form>"
            else:
                print "<h2>Error: Species ID not found.</h2>"
        elif table == "samples":
            sampleID = selected_row
            query = """SELECT species.spName, samples.sampleID, samples.locality, collectors.collectorName
                                   FROM species
                                   INNER JOIN samples ON species.spID = samples.spID 
                                   INNER JOIN collectors ON samples.collectorID = collectors.collectorID WHERE sampleID = %s""" % sampleID
            cur.execute(query)
            sample_data = cur.fetchone()

            if sample_data:
                print "<h2>Update Sample Data</h2>"
                print "<p>You are currently updating sampleID: %s </p>" % selected_row
                print "<form action='samplesUpdate.py' method='post'>"
                print "<input type='hidden' name='selected_row' value='%s'>" % selected_row
                print "<input type='hidden' name='selectForm' value='%s'>" % table

                # Get species data for dropdown menu
                query_species = "SELECT * FROM species"
                cur.execute(query_species)
                species_list = cur.fetchall()

                print "Species Name: <select name='spID'>"
                for species in species_list:
                    selected = "selected" if species[3] == sample_data[0] else ""
                    print "<option value='%s' %s>%s</option>" % (species[0], selected, species[3])
                print "</select><br><br>"

                # Get collector data for dropdown menu
                query_collectors = "SELECT * FROM collectors"
                cur.execute(query_collectors)
                collector_list = cur.fetchall()
print "Collector Name: <select name='collectorID'>"
                for collector in collector_list:
                    selected = "selected" if collector[1] == sample_data[3] else ""
                    print "<option value='%s' %s>%s</option>" % (collector[0], selected, collector[1])
                print "</select><br><br>"

                print "Locality: <input type='text' name='locality' value='%s'><br><br>" % sample_data[2]
                print "<input class='submit' type='submit' name='update' value='Update'>"
                print "</form>"
            else:
                print "<h2>Error: Sample ID not found.</h2>"
    else:
        print "<h2>Error: Please select a row to update.</h2>"

elif "delete" in form:
    # Delete operation
    selected_row = form.getvalue('selected_row')
    table = form.getvalue('selectForm')

    if selected_row:
        if table == "collectors":
            collectorID = selected_row
            query = "DELETE FROM collectors WHERE collectorID = %s" % collectorID
            cur.execute(query)
            db.commit()
            print "<h2>Collector data deleted successfully!</h2>"
        elif table == "species":
            spID = selected_row
            query = "DELETE FROM species WHERE spID = %s" % spID
            cur.execute(query)
            db.commit()
print "<h2>Species data deleted successfully!</h2>"
        elif table == "samples":
            sampleID = selected_row
            query = "DELETE FROM samples WHERE sampleID = %s" % sampleID
            cur.execute(query)
            db.commit()
            print "<h2>Sample data deleted successfully!</h2>"
    else:
        print "<h2>Error: Please select a row to delete.</h2>"

print "<br>"
print "<a href='manPage.cgi'>Go Back</a>"

print "</body></html>"