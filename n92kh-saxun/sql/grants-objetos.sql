SELECT 'GRANT EXECUTE ON ' || OWNER || '.' || OBJECT_NAME 
   || ' TO ' || :DESTINO || ';' "GRANT"
FROM ALL_OBJECTS
WHERE OWNER = :PROPIETARIO
  AND OBJECT_TYPE IN ('FUNCTION', 'PACKAGE', 'PROCEDURE')
ORDER BY OBJECT_TYPE, OBJECT_NAME;
  
SELECT DISTINCT OBJECT_TYPE
FROM ALL_OBJECTS
WHERE OWNER = 'MEXICO01';