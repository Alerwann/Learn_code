import { ComponentFixture, TestBed } from '@angular/core/testing';
import { SectionCours } from './section-cours';

describe('SectionCours', () => {
  let component: SectionCours;
  let fixture: ComponentFixture<SectionCours>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SectionCours],
    }).compileComponents();

    fixture = TestBed.createComponent(SectionCours);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
