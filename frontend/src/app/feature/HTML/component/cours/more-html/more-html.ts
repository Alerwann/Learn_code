import { Component } from '@angular/core';
import { SectionCours } from '../../section-cours/section-cours';
import { ɵEmptyOutletComponent } from '@angular/router';

@Component({
  imports: [SectionCours],
  selector: 'app-more-html',
  styleUrl: './more-html.css',
  templateUrl: './more-html.html',
})
export class MoreHtml {}
