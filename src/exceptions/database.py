import psycopg2


DuplicateKeyError = psycopg2.errors.UniqueViolation
