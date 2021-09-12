
# Thoughts on current solution

The current solution works well, however there are lots of improvement
I would like to make in the future. 

- Instead of a csv_ingest directory, it could be more useful to write
the script to pull from a cloud provider service like AWS S3. 

- Implementing a way to have schema types automatically loaded and passed 
 around. As it stands my current solution relies on knowing the expected output 
 schema and datatypes to cast to. Some of the values are hadrcoded but it would 
 be great to pass in a schema type file and have the script detect it and check
 cast data accordingly. This would greatly increase the scripts flexibility.

- Implement more tests for edge cases and other scenarios I haven't thought of. 