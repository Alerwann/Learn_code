import { Component, output, input } from '@angular/core';
import { EventEmitter } from '@angular/core';
@Component({
  imports: [],
  selector: 'app-li-component',
  styleUrl: './li-component.css',
  templateUrl: './li-component.html',
})
export class LiComponent {
  select = output<void>();
}
