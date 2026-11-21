INSERT INTO role(role_nom) VALUES
('admin'),
('utilisateur');

INSERT INTO utilisateur (email, password, pseudo, is_actif, role_id) VALUES
('admin1@admin.com','$2y$10$abcdefghijklmnopqrstuvABCDEFGHIJKLMNOPQRSTUV0123456789xyz','admin',1,1 ),
('utilisateur@utilisateur.com','$2y$10$abcdefghijklmnopqrstuvABCDEFGHIJKLMNOPQRSTUV0123456789xyz','user',1,2);


INSERT INTO user_quiz_results(quiz_id,quizz_note,utilisateur_id) VALUES
(1,5,2),
(2,0,2);

INSERT INTO user_cours_suivi(cours_id,progression,utilisateur_id) VALUES
(1,0.80,2),
(2,0.25,2);