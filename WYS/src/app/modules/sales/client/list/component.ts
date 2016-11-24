import { Component,OnInit} from '@angular/core';
import { CompanyService } from '../../../wysservices/company.service';

@Component({
   selector: 'client-list',
   templateUrl: 'list.html'
})

export class ClientListComponent implements OnInit {

    clients:any;

    constructor(
        private _supplierService:CompanyService
    ){}
    
    ngOnInit(){
        this._supplierService.get_client_list().subscribe(
            clients=>this.clients = clients,
            error=>alert(error)
        );
    }
}

