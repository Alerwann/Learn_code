import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { AccueilCard } from '../feature/models/accueil-card/accueil-card.model';

@Injectable({
  providedIn: 'root',
})
export class AccueilCardService {
  private readonly http = inject(HttpClient);
  private readonly apiUrl = 'http://localhost:8000/accueil-cards';

  getCards(): Observable<AccueilCard[]> {
    return this.http.get<AccueilCard[]>(this.apiUrl);
  }

  getCardById(id: string): Observable<AccueilCard> {
    return this.http.get<AccueilCard>(`${this.apiUrl}/${id}`);
  }
}
