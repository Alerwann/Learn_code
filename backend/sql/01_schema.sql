CREATE TABLE role(
    role_id INT AUTO_INCREMENT PRIMARY KEY,
    role_nom VARCHAR(50) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE utilisateur(
    utilisateur_id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL, 
    pseudo VARCHAR(50) NOT NULL,
    is_actif BOOLEAN DEFAULT TRUE,
    role_id INT NOT NULL, 
    CONSTRAINT fk_utilisateur_role FOREIGN KEY (role_id) REFERENCES role(role_id) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


CREATE TABLE user_quiz_results(
    quizz_result_id INT AUTO_INCREMENT PRIMARY KEY,
    quiz_id INT NOT NULL,
    quizz_note INT,
    utilisateur_id INT NOT NULL,
    CONSTRAINT fk_utilisateur_result FOREIGN KEY (utilisateur_id) REFERENCES utilisateur(utilisateur_id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


CREATE TABLE user_cours_suivi(
    user_cours_id INT AUTO_INCREMENT PRIMARY KEY,
    cours_id INT NOT NULL,
    progression DOUBLE,
    utilisateur_id INT NOT NULL,
    CONSTRAINT fk_utilisateur_cours FOREIGN KEY (utilisateur_id) REFERENCES utilisateur(utilisateur_id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;