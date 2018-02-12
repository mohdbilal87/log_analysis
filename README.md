# Log Analysis Project

**Log Analysis Project** is the 3rd and last project for Udacity full stack web dev course from part 1.

## Main files

Following are the files with their brief description:
<ul>
    <li>loganalysis.py: This file implements the main logic of SQL queries and tries to answer the 3 main questions of the asisgment from **news** database.
    </li>
    <li>result.txt: This file has the result from stdout when *loganalysis.py* file is run.</li>
</ul>

## Running the project.
<ul>
    <li>Spin up the virtual box: `vargant up`</li>
    <li>Login to virtual machine: `vargant ssh`</li>
    <li>go to directory where sql file is kept: `cd /vagrant`</li>
    <li>The following postgre command will import the sql file and populate tables in **news** DB: `psql -d news -f newsdata.sql`</li>
    <li>Enter the DB: `psql news`</li>
    <li>We will need to create two views. This is required to answer the third question about error logs:
      <ul>
          <li>`create view total_requests as                                                
   select date(time) as date, count(*) as total
   from log group by date;`</li>
          <li>`create view status_counts as                                                
   select date(time) as date,status, count(*) as total
   from log group by date,log.status;`</li>
      </ul>
    </li>
    <li>Exit the DB and run the python script: `python3 loganalysis.py`</li>
<ul>

## LICENSE
Much of the code is inspired from the content videos themselves and some documentation from the web.

All the code listed above is  <a href="https://opensource.org/licenses/MIT">MIT Licensed</a>.
