import { Component } from '@angular/core';
import { ButtonModule } from 'primeng/button';
import { PanelModule } from 'primeng/panel';
import { TableModule } from 'primeng/table';
import { ServiceAService } from '../services/service-a.service';
import { DemoAngularPyconComponent } from 'demo-angular-pycon';


interface Data {
  email: string,
  login_timestamps: string[],
  is_online: boolean,
  id: string,
  date: string
}

@Component({
  selector: 'app-page-a',
  standalone: true,
  imports: [ButtonModule, PanelModule, TableModule, DemoAngularPyconComponent],
  templateUrl: './page-a.component.html',
  styleUrl: './page-a.component.css'
})
export class PageAComponent {

  data!: Data[];

  constructor(private servicea: ServiceAService) { }

  ngOnInit() {
    this.servicea.getTrackers().subscribe((data: any) => {
      this.data = Object.keys(data).map((key) => {
        return { email: data[key].email, login_timestamps: data[key].login_timestamps, is_online: data[key].is_online, id: data[key].id, date: data[key].date }
      })
    })
  }

}
