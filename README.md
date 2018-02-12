# Log Analysis Project

**Log Analysis Project** is the 3rd and last project for Udacity full stack web dev course from part 1.

## Main files

Following are the files with their brief description:
<ul>
    <li>loganalysis.py: This file implements the main logic of SQL queries and tries to answer the 3 main questions of the assignment from **news** database.</li>
    <li>result.txt: This file has the result from stdout when *loganalysis.py* file is run.</li>
</ul>

## Running the project.
* Spin up the virtual box: `vargant up`
* Login to virtual machine: `vargant ssh`
* go to directory where sql file is kept: `cd /vagrant`
* The following postgre command will import the sql file and populate tables in **news** DB: `psql -d news -f newsdata.sql`
    * Enter the DB: `psql news`
    * We will need to create two views. This is required to answer the third question about error logs:
      
          * `create view total_requests as select date(time) as date, count(*) as total from log group by date;`
          * `create view status_counts as select date(time) as date,status, count(*) as total from log group by date,log.status;`

    * Exit the DB and run the python script: `python3 loganalysis.py`

## LICENSE
Much of the code is inspired from the content videos themselves and some documentation from the web.

All the code listed above is  <a href="https://opensource.org/licenses/MIT">MIT Licensed</a>.
