import { Component} from '@angular/core';
import { Router } from '@angular/router';

@Component({
   moduleId: module.id,
   selector: 'department-title',
   templateUrl: 'departmenttitle.component.html'
})
export class DepartmenttitleComponent{
    create() {
        alert('新建');
    }
}

