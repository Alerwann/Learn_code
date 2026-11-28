SET NAMES utf8mb4;

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

INSERT INTO balise_info(balise_type,balise_name,balise_exemple,balise_explication) VALUES
('Entête de la page','header','<header>Contenu</header>', 'Partie du haut de la page qui contient souvent un logo un titre et la navigation'),
('Pied de page','footer','<footer>Contenu</footer', 'Partie tout en bas de la page. Contient les informations légales, les informations sur l''entreprise'),
('Navigation','nav','<nav>Contenu</nav>', 'Ensemble des liens permettant de naviguer sur les pages principales du site'),
('Corps de la page','main','<main>Contenu</main>', 'Entre le header et le footer, cette partie contient le contenu principal de la page'),
('Titre','h1, h2, .... , h6','<h1>Titre</h1>','La lettre h vient de heading en anglais qui veut dire titre/en-tête de section. Le chiffre représente sa place dans la hiérarchie des titres. Il ne faut qu''un h1 par page pour le SEO. Le respect de l''ordre des indices et le fait de ne pas en sauter est aussi important.'),
('Paragraphe','p','<p>Paragraphe</p>', '<p> Permet d''encadrer une ou plusieurs phrases'),
('Contenaire de liste','ul ou uo','<ul>Liste</ul>', 'Encadre les éléments d''une liste. Si celle si est ordonnée utiliser uo'),
('Élement d''une liste','li','<li>Element</li>','Doit être utiliser dans un ul ou uo obligatoirement'),
('Section','section','<section>Contenu</section>','La section regroupe plusieurs éléments qui ne peuvent être regroupé dans un champs sémentique'),
('Lien','a','<a href="Lien vers la page ou l''élément">Text qui sera cliquable</a>', 'Le lien a un attribut href pour savoir vers où rediriger au clique'),
('Article',
  'article',
  '<article>
        <h?>Titre de l''article</h?>
        <section>Contenu</section>
   </article>',
  'L''article contient obligatoirement un titre et un enfant(contenu)'),
  ('Contenaire général','div','<div>Contenu</div>','Contenaire général à utiliser uniquement pour la mise en page'),
  ('Image','img','<img src="asset/img.webp" alt="description de l''image"/>','Pour afficher l''image, il faut 2 attributs : src qui est le chemin vers la source de l''image et alt, pour alternatif, qui est le text qui remplace l''image si elle ne s''affiche pas et sert pour les lecteur d''écran pour les personnes malveillantes'),
  ('br','br','<br>','Balise permettant de forcer un retour à la ligne');

INSERT INTO all_definition(def_name,def_description,def_category) VALUES
('BALISES','Nom donné pour définir un élément de la page. Chaque nom de balise est entouré de < et >. Les balises sont obligatoirement ouvertes et fermées.','html'),
('BALISES AUTO-FERMANTES',' Certaines balises ont la particularités de se fermer automatiquement. Elles sont appelé élements vide(void element en Anglais). Elles n''ont pas besoin de balise de fermeture et, même si votre IDE l''ajoute, un / n''est pas nécessaire pour la fermer.','html'),
('ATTRIBUT', "Élement que l'on peut ajouter pour préciser le comportement, l'apparence ou la fonctionnalité. Il doit être inscrit dans une balise ouvrante.",'html');