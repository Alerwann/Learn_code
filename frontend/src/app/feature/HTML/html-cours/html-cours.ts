import { Component, signal } from '@angular/core';
import { LiComponent } from '../component/li-component/li-component';
import { InitPage } from '../component/cours/init-page/init-page';
import { FirstBalisePage } from '../component/cours/first-balise-page/first-balise-page';
import { HtmlExercices } from '../html-exercices/html-exercices';
import { MoreHtml } from '../component/cours/more-html/more-html';

@Component({
  imports: [LiComponent, InitPage, FirstBalisePage, HtmlExercices, MoreHtml],
  selector: 'app-html-cours',
  styleUrl: './html-cours.css',
  templateUrl: './html-cours.html',
})
export class HtmlCours {
  indexPage = signal(0);

  toggle(newInd: number) {
    this.indexPage.update((index) => newInd);
  }
}
