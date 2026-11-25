import { Component, signal } from '@angular/core';
import { FlipCard } from '../../../shared/flip-card/flip-card';

@Component({
  imports: [FlipCard],
  selector: 'app-home-html',
  styleUrl: './home-html.css',
  templateUrl: './home-html.html',
})
export class HomeHtml {
  isFlipped = signal(false);

  toggle() {
    this.isFlipped.update((v) => !v);
  }
}
