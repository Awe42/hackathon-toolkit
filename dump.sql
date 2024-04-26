/* Use the following command in a terminal to dump the database:

docker exec -t db pg_dumpall -c -U postgres > dump_`date +%Y-%m-%d"_"%H_%M_%S`.sql

Rename the latest dump file to dump.sql and place it in the root of the project.
Then it will be automatically loaded into DB on startup.
*/