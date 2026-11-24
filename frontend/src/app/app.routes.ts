import { Routes } from '@angular/router';
import { Home } from './feature/home/home';
import { HomeHtml } from './feature/HTML/home-html/home-html';

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
];
