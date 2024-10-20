-- Query the INFORMATION_SCHEMA.COLUMNS table to describe the structure of the 'Books' table
SELECT COLUMN_NAME, COLUMN_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'alx_book_store' 
  AND TABLE_NAME = 'Books';
