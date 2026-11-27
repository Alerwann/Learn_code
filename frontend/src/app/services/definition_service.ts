import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';
import { DefinitionIn, DefinitionOut } from '../shared/models/definition_model.model';

@Injectable({
  providedIn: 'root',
})
export class DefinitionService {
  private readonly http = inject(HttpClient);
  private readonly apiUrl = 'http://localhost:8000/definition';

  getDefinitions(): Observable<DefinitionOut[]> {
    return this.http.get<DefinitionOut[]>(this.apiUrl);
  }

  getDefinitionById(def_id: number): Observable<DefinitionOut> {
    return this.http.get<DefinitionOut>(`${this.apiUrl}/${def_id}`);
  }

  getDefinitionByCategory(def_category: string): Observable<DefinitionOut[]> {
    return this.http.get<DefinitionOut[]>(`${this.apiUrl}/category/${def_category}`);
  }

  createDefinition(payload: DefinitionIn): Observable<DefinitionOut> {
    return this.http.post<DefinitionOut>(this.apiUrl, payload);
  }

  updateDefinition(def_id: number, payload: DefinitionIn): Observable<DefinitionOut> {
    return this.http.put<DefinitionOut>(`${this.apiUrl}/${def_id}`, payload);
  }

  deleteDefinition(def_id: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}/${def_id}`);
  }
}
