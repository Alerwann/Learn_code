import { ComponentFixture, TestBed } from '@angular/core/testing';
import { InfoSite } from './info-site';

describe('InfoSite', () => {
  let component: InfoSite;
  let fixture: ComponentFixture<InfoSite>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [InfoSite],
    }).compileComponents();

    fixture = TestBed.createComponent(InfoSite);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
