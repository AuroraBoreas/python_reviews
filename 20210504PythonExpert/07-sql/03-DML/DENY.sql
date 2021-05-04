
CREATE ROLE testRole;

CREATE USER testUser WITHOUT LOGIN;

EXEC sp_addrolemember @rolename = 'testRole', @membername = 'testUser';