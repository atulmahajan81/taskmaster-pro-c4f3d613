-- Seed Users
INSERT INTO users (id, email, password_hash) VALUES
(gen_random_uuid(), 'admin@example.com', 'hashed_password1'),
(gen_random_uuid(), 'user1@example.com', 'hashed_password2'),
(gen_random_uuid(), 'user2@example.com', 'hashed_password3');

-- Seed Categories
INSERT INTO categories (id, user_id, name) VALUES
(gen_random_uuid(), (SELECT id FROM users WHERE email='admin@example.com'), 'Category 1 for admin@example.com'),
(gen_random_uuid(), (SELECT id FROM users WHERE email='admin@example.com'), 'Category 2 for admin@example.com'),
(gen_random_uuid(), (SELECT id FROM users WHERE email='admin@example.com'), 'Category 3 for admin@example.com'),
(gen_random_uuid(), (SELECT id FROM users WHERE email='user1@example.com'), 'Category 1 for user1@example.com'),
(gen_random_uuid(), (SELECT id FROM users WHERE email='user1@example.com'), 'Category 2 for user1@example.com'),
(gen_random_uuid(), (SELECT id FROM users WHERE email='user1@example.com'), 'Category 3 for user1@example.com'),
(gen_random_uuid(), (SELECT id FROM users WHERE email='user2@example.com'), 'Category 1 for user2@example.com'),
(gen_random_uuid(), (SELECT id FROM users WHERE email='user2@example.com'), 'Category 2 for user2@example.com'),
(gen_random_uuid(), (SELECT id FROM users WHERE email='user2@example.com'), 'Category 3 for user2@example.com');

-- Seed Tasks
INSERT INTO tasks (id, user_id, title, due_date, priority) VALUES
(gen_random_uuid(), (SELECT id FROM users WHERE email='admin@example.com'), 'Task 1 for admin@example.com', NOW()::date + INTERVAL '1 day', 'High'),
(gen_random_uuid(), (SELECT id FROM users WHERE email='admin@example.com'), 'Task 2 for admin@example.com', NOW()::date + INTERVAL '5 days', 'Medium'),
(gen_random_uuid(), (SELECT id FROM users WHERE email='admin@example.com'), 'Task 3 for admin@example.com', NOW()::date + INTERVAL '10 days', 'Low'),
(gen_random_uuid(), (SELECT id FROM users WHERE email='user1@example.com'), 'Task 1 for user1@example.com', NOW()::date + INTERVAL '2 days', 'Low'),
(gen_random_uuid(), (SELECT id FROM users WHERE email='user1@example.com'), 'Task 2 for user1@example.com', NOW()::date + INTERVAL '7 days', 'High'),
(gen_random_uuid(), (SELECT id FROM users WHERE email='user1@example.com'), 'Task 3 for user1@example.com', NOW()::date + INTERVAL '15 days', 'Medium'),
(gen_random_uuid(), (SELECT id FROM users WHERE email='user2@example.com'), 'Task 1 for user2@example.com', NOW()::date + INTERVAL '3 days', 'Medium'),
(gen_random_uuid(), (SELECT id FROM users WHERE email='user2@example.com'), 'Task 2 for user2@example.com', NOW()::date + INTERVAL '12 days', 'Low'),
(gen_random_uuid(), (SELECT id FROM users WHERE email='user2@example.com'), 'Task 3 for user2@example.com', NOW()::date + INTERVAL '20 days', 'High');