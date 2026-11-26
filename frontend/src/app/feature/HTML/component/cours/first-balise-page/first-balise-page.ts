import { Component, inject } from '@angular/core';
import { SectionCours } from '../../section-cours/section-cours';
import { BaliseInfoService } from '../../../../../services/balise_data';
import { toSignal } from '@angular/core/rxjs-interop';

@Component({
  imports: [SectionCours],
  selector: 'app-first-balise-page',
  styleUrl: './first-balise-page.css',
  templateUrl: './first-balise-page.html',
})
export class FirstBalisePage {
  private readonly baliseInfoService = inject(BaliseInfoService);
  balises = toSignal(this.baliseInfoService.getBalises(), { initialValue: [] });
}
