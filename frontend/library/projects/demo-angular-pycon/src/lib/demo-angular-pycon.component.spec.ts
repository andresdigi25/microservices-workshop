import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DemoAngularPyconComponent } from './demo-angular-pycon.component';

describe('DemoAngularPyconComponent', () => {
  let component: DemoAngularPyconComponent;
  let fixture: ComponentFixture<DemoAngularPyconComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DemoAngularPyconComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DemoAngularPyconComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
