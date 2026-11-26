import { Routes } from '@angular/router';
import { Home } from './feature/home/home';
import { HomeHtml } from './feature/HTML/home-html/home-html';
import { HtmlCours } from './feature/HTML/html-cours/html-cours';

export const routes: Routes = [
  {
    path: '',
    redirectTo: 'home',
    pathMatch: 'full',
  },
  {
    path: 'home',
    title: 'Accueil',
    component: Home,
  },
  {
    path: 'html',
    title: 'HTML',
    component: HomeHtml,
  },
  {
    path: 'html/cours',
    title: 'Cours',
    component: HtmlCours,
  },
];
