import { ComponentFixture, TestBed } from '@angular/core/testing';
import { MoreHtml } from './more-html';

describe('MoreHtml', () => {
  let component: MoreHtml;
  let fixture: ComponentFixture<MoreHtml>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MoreHtml],
    }).compileComponents();

    fixture = TestBed.createComponent(MoreHtml);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
