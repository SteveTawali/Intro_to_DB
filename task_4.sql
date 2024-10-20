USE alx_book_store;

SELECT column_name, data_type, is_nullable, column_default
FROM information_schema.columns
WHERE table_name = 'books'
AND table_schema = 'alx_book_store';
