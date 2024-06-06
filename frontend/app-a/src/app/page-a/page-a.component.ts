import { Component } from '@angular/core';
import { ButtonModule } from 'primeng/button';
import { PanelModule } from 'primeng/panel';
import { TableModule } from 'primeng/table';
import { ServiceAService } from '../services/service-a.service';
import {addStringToDate} from 'demo-angular-pycon'

@Component({
  selector: 'app-page-a',
  standalone: true,
  imports: [ButtonModule, PanelModule, TableModule],
  templateUrl: './page-a.component.html',
  styleUrl: './page-a.component.css'
})
export class PageAComponent {

  data!: any;

  constructor(private servicea: ServiceAService) { }

  ngOnInit() {
    this.servicea.getTodos().subscribe((data : any) => {
      this.data = Object.keys(data).map((key) => {
        return {task: data[key].task, id: data[key].id, date: addStringToDate(data[key].date)}
      })
    })
  }

}
