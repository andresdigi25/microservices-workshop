import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ServiceAService {

  constructor(private http: HttpClient) {
  }

  getUsers(){
    return this.http.get('/api-b/users')
  }

}
