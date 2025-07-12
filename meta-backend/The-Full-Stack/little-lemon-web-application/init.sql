-- Initialize Little Lemon database
-- This script runs when the MySQL container starts for the first time

-- Create additional users if needed
-- The main database and user are created by environment variables

-- Set proper permissions
GRANT ALL PRIVILEGES ON *.* TO 'littlelemon_user'@'%';
FLUSH PRIVILEGES;
