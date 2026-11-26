import { ComponentFixture, TestBed } from '@angular/core/testing';
import { FirstBalisePage } from './first-balise-page';

describe('FirstBalisePage', () => {
  let component: FirstBalisePage;
  let fixture: ComponentFixture<FirstBalisePage>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [FirstBalisePage],
    }).compileComponents();

    fixture = TestBed.createComponent(FirstBalisePage);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
