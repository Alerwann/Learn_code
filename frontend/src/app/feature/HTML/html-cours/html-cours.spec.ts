import { ComponentFixture, TestBed } from '@angular/core/testing';
import { HtmlCours } from './html-cours';

describe('HtmlCours', () => {
  let component: HtmlCours;
  let fixture: ComponentFixture<HtmlCours>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [HtmlCours],
    }).compileComponents();

    fixture = TestBed.createComponent(HtmlCours);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
