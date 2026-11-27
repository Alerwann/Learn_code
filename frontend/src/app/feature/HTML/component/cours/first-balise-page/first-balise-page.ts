import { Component, inject } from '@angular/core';
import { SectionCours } from '../../section-cours/section-cours';
import { BaliseInfoService } from '../../../../../services/balise_data';
import { toSignal } from '@angular/core/rxjs-interop';
import { DefinitionService } from '../../../../../services/definition_service';

@Component({
  imports: [SectionCours],
  selector: 'app-first-balise-page',
  styleUrl: './first-balise-page.css',
  templateUrl: './first-balise-page.html',
})
export class FirstBalisePage {
  private readonly baliseInfoService = inject(BaliseInfoService);
  private readonly definitionService = inject(DefinitionService);

  balises = toSignal(this.baliseInfoService.getBalises(), { initialValue: [] });
  definitions = toSignal(this.definitionService.getDefinitionByCategory('html'), {
    initialValue: [],
  });
}
