
La base de datos es Postgresql, luego de instarla crear las siguientes tablas:

CREATE TABLE projects (
    project_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    date DATE NOT NULL
);



CREATE TABLE stages (
    stage_id SERIAL PRIMARY KEY,
    description TEXT NOT NULL
);


CREATE TABLE project_stages (
    project_id INT NOT NULL,
    stage_id INT NOT NULL,
    assistant_id VARCHAR(50),
    stage_description TEXT,
    PRIMARY KEY (project_id, stage_id),
    FOREIGN KEY (project_id) REFERENCES projects (project_id),
    FOREIGN KEY (stage_id) REFERENCES stages (stage_id)
);



CREATE TABLE threads (
    thread_id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    stage_id INT NOT NULL,
    project_id INT NOT NULL,
    assistant_thread_id VARCHAR(100),  -- Nuevo campo alfanumérico de 100 caracteres
    FOREIGN KEY (stage_id) REFERENCES stages (stage_id),
    FOREIGN KEY (project_id) REFERENCES projects (project_id)
);


CREATE TABLE messages (
    thread_id INT NOT NULL,
    message_id SERIAL PRIMARY KEY,
    message TEXT NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    FOREIGN KEY (thread_id) REFERENCES threads (thread_id)
);


