import { Component } from '@angular/core';
import { CardsGrid } from './components/cards-grid/cards-grid';
import { InfoSite } from './components/info-site/info-site';

@Component({
  imports: [CardsGrid, InfoSite],
  selector: 'app-home',
  styleUrl: './home.css',
  templateUrl: './home.html',
})
export class Home {
  title = 'home';
}
