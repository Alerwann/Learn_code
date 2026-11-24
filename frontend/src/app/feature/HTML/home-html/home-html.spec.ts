import { ComponentFixture, TestBed } from '@angular/core/testing';
import { HomeHtml } from './home-html';

describe('HomeHtml', () => {
  let component: HomeHtml;
  let fixture: ComponentFixture<HomeHtml>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [HomeHtml],
    }).compileComponents();

    fixture = TestBed.createComponent(HomeHtml);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
