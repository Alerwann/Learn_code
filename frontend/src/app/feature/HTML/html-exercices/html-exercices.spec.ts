import { ComponentFixture, TestBed } from '@angular/core/testing';
import { HtmlExercices } from './html-exercices';

describe('HtmlExercices', () => {
  let component: HtmlExercices;
  let fixture: ComponentFixture<HtmlExercices>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [HtmlExercices],
    }).compileComponents();

    fixture = TestBed.createComponent(HtmlExercices);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
