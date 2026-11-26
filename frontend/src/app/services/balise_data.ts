import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';
import { BaliseInfoIn, BaliseInfoOut } from '../feature/models/html/balise-info.model';

@Injectable({
  providedIn: 'root',
})
export class BaliseInfoService {
  private readonly http = inject(HttpClient);
  private readonly apiUrl = 'http://localhost:8000/balises';

  getBalises(limit = 100, offset = 0): Observable<BaliseInfoOut[]> {
    const params = new HttpParams().set('limit', limit).set('offset', offset);
    return this.http.get<BaliseInfoOut[]>(this.apiUrl, { params });
  }

  getBaliseById(id: number): Observable<BaliseInfoOut> {
    return this.http.get<BaliseInfoOut>(`${this.apiUrl}/${id}`);
  }

  createBalise(payload: BaliseInfoIn): Observable<BaliseInfoOut> {
    return this.http.post<BaliseInfoOut>(this.apiUrl, payload);
  }

  updateBalise(id: number, payload: BaliseInfoIn): Observable<BaliseInfoOut> {
    return this.http.put<BaliseInfoOut>(`${this.apiUrl}/${id}`, payload);
  }

  deleteBalise(id: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}/${id}`);
  }
}
