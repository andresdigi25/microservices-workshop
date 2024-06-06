import { TestBed } from '@angular/core/testing';

import { DemoAngularPyconService } from './demo-angular-pycon.service';

describe('DemoAngularPyconService', () => {
  let service: DemoAngularPyconService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(DemoAngularPyconService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
