import { Component, inject } from '@angular/core';
import { Cardcomponent } from '../../shared/cardcomponent/cardcomponent';
import { toSignal } from '@angular/core/rxjs-interop';
import { AccueilCardService } from '../../services/accueil-card';

@Component({
  imports: [Cardcomponent],
  selector: 'app-home',
  styleUrl: './home.css',
  templateUrl: './home.html',
})
export class Home {
  title = 'home';
  private readonly accueilCardService = inject(AccueilCardService);

  items = toSignal(this.accueilCardService.getCards(), { initialValue: [] });
}
