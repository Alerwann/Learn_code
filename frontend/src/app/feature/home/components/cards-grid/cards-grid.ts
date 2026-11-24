import { Component, inject } from '@angular/core';

import { toSignal } from '@angular/core/rxjs-interop';
import { AccueilCardService } from '../../../../services/accueil-card';
import { Cardcomponent } from '../../../../shared/cardcomponent/cardcomponent';

@Component({
  imports: [Cardcomponent],
  selector: 'app-cards-grid',
  styleUrl: './cards-grid.css',
  templateUrl: './cards-grid.html',
})
export class CardsGrid {
  private readonly accueilCardService = inject(AccueilCardService);
  items = toSignal(this.accueilCardService.getCards(), { initialValue: [] });
}
