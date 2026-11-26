import { Component, signal } from '@angular/core';
import { LiComponent } from '../component/li-component/li-component';
import { InitPage } from '../component/cours/init-page/init-page';

@Component({
  imports: [LiComponent, InitPage],
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
