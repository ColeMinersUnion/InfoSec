<html>
<body>

<!--I have a psql database on postgresql://localhost:5500

I have a username and password for the database. 
I want to see if the username and password entered the form are correct. 
I want to return the first and last name and user name returned to the page.
The first and last name should be in a table, using the username as the key and 
the first and last name as well as the hashed password for values. 
If the username is already registered, it should return an error message, and request came from
index.php. 




-->

Welcome <?php echo $_POST["username"]; ?><br>

</body>
</html>
