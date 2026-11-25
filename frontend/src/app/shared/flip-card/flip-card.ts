import { Component, signal } from '@angular/core';

@Component({
  imports: [],
  selector: 'app-flip-card',
  styleUrl: './flip-card.css',
  templateUrl: './flip-card.html',
})
export class FlipCard {
  isFlipped = signal(false);

  toggle() {
    this.isFlipped.update((v) => !v);
  }
}
