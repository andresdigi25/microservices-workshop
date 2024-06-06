import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Data } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class ServiceAService {

  constructor(private http: HttpClient) {
  }

  getTodos(){
    return this.http.get<Data[]>('/api-a/todos')
  }

}
