import { Component, signal } from '@angular/core';
import { Cardcomponent } from '../../shared/cardcomponent/cardcomponent';
import { AccueilCard } from '../models/accueil-card/accueil-card.model';

@Component({
  imports: [Cardcomponent],
  selector: 'app-home',
  styleUrl: './home.css',
  templateUrl: './home.html',
})
export class Home {
  title = 'home';

  readonly items = signal<AccueilCard[]>([
    {
      title: 'HTML',
      description: "Les bases pour comprendre le fonctionnement d'HTML",
      theme: 'Frontend',
      niveau: 'Facile',
    },
    {
      title: 'CSS',
      description: 'Apprendre mise en forme de votre page',
      theme: 'Frontend',
      niveau: 'Facile',
    },
    {
      title: 'Git/Github',
      description: 'Créer le versonning de ton projet',
      theme: 'Setup',
      niveau: 'Moyen',
    },
  ]);
}
