import { Component } from '@angular/core';
import { ButtonModule } from 'primeng/button';
import { PanelModule } from 'primeng/panel';
import { TableModule } from 'primeng/table';
import { ServiceAService } from '../services/service-a.service';
import { Data } from '../domain/data';


@Component({
  selector: 'app-page-a',
  standalone: true,
  imports: [ButtonModule, PanelModule, TableModule],
  templateUrl: './page-a.component.html',
  styleUrl: './page-a.component.css'
})
export class PageAComponent {

  data!: Data[];

  constructor(private servicea: ServiceAService) { }

  ngOnInit() {
    this.servicea.getTodos().subscribe((data) => {
      this.data = data
    })
  }

}
