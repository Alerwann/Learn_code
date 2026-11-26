import { Component, signal } from '@angular/core';

@Component({
  imports: [],
  selector: 'app-init-page',
  styleUrl: './init-page.css',
  templateUrl: './init-page.html',
})
export class InitPage {
  aggrandi = signal(false);

  toggleZoom() {
    this.aggrandi.update((v) => !v);
  }
}
