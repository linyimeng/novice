import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
   moduleId: module.id,
   selector: 'date-sales-reports-right-title',
   templateUrl: 'date-sales-reports-right-title.component.html'
})
export class DateSalesReportsRightComponent {
    constructor(
        private router:Router
    ) {}  
}

