import { Routes } from '@angular/router';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';
import { PageAComponent } from './page-a/page-a.component';

export const routes: Routes = [
  { path: 'home', component: PageAComponent },
  { path: '**', component: PageNotFoundComponent }
];
