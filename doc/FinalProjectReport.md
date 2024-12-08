# **Final Report:** *Currents*

Mutma A. (adebayo5), Maciek H. (mhryc3), Anagha S. (anaghas2), Aishwarya P. (apasham2)

- - -

<sup> Table of Contents

[1. Shifts in Project Focus](#shifts-in-project-focus)

[2. Usefulness](#usefulness)

[3. Changes](#changes)

- [3a. Schema and Data](#schema-and-data)
- [3b. ER Diagram and Table Implementations](#er-diagram-and-table-implementations)
- [3c. Functionalities](#functionalities)

[4. Database Operations & Application Enhancement](#database-operations--application-enhancement)

[5. Technical Challenges](#technical-challenges)

[6. Future Work](#future-work)

[7. Team Contributions](#team-contributions)


## Shifts in Project Focus

**Please list out changes in the directions of your project if the final project is different from your original proposal (based on your stage 1 proposal submission).**

The original goal of our project, Currents, was to create a dashboard that allows users to explore meteorological and marine data with visualizations that highlight forecasted and historical weather trends. However, due to time and resource constraints, we had to limit the scope of our project, while still working with the same data. We decided to focus on displaying our data in tables rather than including map based visualizations. Our final product is an educational app dedicated to providing middle school students with weather and ocean species related data, helping them answer interesting questions about this data.

## Usefulness

**Discuss what you think your application achieved or failed to achieve regarding its usefulness.**

The original dataset spanned the entire United States, so if we included all of the data, we would have had millions of rows in our database and quickly ran out of GCP credits. Instead, we decided to limit the geographical bounds of the data to the East Coast. Our application was successful in terms of usefulness since the users could still learn about weather and biodiversity metrics in this limited geographic area through the insightful tables presented rather than an interactive map visual as originally proposed.

## Changes

### Schema and Data

**Discuss if you changed the schema or source of the data for your application.**

We kept the schema and data sources the same, but we needed to change the attributes in the Sessions table, as is shown with the table creation command below. 

```sql
CREATE TABLE Sessions(
    session_id INT PRIMARY KEY,
    min_lat INT,
    max_lat INT,
    min_long INT,
    max_long INT,
    rerun BOOLEAN,
    timestamp INT);
```

We discuss our need for this change in the following sections of this report.

### ER Diagram and Table Implementations

**Discuss what you changed to your ER diagram and/or your table implementations. What are some differences between the original design and the final design? Why? What do you think is a more suitable design?**

We made changes to the Sessions table. We decided to directly store the user inputs, rather than the query as this would help with storage. In addition, we implemented a trigger that would update whether user inputs were rerun with the boolean rerun column. In addition, we used a procedure to drop duplicate data, which prevents redundancy and limits how much data is stored using logic involving the rerun and timestamp columns. We also thought that storing the values of the user inputs is useful as the user would be more interested in seeing which values they previously tried rather than a query stored in the database. Our new changes are more of a suitable design because they aid with limiting storage and are more useful for the user.

Our changes to the Sessions table are reflected in the following Stage 3 files: `DatabaseDesign.md` (diagram, relational schema, and 3NF) and `DatabaseImplementationIdx.md` (table creation command).

### Functionalities

**Discuss what functionalities you added or removed. Why?**

We limited the number of filter functionalities on our project. We originally planned to allow users to be able to filter by date, NaturalDisaster name, and OceanSpecies name. However, we decided to instead allow users to filter by latitude and longitude, so that they could then learn about the natural disasters and ocean species occurring in that area. This allows the user to have access to as much data as possible for learning purposes.

Additionally, when a user looked at the Sessions history table, we wanted users to be able to click on the table row and have the previous query data displayed on the front end. Due to limited time, we instead decided that we would store the previous values that the user had entered so that they could re-enter them again if they wanted to see the data output once more. We also included a column ‘Rerun’ which was 1 if that specific query had been run prior, and 0 if it had not yet been.

Finally, in order to focus on our database schema and implement advanced logic such as procedures, transactions, and triggers, we decided to limit our front-end focus by moving away from a map visualization of the data and instead display the data output in a table on the front end.

## Database Operations & Application Enhancement

**Explain how you think your advanced database programs complement your application.**

When a user enters bounds on location, we use stored procedures to execute queries on the NaturalDisaster table and the OceanSpecies table and return results within those bounds. We use a transaction that bundles both an insert (trigger) and a procedure to remove repeated queries in the user’s search history. We have advanced queries that serve as data discovery features on our application, helping the audience answer interesting questions about the data. All of these work to make the database operations more streamlined and efficient as well as ultimately helping to improve the user experience.

## Technical Challenges

**Each team member should describe one technical challenge that the team encountered. This should be sufficiently detailed such that another future team could use this as helpful advice if they were to start a similar project or where to maintain your project.**

1. Mapping specific longitude and latitudes to region IDs

One technical challenge we faced was mapping the longitude and latitudes to specific regions. We had to map the coordinates in the data we originally received to a list of arbitrary regions. To do this, we first made a Python script to generate a CSV that defined the regions. Then we used another script to label each entry in the CSVs of the data and remove the entries that don't fall into any region. This was slightly complicated by the ocean species data being too large to fit into memory, so we had to make sure that the script could process a significant part of the corresponding data file to ensure we had enough entries in the database.

2. Generating and storing user queries

An issue we ran into when generating and storing user queries occurred when we were trying to post the user data to the backend. To get user data, we created a FormData object that took in the values the user put in for minimum latitude, maximum latitude, minimum longitude, and maximum longitude. When the user pressed submit on the front end, the data was collected, stored, and posted to the backend. Initially, however, we were unable to get the user query on the backend. Through rigorous testing, we ultimately found the bug which was that we were accidentally indexing a nonexistent column in the data, which caused the data to return nothing. Once we fixed that by indexing into the correct columns, we were able to parse the user inputs and query our GCP database in order to obtain and display the correct data output on the front end.

3. Connecting the backend to frontend

A challenge we encountered was connecting our Flask backend to the frontend of our application. We needed to make sure that the backend, database, and frontend were functioning as expected. We explored libraries such as flask_cors, google.cloud.sql.connector, pymysql, and sqlalchemy, which helped us properly connect to our database on GCP and connect the flask backend to the database. In addition, we rigorously tested each step, such as connection to the database, GET/POST methods in backend, and displaying query results in tables on the frontend, to ensure that all components of the application are integrated.

4. Implementing the sessions table and writing a trigger to maintain it

One of the goals of our project is to save previously entered queries so that users can access their search history. However, we quickly realized during the planning phase that this would likely be a large memory requirement as searches accumulated. Our initial logic here was to remove queries older than a certain time with a trigger. However, we encountered an issue during implementation: this trigger would have run both an insert and delete on the same table, which is not permitted due to the risk of deadlock. As such, we had to change our database design for Sessions, thinking about how best to add attributes that could be used to determine whether a row should be deleted. We decided to add an attribute that checks whether or not a query has already been run, so that the trigger could update this attribute when it finds another entry in the table with the same query. Duplicate queries are deleted after the trigger has completed its updates. Additionally, to avoid the need for excessive data parsing, we store the individual values that are part of the query, rather than a string of the entire query itself.

## Future Work

**Describe future work that you think, other than the interface, that the application can improve on.**

With additional time, we would try to implement more functionalities from our original plan. While we did accomplish a significant portion of our stretch goals, we decided not to include all the search filters. In the future, these search filters have the potential to make our application more useful by including filters for date, natural disaster attributes, and ocean species attributes. Beyond our original plan, if we were to implement this functionality, we would also have to implement a more robust session-storing mechanism which would scale with more users.

## Team Contributions

**Describe the final division of labor and how well you managed teamwork.**

All team members were assigned responsibilities. Most tasks were assigned in pairs, so we utilized communication tools and planning strategies to set time to work on them together.

Overall:
- All members - Tested application rigorously

Frontend:
- All members - Enable user interaction / user input retrieval
- Mutma, Anagha, Aishwarya - Design theme and aesthetics

Backend:
- Anagha, Aishwarya - Handle API calls to get and process data
- Maciek - Transform the processed data
- All members - Design database and put on GCP
- All members - Update queries live using user input, and save query result
- Maciek, Anagha, Aishwarya - Integrate frontend and backend



