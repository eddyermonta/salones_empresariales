CREATE OR REPLACE PROCEDURE InsertarCliente(
    IN p_identification VARCHAR(20),
    IN p_first_name VARCHAR(50),
    IN p_last_name VARCHAR(50),
    IN p_phone VARCHAR(15),
    IN p_email VARCHAR(50),
    IN p_department VARCHAR(50),
    IN p_city VARCHAR(50),
    IN p_age INTEGER
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO app_clients_client (identification, first_name, last_name, phone, email, department, city, age)
    VALUES (p_identification, p_first_name, p_last_name, p_phone, p_email, p_department, p_city, p_age);
END;
$$;
